import json

import app.database.get_data as data
from app.database.db_builder import db_builder as db


def connect(func):
    def wrapper():
        try:
            db.connect()
        except:
            db.connect("root")

        func()
        db.disconnect()
    return wrapper

@connect
def create_db():
    """Create the database."""
    try:
        db.connect()
    except:
        db.execute("DROP TABLE IF EXISTS purbeurre")
        db.execute("CREATE DATABASE purbeurre")
        print("Database has been created.")

        create_tables()

@connect
def create_tables():
    """Create tables in database."""
    with open("app/database/tables.sql", mode="r") as file:
        sql = file.read()

    db.execute(sql, multi=True)
    print("Tables have been added to database.")

    data.get_data()
