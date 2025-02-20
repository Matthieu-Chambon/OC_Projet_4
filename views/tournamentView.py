from rich import print
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.console import Group
from rich.text import Text


class TournamentView():
    def __init__(self):
        self.console = Console()

    def display_all_tournaments(self, tournaments):
        table = Table(title="\nListe de tous les tournois :trophy:")
        table.title_style = "bold"
        table.add_column("N°", style="red", justify="center")
        table.add_column("Nom", style="cyan", justify="center")
        table.add_column("Lieu", style="yellow", justify="center")
        table.add_column("Statut", style="green", justify="center")

        for index, tournament in enumerate(tournaments, start=1):
            table.add_row(str(index), tournament.name, tournament.location, tournament.status)

        self.console.print(table)

    def display_tournament(self, tournament):
        elements = []

        col_width = 18
        text = Text(f"\n{'Nom : ':<{col_width}}{tournament.name}"
                    + f"\n{'Lieu : ':<{col_width}}{tournament.location}"
                    + f"\n{'Date de début : ':<{col_width}}{tournament.startDate}"
                    + f"\n{'Date de fin : ':<{col_width}}{tournament.endDate}"
                    + f"\n{'Nombre de tours : ':<{col_width}}{tournament.numberOfRounds}"
                    + f"\n{'Tour actuel : ':<{col_width}}{tournament.currentRound}"
                    + f"\n{'Description : ':<{col_width}}{tournament.description}"
                    + f"\n{'Statut : ':<{col_width}}{tournament.status}\n"
                    )

        elements.extend(text)
        elements.extend(item for round in tournament.roundsList for item in self.display_round(round, False))

        group = Group(*elements)
        panel = Panel(group, title=tournament.name, expand=False)

        print()
        self.console.print(panel)

    def display_players(self, tournament):
        table = Table(title="\nListe des joueurs du tournoi :man: :woman:")
        table.title_style = "bold"
        table.min_width = len(table.title)
        table.add_column("N°", style="red", justify="center")
        table.add_column("Joueur", style="cyan", justify="center")
        table.add_column("Score", style="yellow", justify="center")

        for index, player in enumerate(tournament.playersList, start=1):
            table.add_row(str(index), f"{player.name} {player.surname}", str(tournament.scores[player.nationalID]))

        self.console.print(table)

    def display_round(self, round, show):

        table = Table(title="\nListe des matchs du " + round.name)
        table.title_style = "bold"
        table.add_column("N°", style="red", justify="center")
        table.add_column("Joueur 1", style="cyan", justify="left")
        table.add_column("Score", style="yellow", justify="center")
        table.add_column("VS", style="white", justify="center")
        table.add_column("Score", style="yellow", justify="center")
        table.add_column("Joueur 2", style="cyan", justify="right")

        for index, match in enumerate(round.matchsList, start=1):
            j1_fullname = f"{match.joueur1.surname} {match.joueur1.name}"
            j2_fullname = f"{match.joueur2.surname} {match.joueur2.name}"
            table.add_row(str(index), j1_fullname, str(match.score1), "VS", str(match.score2), j2_fullname)

        text = Text(f"{'Date de début : ':<{16}}{round.startDate}"
                    + f"\n{'Date de fin : ':<{16}}{round.endDate}\n")

        if show:
            self.console.print(table)
            print(text)

        return table, text
