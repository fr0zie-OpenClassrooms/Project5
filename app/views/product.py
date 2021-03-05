from app.models.product import Product

from app.helpers import clear


class ProductView():

    def __init__(self):
        """Class initialization."""

        self.model = Product()

    def display(self):
        """Method used to display page in terminal."""

        self.model.get_page()
        clear()

        print("Sélectionnez le produit:\n")
        for product in self.model.products_list:
            print(product.id, "-", product.name)

        self.footer()

    def footer(self):
        """Method used to display page footer."""

        print(f"\nPage {self.model.page}/{self.model.max_pages}")
        print(f"[p-1 à p-{self.model.max_pages}] Aller à la page")
        print("[n] Page suivante")
        print("[b] Page précédente")
        print("[1-9999] Sélectionner le produit")
        print("[q] Quitter l'application")
