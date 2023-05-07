import os
import sys

import jsonpickle
import pika
from sqlalchemy.orm import sessionmaker

from db_connection import Database
from ho.ho_database_setup import ProductSalesHO


def callback(ch, method, properties, body):
    thawed = jsonpickle.decode(body)
    db = Database.get_instance("root", "1337", "localhost", "3306", "ho")
    Session = sessionmaker(bind=db.engine)
    session = Session()
    match thawed["type"]:
        case "INSERT":
            print(thawed["record_data"])
            new_record = ProductSalesHO(**thawed["record_data"])
            session.add(new_record)
        case "UPDATE":
            print("Update...")
        case "DELETE":
            print("Delete...")
        case _:
            print("Unknown command")
    session.commit()
    session.close()


def main():
    with pika.BlockingConnection(
        pika.ConnectionParameters(host="localhost")
    ) as connection:
        channel = connection.channel()
        channel.queue_declare(queue="ho", durable=True)
        channel.basic_consume(queue="ho", on_message_callback=callback, auto_ack=True)
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
