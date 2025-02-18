class TournamentView():
    def display_all_tournaments(self, tournaments):
        print("\n - Liste de tous les tournois - \n")
        col_widths = [5, 20, 20, 15]
        header = f"{'N°':<{col_widths[0]}} {'Nom':<{col_widths[1]}} {'Lieu':<{col_widths[2]}} {'Statut':<{col_widths[3]}}"
        print(header)
        print("=" * len(header))

        for index, tournament in enumerate(tournaments, start=1):
            print(f"{index:<{col_widths[0]}} {tournament.name:<{col_widths[1]}} {tournament.location:<{col_widths[2]}} {tournament.status:<{col_widths[3]}}")

    def display_tournament(self, tournament):
        col_width = 18
        print("\n - Informations sur le tournoi - \n")
        print(f"{'Nom : ':<{col_width}}{tournament.name}")
        print(f"{'Lieu : ':<{col_width}}{tournament.location}")
        print(f"{'Date de début : ':<{col_width}}{tournament.startDate}")
        print(f"{'Date de fin : ':<{col_width}}{tournament.endDate}")
        print(f"{'Nombre de tours : ':<{col_width}}{tournament.numberOfRounds}")
        print(f"{'Tour actuel : ':<{col_width}}{tournament.currentRound}")
        print(f"{'Description : ':<{col_width}}{tournament.description}")
        print(f"{'Statut : ':<{col_width}}{tournament.status}")

    def display_players(self, tournament):
        print("\n - Liste des joueurs du tournoi - \n")

        col_widths = [5, 15, 15, 7]
        header = f"{'N°':<{col_widths[0]}} {'Nom':<{col_widths[1]}} {'Prénom':<{col_widths[2]}} {'Score':<{col_widths[3]}}"
        print(header)
        print("=" * len(header))

        for index, player in enumerate(tournament.playersList, start=1):
            print(f"{index:<{col_widths[0]}} {player.surname:<{col_widths[1]}} {player.name:<{col_widths[2]}} {tournament.scores[player.nationalID]:<{col_widths[3]}}")

    def display_round(self, round):
        print("\n - Matchs du " + round.name + " - \n")

        print(f"{'Date de début : ':<{16}}{round.startDate}")
        print(f"{'Date de fin : ':<{16}}{round.endDate}\n")

        col_widths = [5, 20, 7, 2, 7, 20]
        header = f"{'N°':<{col_widths[0]}} {'Joueur 1':<{col_widths[1]}} {'Score':<{col_widths[2]}} {'VS':^{col_widths[3]}} {'Score':>{col_widths[4]}} {'Joueur 2':>{col_widths[5]}}"
        print(header)
        print("=" * len(header))

        for index, match in enumerate(round.matchsList, start=1):
            j1_fullname = f"{match.joueur1.surname} {match.joueur1.name}"
            j2_fullname = f"{match.joueur2.surname} {match.joueur2.name}"
            print(f"{index:<{col_widths[0]}} {j1_fullname:<{col_widths[1]}} {match.score1:<{col_widths[2]}} {'VS':^{col_widths[3]}} {match.score2:>{col_widths[4]}} {j2_fullname:>{col_widths[5]}}")
