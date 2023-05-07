from sqlalchemy import DECIMAL, Column, Date, Integer, MetaData, String, Table


def get_product_sales(metadata: MetaData):
    return Table(
        "product_sales",
        metadata,
        Column("id", Integer, primary_key=True),
        Column("date", Date()),
        Column("region", String(255)),
        Column("product", String(255)),
        Column("qty", Integer()),
        Column("cost", DECIMAL()),
        Column("amt", DECIMAL()),
        Column("tax", DECIMAL()),
        Column("total", DECIMAL()),
    )
