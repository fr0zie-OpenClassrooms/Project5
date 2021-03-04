# Project 5: Pur Beurre program using OpenFoodFacts API

This Python program interacts with the OpenFoodFacts API in order to find a healthier food substitute according to the desired product.

You can check project details on [Trello](https://www.trello.com/b/OPCfr8Gb/project-5).

## Installation

This project currently supports MySQL.

Installation: [MySQL](https://www.mysql.com).


Create a virtual environment with the [venv](https://docs.python.org/3/tutorial/venv.html) module to install the program:

```bash
python3 -m venv .venv
```

Then, activate the virtual environment:

```bash
.venv/Scripts/activate
```

Install the dependencies using the package manager [pip](https://pip.pypa.io/en/stable/):

```bash
pip install -r requirements.txt
```

Finally, create a `.env` file at the project root, and insert the following:

```bash
DB_USER="user"
DB_PASSWORD="password"
```

Replace values with your MySQL ID and password.

## Usage

### Creating database

When you launch the program for the first time, it will create the `purbeurre` database and add a multitude of products and their details to it. 
This step can take a few minutes.

### Program use

In main menu, you will be able to select either to search a product or to see your saved substitutes.

The first option will ask you to search for a product category.
Then, select a product for which you want to find a substitute.

The program will find the best substitute in a targeted category, and display the product details:
- Name
- Brand
- Nutriscore
- Stores where to buy it
- Description
- OpenFoodFacts link to product

You will then be able to save your found substitute in database.

## License

[MIT](https://www.wikipedia.org/wiki/MIT_License)