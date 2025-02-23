from models import Tournament, Round, Match
from views import TournamentView

from datetime import datetime
import re


class TournamentManager:
    def __init__(self, userManager):
        self.tournamentView = TournamentView()
        self.tournaments = Tournament.load_tournaments_from_JSON(
            userManager.users
            )

    def create_new_tournament(self, userManager):
        print("\n - Création d'un nouveau tournoi -")

        name = self.get_valid_input(
            "Entrez le nom du tournoi",
            r"^[a-zA-Z0-9 ]{1,50}$",
            "Nouveau tournoi")

        place = self.get_valid_input("Entrez le lieu",
                                     r"^[a-zA-Z0-9 ]{1,50}$",
                                     "Paris")
        rounds = int(self.get_valid_input(
            "Entrez le nombre de rounds",
            r"^[1-9][0-9]{,2}$",
            4))

        description = self.get_valid_input(
            "Entrez la description",
            r"^[a-zA-Z0-9 ]{1,50}$",
            "Premier tournoi de la région !")

        userManager.display_users()

        players = []
        while True:
            user_input = self.get_valid_input(
                "Choisissez un joueur via son N° "
                "(q > quitter | a > affichage)",
                r"^[1-9][0-9]*$|^[aAqQ]$",
                "q")

            if user_input == "q" or user_input == "Q":
                if len(players) % 2 == 0:
                    if len(players) != 0:
                        break
                    else:
                        print("Vous devez sélectionner au moins 2 joueurs.")
                else:
                    print("Le nombre de joueurs doit être pair.")

            elif user_input == "a" or user_input == "A":
                print("\n - Liste des joueurs sélectionnés -")
                if len(players) == 0:
                    print("Aucun joueur sélectionné.")
                for player in players:
                    print(f"{player.surname} {player.name}")
            elif int(user_input) > len(userManager.users):
                print("Le nombre choisi est trop grand. Réessayez.")
            elif userManager.users[int(user_input)-1] in players:
                players.remove(userManager.users[int(user_input)-1])
                print(
                    f"{userManager.users[int(user_input)-1].surname} "
                    f"{userManager.users[int(user_input)-1].name} "
                    f"a été retiré.")
            else:
                players.append(userManager.users[int(user_input)-1])
                print(
                    f"{userManager.users[int(user_input)-1].surname} "
                    f"{userManager.users[int(user_input)-1].name} "
                    f"a été ajouté.")

        self.tournaments.append(
            Tournament(name, place, rounds, players, description)
            )
        self.tournaments[-1].sort_players_by_score()
        self.tournamentView.display_tournament(self.tournaments[-1])
        self.tournamentView.display_players(self.tournaments[-1])

        Tournament.save_tournaments_to_JSON(self.tournaments)

    def start_tournament(self, tournament):
        if tournament.check_status("Non commencé"):
            print("Le tournoi commence !")
            tournament.startDate = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            tournament.status = "En cours"
            self.create_round(tournament)
            self.create_matchs(tournament)
            self.display_round(tournament.roundsList[-1])

    def create_round(self, tournament):
        tournament.roundsList.append(
            Round("Round " + str(tournament.currentRound))
            )

    # Créer les matchs d'un round en fonction du tri
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

    def edit_match(self, tournament):
        if not tournament.check_status("En cours"):
            return

        while True:
            self.display_round(tournament.roundsList[-1])

            input_match = self.get_valid_input(
                "Entrez le numéro du match à modifier (q pour quitter)",
                r"^[1-9][0-9]*$|^[qQ]$",
                "q")
            if input_match.lower() == "q":
                break

            if 0 <= int(input_match)-1\
               < len(tournament.roundsList[-1].matchsList):
                match = tournament.roundsList[-1]\
                        .matchsList[int(input_match)-1]

                score1 = self.get_valid_input(
                    "Entrez le score du joueur 1 (0, 1 ou 0.5)",
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

            if tournament.currentRound == tournament.numberOfRounds:
                tournament.endDate = datetime.now().strftime(
                    "%d/%m/%Y %H:%M:%S")
                tournament.status = "Terminé"

                print("Le tournoi est terminé. Résultats finaux :")
                self.display_players(tournament)

            else:
                tournament.currentRound += 1
                self.create_round(tournament)
                self.create_matchs(tournament)
                self.display_players(tournament)
                self.display_round(tournament.roundsList[-1])

        Tournament.save_tournaments_to_JSON(self.tournaments)

    def delete_tournament(self):
        self.display_all_tournaments()

        while True:
            user_input = self.get_valid_input(
                "Entrez le numéro du tournoi à supprimer (q > quitter)",
                r"^[1-9][0-9]*$|^[qQ]$",
                "q")
            if user_input.lower() == "q":
                break
            elif int(user_input) <= len(self.tournaments):
                user_confirm = self.get_valid_input(
                    f"Confirmez-vous la suppression du tournoi "
                    f"\"{self.tournaments[int(user_input)-1].name}\" ? (o/n)",
                    r"^[oOnN]$",
                    "n")
                if user_confirm == "o" or user_confirm == "O":
                    print(
                        f"Tournoi"
                        f"\"{self.tournaments[int(user_input)-1].name}\""
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
        self.tournamentView.display_round(round, True)

    def display_players(self, tournament):
        self.tournamentView.display_players(tournament)

    def get_valid_input(self, prompt, regex, default):
        while True:
            user_input = input(f"\n>>> {prompt} : ")
            if user_input == "":
                return default
            elif re.fullmatch(regex, user_input):
                return user_input
            else:
                print(f"\"{user_input}\" est invalide. Réessayez.")
