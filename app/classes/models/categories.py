import app.classes.models.products as products
from app.database.db_builder import db_builder as db


def connect(func):
    def wrapper():
        db.connect()
        func()
        db.disconnect()
    return wrapper

@connect
def get_categories():
    categories = []

    db.execute("SELECT * FROM Category")
    categories_list = db.fetch(True)

    for category in categories_list:
        categories.append((category[0], category[1]))

    print("Sélectionnez la catégorie :")
    for row in categories:
        print(row[0], "-", row[1])
    choice = input("> ")

    if choice in categories_list:
        products.get_products(choice)