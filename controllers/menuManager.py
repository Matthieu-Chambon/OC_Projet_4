from views import MenuView


class MenuManager:
    def __init__(self):
        self.menuView = MenuView()

    def display_main_menu(self, tournamentManager, userManager):
        while True:
            choice = self.menuView.main_menu()

            match choice:
                case "1":
                    self.display_user_menu(userManager)
                case "2":
                    self.select_tournament(tournamentManager)
                case "3":
                    tournamentManager.create_new_tournament(userManager)
                case "q" | "Q":
                    break
                case _:
                    print("Choix invalide, veuillez réessayer.")

    def display_user_menu(self, userManager):
        while True:
            choice = self.menuView.user_menu()

            match choice:
                case "1":
                    userManager.display_users()
                case "2":
                    userManager.export_users_to_JSON()
                case "3":
                    userManager.import_users_from_JSON()
                case "4":
                    userManager.create_fake_users()
                case "5":
                    userManager.create_new_user()
                case "q" | "Q":
                    break
                case _:
                    print("Choix invalide, veuillez réessayer.")

    def display_tournament_menu(self, tournamentManager, tournament):
        while True:
            choice = self.menuView.tournament_menu()

            match choice:
                case "1":
                    tournamentManager.display_tournament(tournament)
                case "2":
                    pass
                case "3":
                    tournamentManager.display_round(tournament.roundsList[-1])
                case "4":
                    tournamentManager.edit_match(tournament)
                case "5":
                    tournamentManager.end_round(tournament)
                case "6":
                    tournamentManager.display_players(tournament)
                case "q" | "Q":
                    break
                case _:
                    print("Choix invalide, veuillez réessayer.")

    def select_tournament(self, tournamentManager):
        if len(tournamentManager.tournaments) == 0:
            print("Aucun tournoi enregistré.")
        else:
            tournamentManager.display_all_tournaments()
            while True:
                user_input = input("\n>>> Entrez le numéro du tournoi : ")
                try:
                    user_input = int(user_input)
                    if 0 < user_input <= len(tournamentManager.tournaments):
                        self.display_tournament_menu(tournamentManager, tournamentManager.tournaments[user_input-1])
                        break
                    else:
                        print("Numéro de tournoi invalide.")
                except ValueError:
                    print("Entrée invalide. Seuls les chiffres sont acceptés.")
