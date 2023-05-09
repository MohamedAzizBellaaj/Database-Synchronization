import json

import jsonpickle
import pika
from PySide6.QtWidgets import (
    QHBoxLayout,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QStackedWidget,
    QVBoxLayout,
    QWidget,
)

from bo.delete import DeleteWidget
from bo.insert import InsertWidget
from bo.update import UpdateWidget
from utils.db_connection import Database


class MainWindow(QMainWindow):
    def __init__(self, name: str):
        super().__init__()
        self.name = name
        self.logs_path = f"{self.name}/{self.name}_db_logs.json"
        self.db = Database("root", "1337", "localhost", "3306", self.name)
        self.setupUi()
        self.sync_button.clicked.connect(self.sync_db)

    def setupUi(self):
        self.setWindowTitle(f"{self.name.upper()} Admin Dashboard")

        self.stacked_widget = QStackedWidget()
        self.insert_page = InsertWidget(self.db, self.name, self.logs_path)
        self.update_page = UpdateWidget(self.db, self.name, self.logs_path)
        self.delete_page = DeleteWidget(self.db, self.name, self.logs_path)
        self.stacked_widget.addWidget(self.insert_page)
        self.stacked_widget.addWidget(self.update_page)
        self.stacked_widget.addWidget(self.delete_page)

        self.insert_button = QPushButton("Insert")
        self.update_button = QPushButton("Update")
        self.delete_button = QPushButton("Delete")
        self.sync_button = QPushButton("Sync")

        navbar_layout = QHBoxLayout()
        navbar_layout.addWidget(self.insert_button)
        navbar_layout.addWidget(self.update_button)
        navbar_layout.addWidget(self.delete_button)

        main_layout = QVBoxLayout()
        main_layout.addLayout(navbar_layout)
        main_layout.addWidget(self.sync_button)
        main_layout.addWidget(self.stacked_widget)
        main_widget = QWidget()
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

        self.insert_button.clicked.connect(
            lambda: self.stacked_widget.setCurrentIndex(
                self.stacked_widget.indexOf(self.insert_page)
            )
        )
        self.update_button.clicked.connect(
            lambda: self.stacked_widget.setCurrentIndex(
                self.stacked_widget.indexOf(self.update_page)
            )
        )
        self.delete_button.clicked.connect(
            lambda: self.stacked_widget.setCurrentIndex(
                self.stacked_widget.indexOf(self.delete_page)
            )
        )

    def sync_db(self):
        with open(self.logs_path, "r") as file:
            logs = json.load(file)
        try:
            with pika.BlockingConnection(
                pika.ConnectionParameters("localhost")
            ) as connection:
                channel = connection.channel()
                channel.queue_declare(queue=self.name, durable=True)

                channel.basic_publish(
                    exchange="",
                    routing_key=self.name,
                    body=jsonpickle.encode(logs),
                    properties=pika.BasicProperties(delivery_mode=2),
                )
                channel.close()
                with open(self.logs_path, "w") as file:
                    json.dump([], file)
        except Exception:
            self.show_message_box()

    def show_message_box(self):
        message_box = QMessageBox(self)
        message_box.setWindowTitle("Critical Information")
        message_box.setText(
            "Failed to send information to the HO server! Please try again later"
        )
        message_box.setIcon(QMessageBox.Critical)
        message_box.setStandardButtons(QMessageBox.Ok)
        message_box.exec()
