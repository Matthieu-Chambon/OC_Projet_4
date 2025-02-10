from views import MenuView


class MenuManager:
    def __init__(self):
        self.menuView = MenuView()

    def display_main_menu(self, tournamentManager, userManager):
        while True:
            choice = self.menuView.main_menu()

            match choice:
                case "1":
                    self.display_user_menu(tournamentManager, userManager)
                case "2":
                    pass
                case "3":
                    tournamentManager.auto_play_one_round()
                case "q" | "Q":
                    break
                case _:
                    print("Choix invalide, veuillez réessayer.")

    def display_user_menu(self, tournamentManager, userManager):
        while True:
            choice = self.menuView.user_menu()

            match choice:
                case "1":
                    userManager.display_users()
                case "2":
                    userManager.export_users_to_JSON()
                case "3":
                    userManager.import_users_from_JSON()
                case "4":
                    userManager.create_fake_users()
                case "5":
                    userManager.create_new_user()
                case "q" | "Q":
                    break
                case _:
                    print("Choix invalide, veuillez réessayer.")
