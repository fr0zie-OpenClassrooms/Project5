import os
from getpass import getpass
from dotenv import load_dotenv

from app.database.db_builder import db_builder as db


def create_env():
    """Creates MySQL user."""
    user = ""
    pwd = ""

    if not os.path.exists(".env"):
        while len(user) < 1:
            user = input("Entrez votre nom d'utilisateur MySQL (défaut: root): ")
            user = "root" if not user else user

        pwd = getpass(prompt="Entrez votre mot de passe (défaut: ): ")

        with open(".env", "w") as file:
            file.write(f"DB_USER={user}\nDB_PASSWORD={pwd}")

        load_dotenv()


def connect(func):
    def wrapper(*args, **kwargs):
        try:
            db.connect()
        except:
            db.connect("root")

        result = func(*args, **kwargs)
        db.disconnect()
        return result
    return wrapper


def clear():
    os.system('cls')
