class MenuView:
    def main_menu(self):
        print("\nx=x=x=x=x=x=x MENU PRINCIPAL x=x=x=x=x=x=x\n")
        print("  1. Liste des utilisateurs")
        print("  2. Liste des tournois")
        print("  3. Créer un nouveau tournoi")
        print("  4. Supprimer un tournoi")
        print("  Q. Quitter")

        return input("\n>>> Entrez votre choix : ")

    def user_menu(self):
        print("\nx=x=x=x=x=x=x UTILISATEURS x=x=x=x=x=x=x\n")
        print("  1. Afficher utilisateurs")
        print("  2. Créer un nouveau utilisateur")
        print("  3. Modifier un utilisateur")
        print("  4. Supprimer un utilisateur")
        print("  5. Créer des faux utilisateurs")
        print("  Q. <== Retour")

        return input("\n>>> Entrez votre choix : ")

    def tournament_menu(self):
        print("\nx=x=x=x=x=x=x TOURNOI x=x=x=x=x=x=x\n")
        print("  1. Afficher les informations du tournoi")
        print("  2. Afficher les matchs du tour en cours")
        print("  3. Afficher les joueurs du tournoi")
        print("  4. Commencer le tournoi")
        print("  5. Modifier le tournoi")
        print("  6. Modifier un match")
        print("  7. Terminer le tour")
        print("  Q. <== Retour")

        return input("\n>>> Entrez votre choix : ")
