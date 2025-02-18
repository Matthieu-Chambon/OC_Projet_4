from models.user import User


class Match:
    def __init__(self, j1, j2):
        self.joueur1 = j1
        self.joueur2 = j2
        self.score1 = 0
        self.score2 = 0

    def __str__(self):
        return f"{self.joueur1} ({self.score1}) - ({self.score2}) {self.joueur2}"

    def to_dict(self):
        return {
            "joueur1": self.joueur1.to_dict(),
            "joueur2": self.joueur2.to_dict(),
            "score1": self.score1,
            "score2": self.score2
        }

    @staticmethod
    def from_dict(match_dict):
        match = Match(
            User.from_dict(match_dict["joueur1"]),
            User.from_dict(match_dict["joueur2"])
        )

        match.score1 = match_dict["score1"]
        match.score2 = match_dict["score2"]

        return match
