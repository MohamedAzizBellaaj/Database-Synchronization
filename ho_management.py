import os
import sys

import jsonpickle
import pika
from sqlalchemy import MetaData, Table, text
from sqlalchemy.orm import sessionmaker

from ho_setup import ProductSalesHO
from utils.db_connection import Database


def callback(ch, method, properties, body):
    db = Database.get_instance("root", "1337", "localhost", "3306", "ho")
    thawed = jsonpickle.decode(body)
    Session = sessionmaker(bind=db.engine)
    metadata = MetaData()
    metadata.reflect(bind=db.engine)
    session = Session()
    with db.engine.connect() as connection:
        for query in thawed:
            query = jsonpickle.decode(query)
            match query["type"]:
                case "INSERT":
                    new_record = ProductSalesHO(**query["record_data"])
                    session.add(new_record)
                    session.commit()
                case "UPDATE":
                    product_sales_ho_table = Table(
                        "product_sales_ho", metadata, autoload=True
                    )
                    updated_where_clause = query["where_clause"].replace(
                        "id", "origin_id"
                    )
                    updated_where_clause = (
                        f"{updated_where_clause} and origin = '{query['origin']}'"
                    )
                    update_query = (
                        product_sales_ho_table.update()
                        .where(text(updated_where_clause))
                        .values(**query["update_record"])
                    )
                    connection.execute(update_query)
                    connection.commit()
                case "DELETE":
                    product_sales_ho_table = Table(
                        "product_sales_ho", metadata, autoload=True
                    )
                    updated_where_clause = query["where_clause"].replace(
                        "id", "origin_id"
                    )
                    updated_where_clause = (
                        f"{updated_where_clause} and origin = '{query['origin']}'"
                    )
                    delete_query = product_sales_ho_table.delete().where(
                        text(updated_where_clause)
                    )
                    connection.execute(delete_query)
                    connection.commit()
    session.close()


def main():
    with pika.BlockingConnection(
        pika.ConnectionParameters(host="localhost")
    ) as connection:
        channel = connection.channel()
        channel.queue_declare(queue="bo1", durable=True)
        channel.queue_declare(queue="bo2", durable=True)
        channel.basic_consume(queue="bo1", on_message_callback=callback, auto_ack=True)
        channel.basic_consume(queue="bo2", on_message_callback=callback, auto_ack=True)
        channel.start_consuming()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
            raise
