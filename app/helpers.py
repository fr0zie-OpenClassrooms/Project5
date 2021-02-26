import os

from app.database.db_builder import db_builder as db


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
