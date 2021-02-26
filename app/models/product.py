from app.models.product_details import ProductDetails

from app.database.db_builder import db_builder as db
from app.functions import connect


class Product:
    """"""

    def __init__(self):
        """Class initialization."""
        self.page = 1
        self.page_size = 20
        self.max_pages = None
        self.limit = self.page_size * self.page - 1
        self.products_list = None
        self.products_id_list = None
        self.product_id = None
        self.category_id = None

        self.product = None
        self.substitute = None

        self.get_max_pages()
        self.get_products_id()

    @connect
    def get_products_id(self):
        """Function returning all IDs matching 'category_id' from 'Product_per_category' table."""

        db.execute("SELECT * FROM Product_per_category WHERE category_id = %s", (self.category_id,))
        products_list = db.fetch(True)
        self.products_id_list = [product_id for (pk, category_id, product_id) in products_list]

    @connect
    def get_max_pages(self):
        """Function returning the count of all categories matching 'category_id' from 'Product_per_category' table."""

        db.execute("SELECT COUNT(*) FROM Product_per_category WHERE category_id = %s", (self.category_id,))
        max_products = db.fetch()[0]
        self.max_pages = max_products // self.page_size

    @connect
    def get_page(self):
        self.products_list = []

        db.execute("SELECT product_id FROM Product_per_category WHERE category_id = %s LIMIT %s,%s", (self.category_id, self.limit, self.page_size,))
        products_list = db.fetch(True)

        for product in products_list:
            product = ProductDetails(product[0])
            self.products_list.append(product)
