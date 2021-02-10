from app.database.db_builder import db_builder as db
from app.functions import connect, clear, get_nutriscore_id


class Substitutes():

    @connect
    def __init__(self, product_id):
        self.product_id = product_id
        self.nutriscore_id = get_nutriscore_id(product_id)
        self.concordance = 0

        self.get_targeted_category()

    def get_targeted_category(self):
        db.execute("""
            SELECT Category.id,
            (
                SELECT COUNT(Product_per_category.product_id)
                FROM Category AS category_duplicate
                INNER JOIN Product_per_category
                ON Product_per_category.category_id = category_duplicate.id
                WHERE Category.id = category_duplicate.id
            ) AS products_count
            FROM Product
            INNER JOIN Product_per_category
            ON Product.id = Product_per_category.product_id
            INNER JOIN Category
            ON Category.id = Product_per_category.category_id
            WHERE Product.id = %s
            ORDER BY products_count
        """, (self.product_id,))
        targeted_category = db.fetch(True)[self.concordance][0]

        self.get_substitute(targeted_category)

    def get_substitute(self, category_id):
        db.execute("""
            SELECT product_id, nutriscore_id
            FROM Product_per_category
            INNER JOIN Product
            ON Product.id = product_id
            WHERE category_id = %s AND nutriscore_id < %s
            ORDER BY nutriscore_id
        """, (category_id, self.nutriscore_id,))
        products_list = db.fetch(True)
        breakpoint()





        db.execute("SELECT * FROM Product_per_category WHERE category_id = %s", (targeted_category,))
        products_list = db.fetch(True)

        for product in products_list:
            db.execute(f"SELECT * FROM Product WHERE id = {product[2]} and nutriscore_id < {product_id[3]}")
            product_info = db.fetch()

            if product_info is not None:
                substitutes.append(product_info)

        best_substitute = product_to_substitute
        for substitute in substitutes:
            if substitute[3] < best_substitute[3]:
                best_substitute = substitute

        clear()
        show_product(product_to_substitute, False)
        if product_to_substitute != best_substitute:
            show_product(best_substitute, True)
            show_menu(product_to_substitute, best_substitute)
        else:
            print("\nAucun substitut trouvé.")

    @connect
    def show_product(product, is_substitute=False):
        if is_substitute:
            title = "Substitut trouvé :"
        else:
            title = "Produit sélectionné :"

        db.execute(f"SELECT score FROM Nutriscore WHERE id = {product[3]}")
        nutriscore = db.fetch()

        print("\n")
        print(title, "\n")
        print("Nom: ", product[1])
        print("Marque: ", product[2])
        print("Nutriscore: ", nutriscore)
        print("Magasins: ", product[4])
        print("Description: ", product[5])
        print("URL: ", product[6])

    @connect
    def get_saved_substitutes():
        products = []

        db.execute(f"SELECT * FROM Substitute")
        items_list = db.fetch(True)

        for item in items_list:
            db.execute(f"SELECT * FROM Product WHERE id = {item[1]}")
            product_info = db.fetch()
            products.append(product_info)

        print("Sélectionnez l'aliment substitué :")
        for product in products:
            print(product[0], "-", product[1], f"({product[2]})")
        choice = input("> ")

        products_id = [product_id for (pk, product_id, substitute_id) in items_list]
        if int(choice) in products_id:
            clear()

            db.execute(f"SELECT * FROM Substitute WHERE product_id = {int(choice)}")
            product_info = db.fetch()
            db.execute(f"SELECT * FROM Product WHERE id = {product_info[1]}")
            product = db.fetch()
            db.execute(f"SELECT * FROM Product WHERE id = {product_info[2]}")
            substitute = db.fetch()

            show_product(product, False)
            show_product(substitute, True)
        else:
            get_saved_substitutes()

    @connect
    def show_menu(product, substitute):
        print("Menu :", "\n")
        print("[s] : Enregistrer le substitut dans la base de données.")
        choice = input("> ")

        if choice == "s":
            db.execute(f"INSERT IGNORE INTO Substitute(product_id, substitute_id) VALUES({product[0]}, {substitute[0]})")
            db.commit()
            