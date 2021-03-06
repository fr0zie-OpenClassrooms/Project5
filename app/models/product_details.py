from app.database.db_builder import db_builder as db
from app.helpers import connect


class ProductDetails:
    """Product details class builder."""

    def __init__(self, product_id=None):
        """Class initialization."""

        self.id = product_id
        self.name = None
        self.brand = None
        self.nutriscore = None
        self.store = None
        self.description = None
        self.url = None

        self.category_id = None
        self.category_concordance = 0

        self.product = None
        self.substitute = None

        if product_id:
            self.get_nutriscore()
            self.get_product_details()

    @connect
    def get_nutriscore(self):
        """Method getting product's nutriscore ID."""

        db.execute("SELECT nutriscore_id FROM Product WHERE id = %s",
                   (self.id,))
        self.nutriscore = db.fetch()[0]

    @connect
    def get_product_details(self):
        """Method getting all product details."""

        db.execute("SELECT * FROM Product WHERE id = %s", (self.id,))
        product = db.fetch()

        self.name = product[1]
        self.brand = product[2]
        self.nutriscore_id = product[3]
        self.store = product[4]
        self.description = product[5]
        self.url = product[6]

    @connect
    def get_targeted_category(self):
        """Method getting the most targeted category of a product."""

        db.execute("""
            SELECT Category.id,
            (
                SELECT COUNT(Product_per_category.product_id)
                FROM Category AS category_duplicate
                INNER JOIN Product_per_category
                ON Product_per_category.category_id = category_duplicate.id
                WHERE Category.id = category_duplicate.id
            ) AS products_count
            FROM Product
            INNER JOIN Product_per_category
            ON Product.id = Product_per_category.product_id
            INNER JOIN Category
            ON Category.id = Product_per_category.category_id
            WHERE Product.id = %s
            ORDER BY products_count
        """, (self.id,))
        try:
            self.category_id = db.fetch(True)[self.category_concordance][0]
        except IndexError:
            return

    @connect
    def find_substitute(self):
        """Method used to find the healthiest substitute according to the targeted category."""

        products_list = None

        while not products_list:
            self.get_targeted_category()

            db.connect()
            db.execute("""
                SELECT product_id, nutriscore_id
                FROM Product_per_category
                INNER JOIN Product
                ON Product.id = product_id
                WHERE category_id = %s AND nutriscore_id < %s
                ORDER BY nutriscore_id
            """, (self.category_id, self.nutriscore,))
            products_list = db.fetch(True)
            db.disconnect()
            self.category_concordance += 1

        return products_list[0][0]

    @connect
    def save(self):
        """Method used to save the found substitute in database."""

        db.execute("INSERT IGNORE INTO Substitute(product_id, substitute_id) VALUES(%s, %s)",
                   (self.product.id, self.substitute.id,))
        db.commit()
        print("Substitut sauvegardé dans la base de données.")

    @connect
    def is_product_saved(self):
        """Method that checks if product is already in database."""

        db.execute("SELECT product_id FROM Substitute WHERE product_id = %s",
                   (self.product.id,))
        product = db.fetch()
        if product:
            return True
        else:
            return False