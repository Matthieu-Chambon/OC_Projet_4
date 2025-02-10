from datetime import date


class Tournament:
    def __init__(self, name, place, rounds, players, description):
        self.name = name
        self.place = place
        self.startDate = date.today().strftime("%d/%m/%Y")
        self.endDate = None
        self.numberOfRounds = rounds
        self.currentRound = 1
        self.roundsList = []
        self.playersList = players
        self.description = description
