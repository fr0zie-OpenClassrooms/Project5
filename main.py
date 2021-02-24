from app.application import Application
from app.functions import clear

import app.database.create_db as db


def main():
    """Launch program."""
    app = Application()
    app.run()


if __name__ == "__main__":
    main()
