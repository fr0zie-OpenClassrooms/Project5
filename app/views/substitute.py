from app.models.substitute import Substitute

from app.helpers import clear


class SubstituteView():

    def __init__(self):
        self.model = Substitute()

    def display(self):
        self.model.get_saved_substitutes()
        clear()

        print("Sélectionnez le produit:\n")
        for product in self.model.products_list:
            print(product[0][0], "-", product[0][1])

        self.footer()

    def footer(self):
        print("\n[1-9999] Sélectionner le produit")
        print("[q] Quitter l'application")
