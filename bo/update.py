from datetime import date

import jsonpickle
from PySide6.QtWidgets import QWidget
from sqlalchemy import MetaData, Table, text

from bo.ui.update_ui import Ui_Update
from utils.write_json import write_json


class UpdateWidget(QWidget, Ui_Update):
    def __init__(self, db, name, logs_path):
        super().__init__()
        self.setupUi(self)
        self.db = db
        self.name = name
        self.logs_path = logs_path
        self.update_button.clicked.connect(self.update_db)

    def update_db(self):
        metadata = MetaData()
        metadata.reflect(bind=self.db.engine)

        product_sales_table = Table("product_sales", metadata, autoload=True)

        form_data = {
            "date": date.today(),
            "region": self.region_line_edit.text(),
            "product": self.product_line_edit.text(),
            "qty": int(self.qty_line_edit.text())
            if self.qty_line_edit.text() != ""
            else "",
            "cost": float(self.cost_line_edit.text())
            if self.cost_line_edit.text() != ""
            else "",
            "amt": float(self.amt_line_edit.text())
            if self.amt_line_edit.text() != ""
            else "",
            "tax": float(self.tax_line_edit.text())
            if self.tax_line_edit.text() != ""
            else "",
            "total": float(self.total_line_edit.text())
            if self.total_line_edit.text() != ""
            else "",
        }

        update_record = {key: value for key, value in form_data.items() if value != ""}

        update_query = (
            product_sales_table.update()
            .where(text(self.where_clause_line_edit.text()))
            .values(**update_record)
        )

        with self.db.engine.connect() as connection:
            connection.execute(update_query)
            connection.commit()

        payload = {
            "type": "UPDATE",
            "origin": self.name,
            "update_record": update_record,
            "where_clause": self.where_clause_line_edit.text(),
        }

        write_json(jsonpickle.encode(payload), self.logs_path)
