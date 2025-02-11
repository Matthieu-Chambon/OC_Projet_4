class TournamentView():
    def display_tournament(self, tournament):
        print("\n - Tournoi actuel - \n")
        print(f"Nom : {tournament.name}")
        print(f"Lieu : {tournament.location}")
        print(f"Date de début : {tournament.startDate}")
        print(f"Date de fin : {tournament.endDate}")
        print(f"Nombre de tours : {tournament.numberOfRounds}")
        print(f"Tour actuel : {tournament.currentRound}")
        print(f"Description : {tournament.description}")

    def display_players(self, tournament):
        print("\n - Liste des joueurs du tournoi - \n")

        col_widths = [5, 15, 15, 7]
        header = f"{'N°':<{col_widths[0]}} {'Nom':<{col_widths[1]}} {'Prénom':<{col_widths[2]}} {'Score':<{col_widths[3]}}"
        print(header)
        print("=" * len(header))

        for index, player in enumerate(tournament.playersList, start=1):
            print(f"{index:<{col_widths[0]}} {player.surname:<{col_widths[1]}} {player.name:<{col_widths[2]}} {player.score:<{col_widths[3]}}")

    def display_current_round(self, tournament):
        print("\n - Matchs du tour actuel (Round " + str(tournament.currentRound) + ") - \n")

        col_widths = [5, 20, 7, 2, 7, 20]
        header = f"{'N°':<{col_widths[0]}} {'Joueur 1':<{col_widths[1]}} {'Score':<{col_widths[2]}} {'VS':^{col_widths[3]}} {'Score':>{col_widths[4]}} {'Joueur 2':>{col_widths[5]}}"
        print(header)
        print("=" * len(header))

        for index, match in enumerate(tournament.roundsList[tournament.currentRound-1].matchsList, start=1):
            j1_fullname = f"{match.joueur1.surname} {match.joueur1.name}"
            j2_fullname = f"{match.joueur2.surname} {match.joueur2.name}"
            print(f"{index:<{col_widths[0]}} {j1_fullname:<{col_widths[1]}} {match.score1:<{col_widths[2]}} {'VS':^{col_widths[3]}} {match.score2:>{col_widths[4]}} {j2_fullname:>{col_widths[5]}}")
