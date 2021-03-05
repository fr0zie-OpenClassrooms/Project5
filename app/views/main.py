from app.helpers import clear


class MainView:

    def __init__(self):
        pass

    def display(self):
        """Method used to display page in terminal."""

        clear()
        print("Bienvenue dans le programme Pur Beurre !\n")
        print("[1] Chercher un aliment")
        print("[2] Retrouver mes aliments substitués")
        print("[3] Réinitialiser la base de données")
        print("[4] Quitter l'application")
