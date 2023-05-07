from datetime import date

import jsonpickle
import pika
from PySide6.QtWidgets import QWidget
from sqlalchemy.orm import sessionmaker

from bo.bo_database_setup import ProductSales
from bo.ui.insert_ui import Ui_InsertWidget


class InsertWidget(QWidget, Ui_InsertWidget):
    def __init__(self, db, name):
        super().__init__()
        self.setupUi(self)
        self.db = db
        self.name = name
        self.insert_button.clicked.connect(self.insert_to_db)

    def insert_to_db(self):
        Session = sessionmaker(bind=self.db.engine)
        session = Session()

        record_data = {
            "date": date.today(),
            "region": self.region_line_edit.text(),
            "product": self.product_line_edit.text(),
            "qty": int(self.qty_line_edit.text()),
            "cost": float(self.cost_line_edit.text()),
            "amt": float(self.amt_line_edit.text()),
            "tax": float(self.tax_line_edit.text()),
            "total": float(self.total_line_edit.text()),
        }

        new_record = ProductSales(**record_data)

        session.add(new_record)
        session.commit()

        record_data.update(
            {
                "origin": self.name,
                "origin_id": new_record.id,
            }
        )

        with pika.BlockingConnection(
            pika.ConnectionParameters("localhost")
        ) as connection:
            channel = connection.channel()
            channel.queue_declare(queue="ho", durable=True)
            payload = {
                "type": "INSERT",
                "record_data": record_data,
            }
            channel.basic_publish(
                exchange="",
                routing_key="ho",
                body=jsonpickle.encode(payload),
                properties=pika.BasicProperties(delivery_mode=2),
            )

        session.close()
