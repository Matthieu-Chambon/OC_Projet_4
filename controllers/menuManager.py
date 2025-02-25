from views import MenuView

from rich import print


class MenuManager:
    def __init__(self, app):
        self.menuView = MenuView()
        self.app = app

    def display_main_menu(self, tournamentManager, userManager):
        while True:
            choice = self.menuView.main_menu()

            match choice:
                case "1":
                    self.display_user_menu(userManager)
                case "2":
                    self.select_tournament(tournamentManager)
                case "3":
                    tournamentManager.create_new_tournament()
                case "4":
                    tournamentManager.delete_tournament()
                case "q" | "Q":
                    break
                case _:
                    print("[red]Choix invalide, veuillez réessayer.")

    def display_user_menu(self, userManager):
        while True:
            choice = self.menuView.user_menu()

            match choice:
                case "1":
                    userManager.display_users()
                case "2":
                    userManager.create_new_user()
                case "3":
                    userManager.edit_user()
                case "4":
                    userManager.delete_user()
                case "q" | "Q":
                    break
                case _:
                    print("[red]Choix invalide, veuillez réessayer.")

    def display_tournament_menu(self, tournamentManager, tournament):
        while True:
            choice = self.menuView.tournament_menu(tournament)

            match choice:
                case "1":
                    tournamentManager.display_tournament(tournament)
                case "2":
                    if tournament.check_status("En cours"):
                        last_round = tournament.roundsList[-1]
                        tournamentManager.display_round(last_round)
                case "3":
                    tournamentManager.display_players_by_score(tournament)
                case "4":
                    tournamentManager.start_tournament(tournament)
                case "5":
                    tournamentManager.edit_tournament(tournament)
                case "6":
                    tournamentManager.edit_match(tournament)
                case "7":
                    tournamentManager.end_round(tournament)
                case "q" | "Q":
                    break
                case _:
                    print("[red]Choix invalide, veuillez réessayer.")

    def select_tournament(self, tournamentManager):
        nb_tournaments = len(tournamentManager.tournaments)

        if nb_tournaments == 0:
            print("[red]Aucun tournoi enregistré.")

        else:
            tournamentManager.display_all_tournaments()
            while True:
                user_input = self.app.get_valid_input(
                    "Entrez le [red]numéro[/red] du tournoi",
                    "q > quitter",
                    "^[0-9]+$|^[qQ]$",
                    "q"
                )

                if user_input.lower() == "q" or user_input.lower() == "":
                    break

                elif 0 < int(user_input) <= nb_tournaments:
                    index = int(user_input)-1

                    self.display_tournament_menu(
                        tournamentManager,
                        tournamentManager.tournaments[index])
                    break

                else:
                    print("[red]Numéro de tournoi invalide.")
