class MenuView:
    def main_menu(self):
        print("\nx=x=x=x=x=x=x MENU PRINCIPAL x=x=x=x=x=x=x\n")
        print("  1. Utilisateurs")
        print("  2. Tournois")
        print("  3. Jouer 1 tour")
        print("  Q. Quitter")

        return input("\n>>> Entrez votre choix : ")

    def user_menu(self):
        print("\nx=x=x=x=x=x=x UTILISATEURS x=x=x=x=x=x=x\n")
        print("  1. Afficher utilisateurs")
        print("  2. Exporter les users dans un fichier JSON")
        print("  3. Importer les users depuis le fichier JSON")
        print("  4. Créer des faux utilisateurs")
        print("  5. Créer un nouveau utilisateur")
        print("  Q. <== Retour")

        return input("\n>>> Entrez votre choix : ")
