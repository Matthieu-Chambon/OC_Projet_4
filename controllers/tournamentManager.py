from models import Tournament, Round, Match
from views import TournamentView

import random


class TournamentManager:
    def __init__(self):
        self.tournamentView = TournamentView()

    def createTournament(self, name, place, rounds, players, description):
        # Créer un tournoi
        self.tournament = Tournament(name, place, rounds, players, description)

        self.create_rounds()

    def sort_players(self):
        if self.tournament.currentRound == 1:
            random.shuffle(self.tournament.playersList)
        else:
            self.tournament.playersList.sort(key=lambda player: player.score, reverse=True)

    # Créer autant de rounds qu'indiqué dans la classe Tournament
    def create_rounds(self):
        for i in range(self.tournament.numberOfRounds):
            self.tournament.roundsList.append(Round("Round " + str(i+1)))

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

    def auto_play_one_round(self):
        self.sort_players()
        self.display_players()
        self.create_matchs()
        self.random_results()
        self.display_matchs()
        self.tournament.currentRound += 1

    def display_players(self):
        self.tournamentView.display_players(self.tournament)

    def display_matchs(self):
        self.tournamentView.display_matchs(self.tournament)
