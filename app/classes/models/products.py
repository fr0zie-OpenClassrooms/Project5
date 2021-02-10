from app.classes.models.substitutes import Substitutes
from app.database.db_builder import db_builder as db
from app.functions import connect, clear


class Products():

    @connect
    def __init__(self):
        self.products_id = []

    @connect
    def display_menu(self, category_id):
        clear()

        products = []

        db.execute("SELECT * FROM Product_per_category WHERE category_id = %s", (category_id,))
        products_list = db.fetch(True)
        products_id = [product_id for (pk, category_id, product_id) in products_list]

        for product in products_list:
            db.execute(f"SELECT * FROM Product WHERE id = '{product[2]}'")
            product_info = db.fetch()
            products.append(product_info)

        print("Sélectionnez le produit :")
        for product in products:
            print(product[0], "-", product[1], f"({product[2]})")
        choice = input("> ")

        
        if int(choice) in products_id:
            Substitutes(choice)
        else:
            self.display_menu(category_id)