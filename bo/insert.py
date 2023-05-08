from datetime import date

import jsonpickle
from PySide6.QtWidgets import QWidget
from sqlalchemy.orm import sessionmaker

from bo.ui.insert_ui import Ui_InsertWidget
from bo_setup import ProductSales
from utils.write_json import write_json


class InsertWidget(QWidget, Ui_InsertWidget):
    def __init__(self, db, name, logs_path):
        super().__init__()
        self.setupUi(self)
        self.db = db
        self.name = name
        self.logs_path = logs_path
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

        session.close()

        payload = {
            "type": "INSERT",
            "record_data": record_data,
        }

        write_json(jsonpickle.encode(payload), self.logs_path)
