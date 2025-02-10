class TournamentView():
    def display_players(self, tournament):
        print("\nScore total des joueurs")
        for player in tournament.playersList:
            print(f"{player.surname} {player.name} - Score : {player.score}")

    def display_matchs(self, tournament):
        print("\nRésultats des matchs du round " + str(tournament.currentRound))
        for match in tournament.roundsList[tournament.currentRound-1].matchsList:
            print(f"{match.joueur1.surname} {match.joueur1.name} {match.score1} VS {match.score2} {match.joueur2.surname} {match.joueur2.name}")


class PlayerView():
    def display_players(self, players):
        print("\nListe des joueurs d'échec")
        for player in players:
            print(f"{player.surname} {player.name}")
