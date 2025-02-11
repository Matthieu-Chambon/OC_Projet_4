from controllers import UserManager, TournamentManager, MenuManager


class Application:
    def __init__(self):
        self.userManager = UserManager()
        self.tournamentManager = TournamentManager()
        self.menuManager = MenuManager()

    def menu(self):
        self.menuManager.display_main_menu(self.tournamentManager, self.userManager)
