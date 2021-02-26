from app.views.main import MainView


class MainController():

    def __init__(self):
        """Class initialization."""
        self.view = MainView()

    def display(self):
        """Method displaying page."""
        self.view.display()

    def get_command(self):
        """Method getting user input."""
        choice = input("> ")

        if choice == "1":
            return "goto-category"
        elif choice == "2":
            return "goto-substitute"
        elif choice == "3":
            return "rebuild-database"