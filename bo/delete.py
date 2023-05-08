import jsonpickle
from PySide6.QtWidgets import QWidget
from sqlalchemy import MetaData, Table, text

from bo.ui.delete_ui import Ui_Delete
from utils.write_json import write_json


class DeleteWidget(QWidget, Ui_Delete):
    def __init__(self, db, name, logs_path):
        super().__init__()
        self.setupUi(self)
        self.db = db
        self.name = name
        self.logs_path = logs_path
        self.delete_button.clicked.connect(self.delete_db)

    def delete_db(self):
        metadata = MetaData()
        metadata.reflect(bind=self.db.engine)

        product_sales_table = Table("product_sales", metadata, autoload=True)

        delete_query = product_sales_table.delete().where(
            text(self.where_clause_line_edit.text())
        )

        with self.db.engine.connect() as connection:
            connection.execute(delete_query)
            connection.commit()

        payload = {
            "type": "DELETE",
            "origin": self.name,
            "where_clause": self.where_clause_line_edit.text(),
        }

        write_json(jsonpickle.encode(payload), self.logs_path)
