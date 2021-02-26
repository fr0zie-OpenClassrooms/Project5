from app.views.substitute import SubstituteView
from app.models.product_details import ProductDetails



class SubstituteController:
    """Class defining substitute controllers."""

    def __init__(self):
        """Class initialization."""

        self.view = SubstituteView()
        self.model = self.view.model

    def display(self):
        """Method displaying page."""
        self.view.display()

    def get_command(self):
        """Method getting user input."""
        choice = input("> ")

        if int(choice) in self.model.products_id_list:
            product = ProductDetails(choice)