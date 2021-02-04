import app.classes.models.products as products
from app.database.db_builder import db_builder as db
from app.functions import connect
from app.functions import clear


@connect
def get_categories():
    clear()
    
    categories = []

    db.execute("SELECT * FROM Category")
    categories_list = db.fetch(True)

    for category in categories_list:
        categories.append((category[0], category[1]))

    print("Sélectionnez la catégorie :")
    for row in categories:
        print(row[0], "-", row[1])
    choice = input("> ")

    categories_id = [pk for (pk, name) in categories_list]
    if int(choice) in categories_id:
        products.get_products(choice)