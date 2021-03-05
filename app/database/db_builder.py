import os
from dotenv import load_dotenv

import mysql
import mysql.connector


class Database:
    """Database class builder."""

    def __init__(self):
        """Class initialization."""

        load_dotenv()

        self.connection = None
        self.cursor = None

    def connect(self, database="purbeurre"):
        """Method used to connect to database."""

        if database == "root":
            database = ""
        host = "localhost"
        user = os.getenv("DB_USER")
        password = os.getenv("DB_PASSWORD")

        self.connection = mysql.connector.connect(
            database=database,
            host=host,
            user=user,
            password=password
        )

        self.cursor = self.connection.cursor()

    def disconnect(self):
        """Method used to disconnect from database."""

        self.cursor.close()
        self.connection.close()

    def execute(self, request, params=None, multi=False):
        """Method used to execute a request."""

        result = self.cursor.execute(request, params, multi)
        if multi:
            return result

    def fetch(self, all=False):
        """Method used to return database request result."""

        if all:
            return self.cursor.fetchall()
        else:
            return self.cursor.fetchone()

    def lastrowid(self):
        """Method used to return database last inserted row."""

        return self.cursor.lastrowid()

    def commit(self):
        """Method used to commit database last request."""

        return self.connection.commit()


db_builder = Database()
