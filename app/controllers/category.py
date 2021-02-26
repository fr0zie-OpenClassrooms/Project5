from app.views.category import CategoryView


class CategoryController():

    def __init__(self):
        """Class initialization."""
        self.view = CategoryView()
        self.model = self.view.model

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
        elif choice.isdigit():
            self.model.category_id = choice
            return "goto-product"
                
        self.model.limit = self.model.page_size * self.model.page - 1