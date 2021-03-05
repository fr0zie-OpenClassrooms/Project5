from app.models.category import Category

from app.helpers import clear


class CategoryView():

    def __init__(self):
        """Class initialization."""
        self.model = Category()

    def display(self):
        self.model.get_page()
        clear()

        print("Sélectionnez la catégorie:\n")
        for category in self.model.categories_list:
            print(category[0], "-", category[1])

        self.footer()

    def footer(self):
        print(f"\nPage {self.model.page}/{self.model.max_pages}")
        print(f"[p-1 à p-{self.model.max_pages}] Aller à la page")
        print("[n] Page suivante")
        print("[b] Page précédente")
        print("[1-9999] Sélectionner la catégorie")
        print("[q] Quitter l'application")
