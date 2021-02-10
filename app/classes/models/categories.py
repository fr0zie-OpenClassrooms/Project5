from app.classes.models.products import Products
from app.database.db_builder import db_builder as db
from app.functions import connect, clear


class Categories():

    @connect
    def __init__(self):
        db.execute("SELECT COUNT(*) FROM Category")
        self.max_categories = db.fetch()[0]
        self.page = 1
        self.page_size = 20
        self.limit = self.page_size * self.page
        self.max_pages = self.max_categories // self.page_size

        self.categories_id = []

    @connect
    def menu(self, page=1):
        categories = []

        db.execute("SELECT * FROM Category LIMIT %s,%s", (self.limit, self.page_size))
        categories_list = db.fetch(True)
        self.categories_id = [pk for (pk, name) in categories_list]

        for category in categories_list:
            categories.append((category[0], category[1]))

        print("Sélectionnez la catégorie:\n")
        for category in categories:
            print(category[0], "-", category[1])

        self.footer()

    def footer(self):
        print(f"\nPage {self.page}/{self.max_pages}")
        print(f"[n] Page suivante / [b] Page précédente / [p0-p{self.max_pages}] Aller à la page")
        print("[1-9999] Sélectionner la catégorie")
        choice = input("> ")

        if choice.isdigit():
            if int(choice) in self.categories_id:
                Products().display_menu(choice)
        else:
            if choice == "n":
                if self.page < self.max_pages:
                    self.page += 1
            elif choice == "b":
                if self.page > 1:
                    self.page -= 1
            # Autre méthode?
            else:
                page = str
                for char in choice:
                    if char.isdigit():
                        page += char
                self.page = int(choice)
                   
        self.limit = self.page_size * self.page
        self.menu(self.limit)

        