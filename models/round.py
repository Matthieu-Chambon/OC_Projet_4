from datetime import date


class Round:
    def __init__(self, name):
        self.name = name
        self.matchsList = []
        self.startDate = date.today().strftime("%d/%m/%Y %H:%M:%S")
        self.endDate = None
