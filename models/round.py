from datetime import datetime


class Round:
    def __init__(self, name):
        self.name = name
        self.matchsList = []
        self.startDate = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.endDate = None

    def to_dict(self):
        return {
            "name": self.name,
            "matchsList": [match.to_dict() for match in self.matchsList],
            "startDate": self.startDate,
            "endDate": self.endDate
        }
