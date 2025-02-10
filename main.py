from controllers import PlayerManager, TournamentManager

playerManager = PlayerManager()
tournamentManager = TournamentManager()

listOfPlayers = []

for player in playerManager.players:
    listOfPlayers.append(player)

tournamentManager.createTournament("Tournoi d'échec", "Paris", 10, listOfPlayers, "Le premier tournoi d'échec de Paris !")
# playerManager.reset_scores()

playerManager.display_players()

while tournamentManager.tournament.currentRound <= tournamentManager.tournament.numberOfRounds:
    tournamentManager.auto_play_one_round()

tournamentManager.sort_players()
tournamentManager.display_players()
