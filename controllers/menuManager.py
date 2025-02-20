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
                    if len(userManager.users) < 2:
                        print("Il faut au moins 2 utilisateurs.")
                    else:
                        tournamentManager.create_new_tournament(userManager)
                case "4":
                    tournamentManager.delete_tournament()
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
                    userManager.create_new_user()
                case "3":
                    pass
                case "4":
                    userManager.delete_user()
                case "5":
                    userManager.create_fake_users()
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
                    if tournament.check_status("En cours"):
                        last_round = tournament.roundsList[-1]
                        tournamentManager.display_round(last_round)
                case "3":
                    tournamentManager.display_players(tournament)
                case "4":
                    tournamentManager.start_tournament(tournament)
                case "5":
                    pass
                case "6":
                    tournamentManager.edit_match(tournament)
                case "7":
                    tournamentManager.end_round(tournament)
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
                        self.display_tournament_menu(
                            tournamentManager,
                            tournamentManager.tournaments[user_input-1])
                        break
                    else:
                        print("Numéro de tournoi invalide.")
                except ValueError:
                    print("Entrée invalide. Seuls les chiffres sont acceptés.")
