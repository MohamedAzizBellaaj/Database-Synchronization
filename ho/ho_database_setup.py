from sqlalchemy import DECIMAL, Column, Date, Integer, String, create_engine
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class ProductSalesHO(Base):
    __tablename__ = "product_sales_ho"
    id = Column(Integer, primary_key=True)
    date = Column(Date)
    region = Column(String(255))
    product = Column(String(255))
    qty = Column(Integer)
    cost = Column(DECIMAL)
    amt = Column(DECIMAL)
    tax = Column(DECIMAL)
    total = Column(DECIMAL)
    origin = Column(String(255))
    origin_id = Column(Integer)


user = "root"
password = "1337"
host = "localhost"
port = "3306"
database = "ho"

engine = create_engine(f"mysql://{user}:{password}@{host}:{port}/{database}")

Base.metadata.create_all(engine)
