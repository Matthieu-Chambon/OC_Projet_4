from datetime import date


class Tournament:
    def __init__(self, name, location, rounds, players, description):
        self.name = name
        self.location = location
        self.startDate = date.today().strftime("%d/%m/%Y %H:%M:%S")
        self.endDate = None
        self.numberOfRounds = rounds
        self.currentRound = 1
        self.roundsList = []
        self.playersList = players
        self.description = description
        self.status = "En cours"
