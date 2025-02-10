from models import Player, Tournament, Round, Match
from views import TournamentView, PlayerView

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


class PlayerManager:
    def __init__(self):
        self.players = []
        self.players.append(Player("Dupont", "Jean", "15/04/1985", "AB12345"))
        self.players.append(Player("Martin", "Sophie", "22/08/1990", "CD67890"))
        self.players.append(Player("Durand", "Lucas", "05/12/1983", "EF13579"))
        self.players.append(Player("Lefevre", "Emma", "30/06/1995", "GH24680"))
        self.players.append(Player("Morel", "Hugo", "17/02/1988", "IJ98765"))
        self.players.append(Player("Lemoine", "Alice", "09/09/1992", "KL54321"))
        self.players.append(Player("Rousseau", "Thomas", "28/11/1980", "MN11223"))
        self.players.append(Player("Perrin", "Camille", "14/07/1987", "OP33445"))
        self.players.append(Player("Fournier", "Noé", "03/03/1993", "QR55667"))
        self.players.append(Player("Girard", "Laura", "19/10/1991", "ST77889"))
        self.players.append(Player("Blanc", "Maxime", "25/05/1986", "UV99001"))
        self.players.append(Player("Gauthier", "Julie", "07/01/1994", "WX22334"))
        self.players.append(Player("Chevalier", "Antoine", "12/06/1989", "YZ44556"))
        self.players.append(Player("André", "Lucie", "08/04/1996", "AB66778"))
        self.players.append(Player("Bernard", "Paul", "21/09/1984", "CD88990"))
        self.players.append(Player("Noel", "Clara", "02/12/1982", "EF11223"))

        self.playerView = PlayerView()

    def display_players(self):
        self.playerView.display_players(self.players)

    def reset_scores(self):
        for player in self.players:
            player.score = 0
