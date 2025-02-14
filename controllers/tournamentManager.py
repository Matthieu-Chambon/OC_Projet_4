from models import Tournament, Round, Match
from views import TournamentView

import random
from datetime import datetime
import json
# import os


class TournamentManager:
    def __init__(self):
        self.tournamentView = TournamentView()
        self.tournaments = []

    def create_new_tournament(self, userManager):

        name = input("\n>>> Entrez le nom du tournoi : ")
        if name == "":
            name = "Nouveau tournoi"

        place = input("\n>>> Entrez le lieu : ")
        if place == "":
            place = "Paris"

        rounds = int(input("\n>>> Entrez le nombre de round : "))
        if rounds == "":
            rounds = 4

        description = input("\n>>> Entrez la description : ")
        if description == "":
            description = "Description du tournoi"

        userManager.display_users()

        players = []
        while True:
            player = input("\n>>> Choisissez un joueur via son N° (q pour quitter) : ")
            if player == "q":
                break
            else:
                players.append(userManager.users[int(player)-1])

        self.tournaments.append(Tournament(name, place, rounds, players, description))
        self.sort_players(self.tournaments[-1])
        self.tournamentView.display_tournament(self.tournaments[-1])
        self.tournamentView.display_players(self.tournaments[-1])
        self.create_round(self.tournaments[-1])
        self.create_matchs(self.tournaments[-1])

    def sort_players(self, tournament):
        if tournament.currentRound == 1:
            random.shuffle(tournament.playersList)
        else:
            tournament.playersList.sort(key=lambda player: player.score, reverse=True)

    def create_round(self, tournament):
        tournament.roundsList.append(Round("Round " + str(tournament.currentRound)))

    # Créer les matchs d'un round en fonction du tri
    def create_matchs(self, tournament):
        # Créer nb_joueurs/2 matchs
        for i in range(int(len(tournament.playersList)/2)):
            tournament.roundsList[tournament.currentRound-1].matchsList.append(Match(tournament.playersList[i*2], tournament.playersList[i*2+1]))

    def edit_match(self, tournament):
        while True:
            self.display_round(tournament.roundsList[-1])
            match = input("\n>>> Entrez le numéro du match à modifier (q pour quitter) : ")
            if match == "q":
                break
            elif int(match) <= len(tournament.roundsList[-1].matchsList) and int(match) > 0:
                score1 = input("\n>>> Entrez le score du joueur 1 : ")
                score2 = input(">>> Entrez le score du joueur 2 : ")

                tournament.roundsList[tournament.currentRound-1].matchsList[int(match)-1].score1 = int(score1)
                tournament.roundsList[tournament.currentRound-1].matchsList[int(match)-1].score2 = int(score2)
            else:
                print("Match invalide.")

    def end_round(self, tournament):
        if tournament.status == "En cours":
            self.calculate_player_score(tournament)
            tournament.roundsList[-1].endDate = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

            if tournament.currentRound == tournament.numberOfRounds:
                tournament.endDate = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                tournament.status = "Terminé"

                print("Le tournoi est terminé. Résultats finaux :")
                self.calculate_player_score(tournament)
                self.display_players(tournament)

            else:
                tournament.currentRound += 1
                self.create_round(tournament)
                self.sort_players(tournament)
                self.create_matchs(tournament)
                self.display_players(tournament)
                self.display_round(tournament.roundsList[-1])
        else:
            print("Action impossible, le tournoi est terminé.")

    def calculate_player_score(self, tournament):
        for player in tournament.playersList:
            player.score = 0
            for round in tournament.roundsList:
                for match in round.matchsList:
                    if match.joueur1 == player:
                        player.score += match.score1
                    elif match.joueur2 == player:
                        player.score += match.score2

    def export_tournament_to_JSON(self):
        fileName = "data/current_tournament.json"
        with open(fileName, "w", encoding="utf-8") as file:
            json.dump(self.tournament.to_dict(), file, indent=4)
        pass

    def import_tournament_from_JSON(self):
        pass

    def display_all_tournaments(self):
        self.tournamentView.display_all_tournaments(self.tournaments)

    def display_tournament(self, tournament):
        self.tournamentView.display_tournament(tournament)

        for round in tournament.roundsList:
            self.tournamentView.display_round(round)

    def display_round(self, round):
        self.tournamentView.display_round(round)

    def display_players(self, tournament):
        self.tournamentView.display_players(tournament)
