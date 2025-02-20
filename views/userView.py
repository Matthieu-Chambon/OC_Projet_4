from rich.console import Console
from rich.table import Table


class UserView():
    def __init__(self):
        self.console = Console()

    def display_users(self, users):

        table = Table(title="\nListe de tous les utilisateurs :man: :woman:")
        table.title_style = "bold"
        table.add_column("N°", style="red", justify="center")
        table.add_column("Nom", style="cyan", justify="center")
        table.add_column("Prénom", style="yellow", justify="center")
        table.add_column("Date de naissance", style="magenta", justify="center")
        table.add_column("ID National", style="green", justify="center")

        for index, user in enumerate(users, start=1):
            table.add_row(str(index), user.surname, user.name, user.dateOfBirth, user.nationalID)
        self.console.print(table)
