import requests

from app.database.db_builder import db_builder as db
from app.functions import connect


def get_data():
    """Get a product list from URL."""

    params = {
        "action": "process",
        "tagtype_0": "categories",
        "tagtype_1": "countries",
        "tag_contains_1": "france",
        "page_size": 10000,
        "json": 1
    }
    products_url = requests.get("https://fr.openfoodfacts.org/cgi/search.pl", params=params)
    products = products_url.json()["products"]

    for product in products:
        create_product(product)

    print("Data has been added to database.")

@connect
def create_product(product):
    """Insert the product in 'Product' database table."""
    # Get product name
    name = product.get("product_name", "").replace("'", " ")
    if not name:
        return

    # Get product brand
    brand = product.get("brands", "").replace("'", " ")
    if not brand:
        return

    # Get product nutriscore
    nutriscore = product.get("nutriscore_grade")
    if not nutriscore:
        return

    db.execute("SELECT id FROM Nutriscore WHERE score = %s", (nutriscore,))
    nutriscore_id = db.fetch()[0]

    # Get product store
    store = product.get("stores", "").replace("'", " ")

    # Get product description
    description = product.get("generic_name", "").replace("'", " ")

    # Get product URL
    url = product.get("url", "")
    if not url:
        return

    # Get product categories
    categories = product.get("categories").replace("'", " ").replace("en:", "")
    if not categories or product.get("categories_lc") != "fr":
        return

    # Insert product in database
    db.execute(f"""
        INSERT IGNORE INTO Product(name, brand, nutriscore_id, store, description, url) VALUES(
            '{name}',
            '{brand}',
            '{nutriscore_id}',
            '{store}',
            '{description}',
            '{url}'
        )""")
    db.commit()

    # Get product ID and create category
    db.execute("SELECT LAST_INSERT_ID()")
    product_id = db.fetch()[0]
    for category in categories.split(","):
        create_category(product_id, category)

@connect
def create_category(product_id, category):
    """Insert the category in 'Category' database table."""
    # Insert category in database
    db.execute(f"INSERT IGNORE INTO Category(name) VALUES('{category}')")
    db.commit()

    # Get category ID and create product per category
    db.execute(f"SELECT id FROM Category WHERE name = '{category}'")
    category_id = db.fetch()[0]
    db.execute(f"""INSERT IGNORE INTO Product_per_category(category_id, product_id) VALUES(
            '{category_id}',
            '{product_id}'
        )""")
    db.commit()
