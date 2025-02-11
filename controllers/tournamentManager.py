from models import Tournament, Round, Match
from views import TournamentView

import random


class TournamentManager:
    def __init__(self):
        self.tournamentView = TournamentView()

    def create_new_tournament(self, userManager):

        name = input("\n>>> Entrez le nom du tournoi : ")
        if name == "":
            name = "Nouveau tournoi"

        place = input("\n>>> Entrez le lieu : ")
        if place == "":
            place = "Paris"

        rounds = input("\n>>> Entrez le nombre de round : ")
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

        self.tournament = Tournament(name, place, rounds, players, description)
        self.sort_players()
        self.tournamentView.display_tournament(self.tournament)
        self.tournamentView.display_players(self.tournament)
        self.create_round()
        self.create_matchs()

    def sort_players(self):
        if self.tournament.currentRound == 1:
            random.shuffle(self.tournament.playersList)
        else:
            self.tournament.playersList.sort(key=lambda player: player.score, reverse=True)

    def create_round(self):
        self.tournament.roundsList.append(Round("Round " + str(self.tournament.currentRound)))

    # Créer les matchs d'un round en fonction du tri
    def create_matchs(self):
        # Créer nb_joueurs/2 matchs
        for i in range(int(len(self.tournament.playersList)/2)):
            self.tournament.roundsList[self.tournament.currentRound-1].matchsList.append(Match(self.tournament.playersList[i*2], self.tournament.playersList[i*2+1]))

    def random_results(self):
        for match in self.tournament.roundsList[self.tournament.currentRound-1].matchsList:
            match.score1 = random.choice([0, 1])
            if match.score1 == 0:
                match.score2 = 1
                match.joueur2.score += 1
            else:
                match.score2 = 0
                match.joueur1.score += 1

    def edit_match(self):
        self.display_current_round()
        match = input("\n>>> Entrez le numéro du match à modifier : ")
        score1 = input("\n>>> Entrez le score du joueur 1 : ")
        score2 = input("\n>>> Entrez le score du joueur 2 : ")

        self.tournament.roundsList[self.tournament.currentRound-1].matchsList[int(match)-1].score1 = int(score1)
        self.tournament.roundsList[self.tournament.currentRound-1].matchsList[int(match)-1].score2 = int(score2)

    def end_round(self):
        self.calculate_player_score()
        self.tournament.currentRound += 1
        self.create_round()
        self.sort_players()
        self.create_matchs()
        self.display_players()
        self.display_current_round()

    def calculate_player_score(self):
        for player in self.tournament.playersList:
            player.score = 0
            for round in self.tournament.roundsList:
                for match in round.matchsList:
                    if match.joueur1 == player:
                        player.score += match.score1
                    elif match.joueur2 == player:
                        player.score += match.score2

    def display_tournament(self):
        self.tournamentView.display_tournament(self.tournament)

    def display_current_round(self):
        self.tournamentView.display_current_round(self.tournament)

    def display_players(self):
        self.tournamentView.display_players(self.tournament)
