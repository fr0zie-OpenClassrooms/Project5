from app.views.product_details import ProductDetailsView


class ProductDetailsController:
    """Class defining product controllers."""

    def __init__(self, product, substitute):
        """Class initialization."""
        self.view = ProductDetailsView()
        self.model = self.view.model

        self.model.product = product
        self.model.substitute = substitute

    def display(self):
        """Method displaying page."""
        self.view.display()

    def get_command(self):
        """Method getting user input."""
        choice = input("> ")

        if choice == "s":
            self.model.save()
            return "goto-menu"
