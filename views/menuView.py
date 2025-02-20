from rich import print
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich import box


class MenuView:
    def __init__(self):
        self.console = Console()

    def main_menu(self):
        text = Text.from_markup(
            "\n1. [cyan]Liste des utilisateurs[/cyan]\n"
            "2. [cyan]Liste des tournois[/cyan]\n"
            "3. [green]Créer un nouveau tournoi[/green]\n"
            "4. [red]Supprimer un tournoi[/red]\n"
            "Q. [yellow]Quitter[/yellow]",
            justify="left")

        panel = Panel(
            text,
            title="[bold white]MENU PRINCIPAL :chess_pawn:[/bold white]",
            border_style="gray50",
            expand=False,
            box=box.DOUBLE,
        )

        print()
        self.console.print(panel)

        return input("\n>>> Entrez votre choix : ")

    def user_menu(self):

        text = Text.from_markup(
            "\n1. [cyan]Afficher utilisateurs[/cyan]\n"
            "2. [green]Créer un nouveau utilisateur[/green]\n"
            "3. [dark_orange]Modifier un utilisateur[/dark_orange]\n"
            "4. [red]Supprimer un utilisateur[/red]\n"
            "5. [magenta]Créer des faux utilisateurs[/magenta]\n"
            "Q. [yellow]<== Retour[/yellow]",
            justify="left"
            )

        panel = Panel(
            text,
            title="[bold white]UTILISATEURS :man:[/bold white]",
            border_style="gray50",
            expand=False,
            box=box.DOUBLE,
        )

        print()
        self.console.print(panel)

        return input("\n>>> Entrez votre choix : ")

    def tournament_menu(self):
        text = Text.from_markup(
            "\n1. [cyan]Afficher les informations du tournoi[/cyan]\n"
            "2. [cyan]Afficher les matchs du tour en cours[/cyan]\n"
            "3. [cyan]Afficher les joueurs du tournoi[/cyan]\n"
            "4. [green]Commencer le tournoi[/green]\n"
            "5. [dark_orange]Modifier le tournoi[/dark_orange]\n"
            "6. [dark_orange]Modifier un match[/dark_orange]\n"
            "7. [red]Terminer le tour[/red]\n"
            "Q. [yellow]<== Retour[/yellow]",
            justify="left"
        )

        panel = Panel(
            text,
            title="[bold white]TOURNOI :trophy:[/bold white]",
            border_style="gray50",
            expand=False,
            box=box.DOUBLE,
        )
        print()
        self.console.print(panel)

        return input("\n>>> Entrez votre choix : ")
