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
        """Database connection."""
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
        """Database disconnection."""
        self.cursor.close()
        self.connection.close()

    def execute(self, request, multi=False):
        """Database request execution."""
        if multi:
            for rows in self.cursor.execute(request, multi=True):
                pass
        else:
            self.cursor.execute(request)

    def fetch(self, all=False):
        """Returns database request result."""
        if all:
            return self.cursor.fetchall()
        else:
            return self.cursor.fetchone()

    def lastrowid(self):
        """Returns database last inserted row."""
        return self.cursor.lastrowid()

    def commit(self):
        """Commit database last request."""
        return self.connection.commit()


db_builder = Database()
