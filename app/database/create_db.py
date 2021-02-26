import json

import app.database.get_data as data
from app.database.db_builder import db_builder as db
from app.helpers import connect


@connect
def create_db():
    """Create the database."""
    print("Creating database... This might take a few minutes.")

    try:
        db.execute("CREATE DATABASE purbeurre")
        print("Database has been created.")
        create_tables()
    except:
        print("Database already exists.")

@connect
def recreate_db():
    choice = input("Confirmez-vous la réinitialisation de la base de données? (Y/N): ").lower()

    if choice == "y":
        db.execute("DROP DATABASE IF EXISTS purbeurre")
        create_db()

@connect
def create_tables():
    """Create tables in database."""
    with open("app/database/tables.sql", mode="r", encoding="utf-8") as file:
        sql = file.read()
        requests = sql.split(";")

        for line in requests:
            db.execute(line)
    
    print("Tables have been added to database.")

    data.get_data()
