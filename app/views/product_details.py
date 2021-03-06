from app.models.product_details import ProductDetails

from app.helpers import clear


class ProductDetailsView():

    def __init__(self):
        """Class initialization."""

        self.model = ProductDetails()

    def display(self):
        """Method used to display page in terminal."""

        clear()
        self.display_product(self.model.product)
        self.display_product(self.model.substitute, True)
        self.footer()

    def display_product(self, product, is_substitute=False):
        """Method used to display a product and its details."""

        if is_substitute:
            print("\nSubstitut trouvé:\n")
        else:
            print("Produit sélectionné:\n")

        print(f"Nom: {product.name}")
        print(f"Marque: {product.brand}")
        print(f"Nutriscore: {product.nutriscore}")
        print(f"Magasin: {product.store}")
        print(f"Description: {product.description}")
        print(f"URL: {product.url}")

    def footer(self):
        """Method used to display page footer."""

        if self.model.is_product_saved():
            print("\n[q] Quitter l'application")
        else:
            print("\n[s] Sauvegarder le substitut")
            print("[q] Quitter l'application")
