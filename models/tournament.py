from models.round import Round
from models.user import User

import random
import os
import json
from rich import print

FILE_NAME = "data/tournaments/tournaments.json"


class Tournament:
    def __init__(self, name, place, nb_rounds, players, description):
        self.name = name
        self.place = place
        self.startDate = "Aucune date de début"
        self.endDate = "Aucune date de fin"
        self.nb_rounds = int(nb_rounds)
        self.currentRound = 1
        self.roundsList = []
        self.playersList = players
        self.scores = {}
        self.description = description
        self.status = "Non commencé"

    def to_dict(self):
        return {
            "name": self.name,
            "place": self.place,
            "startDate": self.startDate,
            "endDate": self.endDate,
            "nb_rounds": self.nb_rounds,
            "currentRound": self.currentRound,
            "roundsList": [round.to_dict() for round in self.roundsList],
            "playersList": [player.to_dict() for player in self.playersList],
            "scores": {nationalID:
                       score for nationalID, score in self.scores.items()},
            "description": self.description,
            "status": self.status
        }

    @staticmethod
    def from_dict(tournament_dict, users):
        tournament = Tournament(
            tournament_dict["name"],
            tournament_dict["place"],
            tournament_dict["nb_rounds"],
            [User.from_dict(player_dict)
             for player_dict in tournament_dict["playersList"]],
            tournament_dict["description"])

        tournament.startDate = tournament_dict["startDate"]
        tournament.endDate = tournament_dict["endDate"]
        tournament.currentRound = tournament_dict["currentRound"]
        tournament.roundsList = [
            Round.from_dict(round_dict)
            for round_dict in tournament_dict["roundsList"]
            ]
        tournament.scores = {nationalID: score for nationalID,
                             score in tournament_dict["scores"].items()}
        tournament.status = tournament_dict["status"]

        return tournament

    @staticmethod
    def load_tournaments_from_JSON(users):
        if os.path.exists(FILE_NAME):
            with open(FILE_NAME, "r", encoding="utf-8") as file:
                data = json.load(file)
                print(
                    f"Importation des données du fichier JSON \"{FILE_NAME}\"")
                return [Tournament.from_dict(tournament, users)
                        for tournament in data]
        else:
            print(
                f"Le fichier JSON \"{FILE_NAME}\" n'existe pas. "
                f"Aucune donnée importée.")
            return []

    @staticmethod
    def save_tournaments_to_JSON(tournaments):
        with open(FILE_NAME, "w", encoding="utf-8") as file:
            json.dump([tournament.to_dict() for tournament in tournaments],
                      file, indent=4)

    def init_scores(self):
        self.scores = {
            player.nationalID: 0
            for player in self.playersList}

    # def sort_players_by_alphabetical(self):
    #     self.playersList.sort(
    #             key=lambda player:
    #             player.surname)

    def shuffle_players(self):
        random.shuffle(self.playersList)

    def sort_players_by_score(self):
        self.playersList.sort(
                key=lambda player:
                self.scores[player.nationalID],
                reverse=True)

    def update_scores(self):
        print("update_scores")

        for player in self.playersList:
            score = 0
            for round in self.roundsList:
                for match in round.matchsList:
                    if match.joueur1 == player:
                        score += match.score1
                    elif match.joueur2 == player:
                        score += match.score2
            self.scores[player.nationalID] = score

        self.sort_players_by_score()

    def check_status(self, status):
        if self.status in status:
            return True

        elif self.status == "Non commencé":
            print("[red]Action impossible, le tournoi n'a pas commencé.")

        elif self.status == "En cours":
            print("[red]Action impossible, le tournoi a déjà commencé.")

        else:
            print("[red]Action impossible, le tournoi est terminé.")

        return False

    def played_together(self, j1, j2):
        played_pairs = set()
        for round in self.roundsList:
            for match in round.matchsList:
                played_pairs.add((match.joueur1, match.joueur2))

        if (j1, j2) in played_pairs or (j2, j1) in played_pairs:
            return True
        return False
