import app.database.create_db as db
from app.application import Application
from app.functions import clear


def main():
    """"""
    db.create_db()
    clear()

    print("Bienvenue dans le programme Pur Beurre !\n")
    print("1: Chercher un aliment")
    print("2: Retrouver mes aliments substitués")
    print("3: Réinitialiser la base de données")
    choices = ["1", "2", "3"]
    choice = input("> ")

    if choice not in choices:
        main()
    else:
        app = Application(choice)
        app.run()


if __name__ == "__main__":
    main()
