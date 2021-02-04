from app.database.db_builder import db_builder as db
from app.functions import connect
from app.functions import clear


@connect
def show_menu(product, substitute):
    print("Menu :", "\n")
    print("[s] : Enregistrer le substitut dans la base de données.")
    choice = input("> ")

    if choice == "s":
        db.execute(f"INSERT IGNORE INTO Substitute(product_id, substitute_id) VALUES({product[0]}, {substitute[0]})")
        db.commit()

@connect
def get_substitutes(category_id, product_to_substitute):
    clear()

    substitutes = []

    db.execute(f"SELECT * FROM Product WHERE id = {product_to_substitute}")
    product_to_substitute = db.fetch()

    db.execute(f"SELECT * FROM Product_per_category WHERE category_id = {category_id}")
    products_list = db.fetch(True)

    for product in products_list:
        db.execute(f"SELECT * FROM Product WHERE id = {product[2]} and nutriscore_id < {product_to_substitute[3]}")
        product_info = db.fetch()

        if product_info is not None:
            substitutes.append(product_info)

    best_substitute = product_to_substitute
    for substitute in substitutes:
        if substitute[3] < best_substitute[3]:
            best_substitute = substitute

    clear()
    show_product(product_to_substitute, False)
    show_product(best_substitute, True)
    show_menu(product_to_substitute, best_substitute)

@connect
def show_product(product, is_substitute=False):
    if is_substitute:
        title = "Meilleur substitut trouvé :"
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