from PySide6.QtWidgets import (
    QHBoxLayout,
    QMainWindow,
    QPushButton,
    QStackedWidget,
    QVBoxLayout,
    QWidget,
)

from db_connection import Database
from bo.insert import InsertWidget


class MainWindow(QMainWindow):
    def __init__(self, name: str):
        super().__init__()
        self.name = name
        self.db = Database("root", "1337", "localhost", "3306", self.name)
        self.setupUi()

    def setupUi(self):
        self.setWindowTitle(f"{self.name.upper()} Admin Dashboard")

        self.stacked_widget = QStackedWidget()
        self.insert_page = InsertWidget(self.db, self.name)
        self.update_page = QWidget()
        self.delete_page = QWidget()
        self.stacked_widget.addWidget(self.insert_page)
        self.stacked_widget.addWidget(self.update_page)
        self.stacked_widget.addWidget(self.delete_page)

        self.insert_button = QPushButton("Insert")
        self.update_button = QPushButton("Update")
        self.delete_button = QPushButton("Delete")

        navbar_layout = QHBoxLayout()
        navbar_layout.addWidget(self.insert_button)
        navbar_layout.addWidget(self.update_button)
        navbar_layout.addWidget(self.delete_button)

        main_layout = QVBoxLayout()
        main_layout.addLayout(navbar_layout)
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
