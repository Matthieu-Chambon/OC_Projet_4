from rich import print
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.console import Group
from rich.text import Text
from rich.columns import Columns
from rich import box
from rich.rule import Rule


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
            table.add_row(
                str(index),
                tournament.name,
                tournament.place,
                tournament.status)

        self.console.print(table, justify="center")

    def display_tournament(self, tournament):
        # Affichage des informations générales du tournoi
        rule = Rule(
            title="Informations sur le tournoi :information: ",
            style="white")
        print(rule)

        labels = [
            Text("Nom : "),
            Text("Lieu : "),
            Text("Date de début : "),
            Text("Date de fin : "),
            Text("Nombre de tours : "),
            Text("Tour actuel : "),
            Text("Description : "),
            Text("Statut : \n")
        ]

        data = [
            Text(f"{tournament.name}", style="cyan"),
            Text(f"{tournament.place}", style="cyan"),
            Text(f"{tournament.startDate}", style="cyan"),
            Text(f"{tournament.endDate}", style="cyan"),
            Text(f"{tournament.nb_rounds}", style="cyan"),
            Text(f"{tournament.currentRound}", style="cyan"),
            Text(f"{tournament.description}", style="cyan"),
            Text(f"{tournament.status}", style="cyan")
        ]

        labels_col = Group(*labels)
        data_col = Group(*data)

        columns = Columns([labels_col, data_col], expand=False)

        pan_width = 25 + max(
            self.console.measure(text).maximum
            for text in data
            )

        panel = Panel(
            columns,
            width=pan_width,
            box=box.SIMPLE_HEAD
        )

        print()
        self.console.print(panel, justify="center")

        # Affichage des joueurs du tournoi
        players = tournament.playersList[:]
        players.sort(key=lambda player: player.surname)

        table = Table(title="\nListe de tous les joueurs :man: :woman:")
        table.title_style = "bold"

        table.add_column("N°", style="red", justify="center")
        table.add_column("Nom", style="cyan", justify="left")
        table.add_column("Prénom", style="magenta", justify="left")
        table.add_column("Date de naissance", style="yellow", justify="center")
        table.add_column("ID National", style="green", justify="center")

        for index, player in enumerate(players, start=1):
            table.add_row(
                str(index),
                player.surname,
                player.name,
                player.dateOfBirth,
                player.nationalID)

        self.console.print(table, justify="center")

        for round in tournament.roundsList:
            self.display_round(round)

    def display_edit_tournament(self, tournament):

        table = Table(title="\nInformations générales")
        table.title_style = "bold"

        table.add_column("N°", style="red", justify="center")
        table.add_column("Champ", style="cyan", justify="left")
        table.add_column("Valeur", style="yellow", justify="left")

        table.add_row("1", "Nom du tournoi", tournament.name)
        table.add_row("2", "Lieu du tournoi", tournament.place)
        table.add_row("3", "Nombre de tours", str(tournament.nb_rounds))
        table.add_row("4", "Description", tournament.description)

        nb_players = str(len(tournament.playersList))
        table.add_row("5", "Liste des joueurs", nb_players + " joueur(s)")

        self.console.print(table, justify="center")

    def display_players_by_score(self, tournament):

        table = Table(
            title="\nScore des joueurs du tournoi :man: :woman: "
        )
        table.title_style = "bold"
        table.min_width = len(table.title)
        table.add_column("N°", style="red", justify="center")
        table.add_column("Joueur", style="cyan", justify="center")
        table.add_column("Score", style="yellow", justify="center")

        for index, player in enumerate(tournament.playersList, start=1):
            table.add_row(
                str(index),
                f"{player.surname} {player.name}",
                str(tournament.scores[player.nationalID])
            )

        self.console.print(table, justify="center")

    def display_round(self, round):

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
            table.add_row(
                str(index),
                j1_fullname,
                str(match.score1),
                "VS",
                str(match.score2),
                j2_fullname
                )

        text = Text(
            f"{'Date de début : ':<{16}}{round.startDate}"
            f"\n{'Date de fin : ':<{16}}{round.endDate}\n"
            )

        self.console.print(table, justify="center")
        self.console.print(text, justify="center")

    def display_selected_players(self, players):

        text = Text()

        if len(players) == 0:
            text.append("\nAucun joueur sélectionné.", style="cyan")

        else:
            for player in players:
                text.append(f"\n{player.surname} {player.name}", style="cyan")

        panel = Panel(
            text,
            title="[green]Liste des joueurs sélectionnés ",
            expand=False,
            box=box.ROUNDED
        )

        print()
        self.console.print(panel, justify="center")
