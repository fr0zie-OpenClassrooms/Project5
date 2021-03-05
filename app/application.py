from app.controllers.main import MainController
from app.controllers.category import CategoryController
from app.controllers.product import ProductController
from app.controllers.product_details import ProductDetailsController
from app.controllers.substitute import SubstituteController

from app.database import create_db as db
from app.helpers import create_env


class Application:
    """"""

    def __init__(self):
        """Class initialization."""

        create_env()
        db.create_db()

        self.controller = MainController()
        self.is_running = True

    def run(self):
        """Method used to loop application."""

        while self.is_running:
            self.controller.display()
            command = self.controller.get_command()
            self.update(command)

        print("Merci d'avoir utilisé le programme Pur Beurre!")

    def update(self, command):
        """Method used to update application and controller."""

        if command == "":
            return
        elif command == "quit":
            self.is_running = False
        elif command == "goto-menu":
            self.controller = MainController()
        elif command == "goto-category":
            self.controller = CategoryController()
        elif command == "goto-product":
            self.controller = ProductController(self.controller.category_id)
        elif command == "goto-product-details":
            self.controller = ProductDetailsController(self.controller.product, self.controller.substitute)
        elif command == "goto-substitute":
            self.controller = SubstituteController()
        elif command == "rebuild-database":
            db.recreate_db()
            return
