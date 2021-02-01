from app.database.db_builder import db_builder as db


def connect(func):
    def wrapper():
        db.connect()
        func()
        db.disconnect()
    return wrapper

@connect
def get_products(id):
    products = []

    db.execute(f"SELECT * FROM Product_per_category WHERE category_id = '{id}'")
    products_list = db.fetch(True)

    for product in products_list:
        products.append((product[0], product[1]))

    print("Sélectionnez le produit :")
    for row in products:
        print(row[0], "-", row[1])
    choice = input("> ")