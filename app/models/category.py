from app.database.db_builder import db_builder as db
from app.helpers import connect


class Category:
    """Category class builder."""

    def __init__(self):
        """Class initialization."""

        self.page = 1
        self.page_size = 20
        self.max_pages = None
        self.limit = self.page_size * (self.page - 1)
        self.categories_list = None
        self.categories_id_list = None

        self.get_max_pages()
        self.get_categories_id()

    @connect
    def get_categories_id(self):
        """Method returning all IDs from 'Category' table."""

        db.execute("SELECT * FROM Category")
        categories_list = db.fetch(True)
        self.categories_id_list = [pk for (pk, name) in categories_list]

    @connect
    def get_max_pages(self):
        """Method returning count of all categories from 'Category' table."""

        db.execute("SELECT COUNT(*) FROM Category")
        max_categories = db.fetch()[0]

        if max_categories % self.page_size == 0:
            self.max_pages = max_categories // self.page_size
        else:
            self.max_pages = (max_categories // self.page_size) + 1

    @connect
    def get_page(self):
        """Method adding categories current page to list."""

        self.categories_list = []

        db.execute("SELECT * FROM Category LIMIT %s,%s", (self.limit, self.page_size))
        categories_list = db.fetch(True)

        for category in categories_list:
            self.categories_list.append(category)
