from app.views.product import ProductView
from app.models.product_details import ProductDetails


class ProductController:
    """Class defining product controllers."""

    def __init__(self, category_id):
        """Class initialization."""

        self.view = ProductView()
        self.model = self.view.model

        self.model.category_id = category_id
        self.model.get_max_pages()
        self.model.get_products_id()

        self.product = None
        self.substitute = None

    def display(self):
        """Method displaying page."""

        self.view.display()

    def get_command(self):
        """Method getting user input."""

        choice = input("> ")

        if choice.startswith("p-"):
            choice = int(choice.replace("p-", ""))
            if choice <= self.model.max_pages and choice > 0:
                self.model.page = choice
        elif choice == "n":
            if self.model.page < self.model.max_pages:
                self.model.page += 1
        elif choice == "b":
            if self.model.page > 1:
                self.model.page -= 1
        elif choice == "q":
            return "quit"
        elif choice.isdigit():
            self.product = ProductDetails(choice)
            substitute = self.product.find_substitute()
            self.substitute = ProductDetails(substitute)
            return "goto-product-details"

        self.model.limit = self.model.page_size * (self.model.page - 1)
