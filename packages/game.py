class Game:
    def __init__(self, list_gamers, score_max, level):
        self.list_gamers = list_gamers
        self.list_cards_louta = []
        self.score_max = score_max
        self.level = level

    def __str__(self):
        return f"Game  : list gamers : {self.list_gamers} liste Carta louta : {self.list_carte_louta}  score = {self.score_max} level = {self.level}"

    def __repr__(self):
        return f"Game  : {self.list_gamers} -> {self.list_carte_louta}  score = {self.score_max} level = {self.level}"

    @property
    def list_gamers(self):
        return self.list_gamers

    @list_gamers.setter
    def list_gamers(self, value):
        self.list_gamers = value

    @property
    def list_cards_louta(self):
        return self.list_cards_louta

    @list_cards_louta.setter
    def list_cards_louta(self, value):
        self.list_gamers = value

    @property
    def score_max(self):
        return self.score_max

    @score_max.setter
    def score_max(self, value):
        self.score_max = value

    @property
    def level(self):
        return self.level

    @level.setter
    def level(self, value):
        self.level = value
