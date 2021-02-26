from app.database.db_builder import db_builder as db
from app.helpers import connect


class Substitute:

    def __init__(self):
        self.products_list = None
        self.products_id_list = None

        self.product = None
        self.substitute = None

    @connect
    def get_saved_substitutes(self):
        self.products_list = []

        db.execute(f"SELECT * FROM Substitute")
        products_list = db.fetch(True)
        self.products_id_list = [product_id for (pk, product_id, substitute_id) in products_list]

        for product in products_list:
            product_id = product[1]
            substitute_id = product[2]

            db.execute("SELECT * FROM Product WHERE id = %s", (product_id,))
            product_info = db.fetch()

            db.execute("SELECT * FROM Product WHERE id = %s", (substitute_id,))
            substitute_info = db.fetch()

            self.products_list.append((product_info, substitute_info))

    @connect
    def select(self, product_id):
        db.execute("SELECT * FROM Substitute WHERE product_id = %s", (product_id))
        product = db.fetch()
        self.product = product[1]
        self.substitute = product[2]