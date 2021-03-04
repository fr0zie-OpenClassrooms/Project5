import os
from getpass import getpass

from app.database.db_builder import db_builder as db


def create_env():
        """Creates MySQL user."""
        user = ""
        pwd = ""

        if not os.path.exists(".env"):
            while len(user) < 1:
                user = input("Entrez votre nom d'utilisateur MySQL (défaut: root): ")
            while len(pwd) < 1:
                pwd = getpass(prompt="Entrez votre mot de passe (défaut: ): ")

            f = open(".env", "x")
            f.write(f"DB_USER=\"{user}\"\nDB_PASSWORD=\"{pwd}\"")
            f.close()

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

clear = lambda: os.system('cls')
