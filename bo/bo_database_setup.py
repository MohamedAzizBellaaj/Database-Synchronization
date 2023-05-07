from sqlalchemy import DECIMAL, Column, Date, Integer, String, create_engine
from sqlalchemy.orm import declarative_base

from db_connection import Database

Base = declarative_base()


class ProductSales(Base):
    __tablename__ = "product_sales"
    id = Column(Integer, primary_key=True)
    date = Column(Date)
    region = Column(String(255))
    product = Column(String(255))
    qty = Column(Integer)
    cost = Column(DECIMAL)
    amt = Column(DECIMAL)
    tax = Column(DECIMAL)
    total = Column(DECIMAL)


for database in ["bo1", "bo2"]:
    user = "root"
    password = "1337"
    host = "localhost"
    port = "3306"

    engine = create_engine(f"mysql://{user}:{password}@{host}:{port}/{database}")

    Base.metadata.create_all(engine)
