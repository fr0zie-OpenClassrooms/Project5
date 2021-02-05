import app.classes.models.substitutes as substitutes
from app.database.db_builder import db_builder as db
from app.functions import connect
from app.functions import clear


@connect
def get_products(category_id):
    clear()

    products = []

    db.execute(f"SELECT * FROM Product_per_category WHERE category_id = '{category_id}'")
    products_list = db.fetch(True)

    for product in products_list:
        db.execute(f"SELECT * FROM Product WHERE id = '{product[2]}'")
        product_info = db.fetch()
        products.append(product_info)

    print("Sélectionnez le produit :")
    for product in products:
        print(product[0], "-", product[1], f"({product[2]})")
    choice = input("> ")

    products_id = [product_id for (pk, category_id, product_id) in products_list]
    if int(choice) in products_id:
        substitutes.get_substitutes(category_id, choice)
    else:
        get_products(category_id)