from rich import print
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.columns import Columns
from rich.text import Text
from rich.console import Group


class UserView():
    def __init__(self):
        self.console = Console()

    def display_users(self, users):

        table = Table(title="\nListe de tous les utilisateurs :man: :woman:")
        table.title_style = "bold"

        table.add_column("N°", style="red", justify="center")
        table.add_column("Nom", style="cyan", justify="left")
        table.add_column("Prénom", style="magenta", justify="left")
        table.add_column("Date de naissance", style="yellow", justify="center")
        table.add_column("ID National", style="green", justify="center")

        for index, user in enumerate(users, start=1):
            table.add_row(
                str(index),
                user.surname,
                user.name,
                user.dateOfBirth,
                user.nationalID)

        self.console.print(table, justify="center")

    def display_user(self, user):
        table = Table(title="\nInformations sur l'utilisateur :information:")
        table.title_style = "bold"

        table.add_column("N°", style="red", justify="center")
        table.add_column("Champ", style="cyan", justify="left")
        table.add_column("Valeur", style="magenta", justify="left")

        table.add_row("1", "Nom de famille", user.surname)
        table.add_row("2", "Prénom", user.name)
        table.add_row("3", "Date de naissance", user.dateOfBirth)
        table.add_row("4", "Identifiant national", user.nationalID)

        self.console.print(table, justify="center")

    def display_new_user(self, user):

        col_1_text = [
            Text(""),
            Text("Nom de famille :", style="white", justify="right"),
            Text("Prénom :", style="white", justify="right"),
            Text("Date de naissance :", style="white", justify="right"),
            Text("Identifiant national :", style="white", justify="right")
        ]

        col_1_grp = Group(*col_1_text)

        col_2_text = [
            Text(""),
            Text(user.surname, style="cyan"),
            Text(user.name, style="cyan"),
            Text(user.dateOfBirth, style="cyan"),
            Text(user.nationalID, style="cyan")
        ]

        col_2_grp = Group(*col_2_text)

        max_col_1_width = max(
            self.console.measure(text).maximum for text in col_1_text
            )

        max_col_2_width = max(
            self.console.measure(text).maximum for text in col_2_text
            )

        panel_width = max_col_1_width + max_col_2_width + 5

        if panel_width < 40:
            panel_width = 40

        panel = Panel(
            Columns([col_1_grp, col_2_grp], expand=False),
            title="[green]Utilisateur enregistré avec succès",
            expand=False,
            width=panel_width
        )

        print()
        self.console.print(panel, justify="center")
