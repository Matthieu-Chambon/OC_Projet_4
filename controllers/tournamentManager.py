from models import Tournament, Round, Match
from views import TournamentView

from datetime import datetime

from rich import print
from rich.rule import Rule


class TournamentManager:
    def __init__(self, app, userManager):
        self.tournamentView = TournamentView()
        self.userManager = userManager
        self.tournaments = Tournament.load_tournaments_from_JSON(
            userManager.users
        )
        self.app = app

        self.fields = {
            "name": ["Entrez le nom du tournoi", None, "Nouveau tournoi"],
            "place": ["Entrez le lieu", None, "Paris"],
            "nb_rounds": ["Entrez le nombre de tours", None, 4],
            "description": ["Entrez la description", None,
                            "Aucune information pour le moment"]
        }

        self.regex_patterns = {
            "name": r"^.{1,50}$",
            "place": r"^.{1,50}$",
            "nb_rounds": r"^[1-9][0-9]{,2}$",
            "description": r"^.{1,100}$"
        }

    def create_new_tournament(self):
        rule = Rule(title="\nCréation d'un nouveau tournoi", style="white")
        print(rule)

        tournament_data = {}

        for attr, (message, options, default) in self.fields.items():
            tournament_data[attr] = self.app.get_valid_input(
                message,
                options,
                self.regex_patterns[attr],
                default
            )

        tournament_data["players"] = self.select_tournament_players([])
        new_tournament = Tournament(**tournament_data)

        self.tournaments.append(new_tournament)
        self.tournamentView.display_tournament(new_tournament)

        Tournament.save_tournaments_to_JSON(self.tournaments)

    def edit_tournament(self, tournament):
        rule = Rule(
            title="Modification d'un tournoi :pencil2: ",
            style="white")
        print(rule)

        while True:
            self.tournamentView.display_edit_tournament(tournament)
            user_input = self.app.get_valid_input(
                "Entrez le [red]numéro[/red] du champ à modifier",
                "q > quitter",
                r"^[12345qQ]$",
                "q"
            )

            if user_input.lower() == "q":
                break

            if user_input == "1":
                attr = "name"

            if user_input == "2":
                attr = "place"

            if user_input == "3":
                if tournament.check_status(["Non commencé"]):
                    attr = "nb_rounds"
                else:
                    continue

            if user_input == "4":
                attr = "description"

            if user_input == "5":
                if tournament.check_status(["Non commencé"]):
                    attr = "playerList"
                    players = tournament.playersList
                    new_value = self.select_tournament_players(players)
                    setattr(tournament, attr, new_value)

                continue

            message, options, default = self.fields[attr]
            default = str(getattr(tournament, attr))

            new_value = self.app.get_valid_input(
                message,
                options,
                self.regex_patterns[attr],
                default
            )

            setattr(tournament, attr, new_value)

        Tournament.save_tournaments_to_JSON(self.tournaments)

    def start_tournament(self, tournament):
        if tournament.check_status("Non commencé"):

            if len(tournament.playersList) < 2:
                print("[red]Action impossible, "
                      "il faut au minimum 2 joueurs dans le tournoi")
                return

            if len(tournament.playersList) % 2 != 0:
                print("[red]Action impossible, "
                      "il faut un nombre pair de joueurs dans le tournoi")
                return

            tournament.startDate = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            tournament.status = "En cours"
            tournament.init_scores()
            tournament.shuffle_players()

            self.create_round(tournament)
            self.create_matchs(tournament)
            self.display_round(tournament.roundsList[-1])

            print("[green]Le tournoi commence !")

    def create_round(self, tournament):
        tournament.roundsList.append(
            Round("Round " + str(tournament.currentRound))
            )

    def create_matchs(self, tournament):
        players = tournament.playersList[:]

        while len(players) > 0:
            player1 = players.pop(0)
            for i, player2 in enumerate(players):
                if not tournament.played_together(player1, player2)\
                   and not tournament.played_together(player2, player1):
                    tournament.roundsList[-1].matchsList.append(
                        Match(player1, player2)
                        )
                    players.pop(i)
                    break
            else:
                tournament.roundsList[-1].matchsList.append(
                    Match(player1, players[0])
                    )
                players.pop(0)

        Tournament.save_tournaments_to_JSON(self.tournaments)

    def select_tournament_players(self, players):
        self.userManager.display_users()
        self.tournamentView.display_selected_players(players)

        while True:
            user_input = self.app.get_valid_input(
                "Choisissez un joueur via son [red]N°",
                "q > quitter | a > affichage joueurs sélectionnés",
                r"^[1-9][0-9]*$|^[aAqQ]$",
                "q")

            if user_input.lower() == "q":
                break

            elif user_input.lower() == "a":
                self.tournamentView.display_selected_players(players)

            elif int(user_input) > len(self.userManager.users):
                print("Le nombre choisi est trop grand. Réessayez.")

            elif self.userManager.users[int(user_input)-1] in players:
                player = self.userManager.users[int(user_input)-1]
                players.remove(player)

                print(
                    f"[red]{player.surname} {player.name} "
                    f"a été retiré"
                )

            else:
                player = self.userManager.users[int(user_input)-1]
                players.append(player)

                print(
                    f"[green]{player.surname} {player.name} "
                    f"a été ajouté"
                )
            players.sort(key=lambda player: player.surname)

        return players

    def edit_match(self, tournament):
        if not tournament.check_status("En cours"):
            return

        while True:
            self.display_round(tournament.roundsList[-1])

            input_match = self.app.get_valid_input(
                "Entrez le [red]numéro[/red] du match à modifier",
                "q > quitter",
                r"^[1-9][0-9]*$|^[qQ]$",
                "q")
            if input_match.lower() == "q":
                break

            if 0 <= int(input_match)-1\
               < len(tournament.roundsList[-1].matchsList):
                last_round = tournament.roundsList[-1]
                match = last_round.matchsList[int(input_match)-1]

                score1 = self.app.get_valid_input(
                    "Entrez le score du joueur 1",
                    "0, 1 ou 0.5) (q > quitter",
                    r"^[10qQ]$|^0[.,]5$",
                    *"q")

                match score1:
                    case "q" | "Q":
                        print("Modification annulée.")
                        break
                    case "0":
                        match.score1 = 0
                        match.score2 = 1
                    case "1":
                        match.score1 = 1
                        match.score2 = 0
                    case "0.5" | "0,5":
                        match.score1 = 0.5
                        match.score2 = 0.5

            else:
                print("Numéro de match invalide.")

        tournament.update_scores()
        Tournament.save_tournaments_to_JSON(self.tournaments)

    def end_round(self, tournament):
        if tournament.check_status("En cours"):
            tournament.roundsList[-1].endDate = datetime.now().strftime(
                "%d/%m/%Y %H:%M:%S")

            if tournament.currentRound == tournament.nb_rounds:
                tournament.endDate = datetime.now().strftime(
                    "%d/%m/%Y %H:%M:%S")
                tournament.status = "Terminé"

                print("Le tournoi est terminé. Résultats finaux :")
                self.display_players_by_score(tournament)

            else:
                tournament.currentRound += 1
                self.create_round(tournament)
                self.create_matchs(tournament)
                self.display_players_by_score(tournament)
                self.display_round(tournament.roundsList[-1])

        Tournament.save_tournaments_to_JSON(self.tournaments)

    def delete_tournament(self):
        rule = Rule(title="\nSuppression d'un tournoi", style="white")
        print(rule)

        self.display_all_tournaments()

        while True:
            user_input = self.app.get_valid_input(
                "Entrez le [red]numéro[/red] du tournoi à supprimer",
                "q > quitter",
                r"^[1-9][0-9]*$|^[qQ]$",
                "q")

            if user_input.lower() == "q":
                break

            elif int(user_input) <= len(self.tournaments):
                name = self.tournaments[int(user_input)-1].name
                user_confirm = self.app.get_valid_input(
                    f"Confirmez-vous la suppression du tournoi "
                    f"\"[cyan]{name}[/cyan]\" ?",
                    "o/n",
                    r"^[oOnN]$",
                    "n")

                if user_confirm == "o" or user_confirm == "O":
                    print(
                        f"Tournoi "
                        f"\"{self.tournaments[int(user_input)-1].name}\" "
                        f"supprimé.")
                    self.tournaments.pop(int(user_input)-1)
                    Tournament.save_tournaments_to_JSON(self.tournaments)
                    self.display_all_tournaments()

                else:
                    print("Suppression annulée.")

            else:
                print("Numéro de tournoi invalide.")

    def display_all_tournaments(self):
        self.tournamentView.display_all_tournaments(self.tournaments)

    def display_tournament(self, tournament):
        self.tournamentView.display_tournament(tournament)

    def display_round(self, round):
        self.tournamentView.display_round(round)

    def display_players_by_score(self, tournament):
        if tournament.check_status(["En cours", "Terminé"]):
            self.tournamentView.display_players_by_score(tournament)
