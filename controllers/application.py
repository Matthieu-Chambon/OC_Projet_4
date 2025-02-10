from controllers import UserManager, TournamentManager, MenuManager


class Application:
    def __init__(self):
        self.userManager = UserManager()
        self.tournamentManager = TournamentManager()
        self.menuManager = MenuManager()

        listOfPlayers = []

        for user in self.userManager.users:
            listOfPlayers.append(user)

        self.tournamentManager.createTournament("Tournoi d'échec", "Paris", 4, listOfPlayers, "Le premier tournoi d'échec de Paris !")

    def auto_tournament(self):

        self.userManager.display_users()

        self.userManager.reset_scores()
        while self.tournamentManager.tournament.currentRound <= self.tournamentManager.tournament.numberOfRounds:
            self.tournamentManager.auto_play_one_round()

        self.tournamentManager.sort_players()
        self.tournamentManager.display_players()

    def menu(self):
        self.menuManager.display_main_menu(self.tournamentManager, self.userManager)
