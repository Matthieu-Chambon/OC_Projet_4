from controllers import UserManager, TournamentManager, MenuManager

import re
from rich import print
from rich.prompt import Prompt


class Application:
    def __init__(self):
        self.userManager = UserManager(self)
        self.tournamentManager = TournamentManager(self, self.userManager)
        self.menuManager = MenuManager(self)

    def display_menu(self):
        self.menuManager.display_main_menu(
            self.tournamentManager,
            self.userManager
        )

    def get_valid_input(self, prompt, options, regex, default):
        prompt = (
                f"\n[green_yellow]>>> "
                f"[white]{prompt}"
        )

        if options is not None:
            prompt += f"[yellow] ({options})"

        if default is not None:
            prompt += f"[cyan] ({default})"

        while True:
            user_input = Prompt.ask(prompt)

            if user_input == "" and default is not None:
                return default

            elif re.fullmatch(regex, user_input):
                return user_input

            else:
                print(f"[bright_red]\"{user_input}\"[/bright_red] "
                      f"est invalide. Réessayez.")
