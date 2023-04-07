class Game:
    def __init__(self, list_gamers, score_max, level):
        self._list_gamers = list_gamers
        self._list_cards_louta = []
        self._score_max = score_max
        self._level = level

    def __str__(self):
        return f"Game  : list gamers : {self._list_gamers} liste Carta louta : {self._list_cards_louta}  score = {self._score_max} level = {self._level}"

    def __repr__(self):
        return f"Game  : {self._list_gamers} -> {self._list_cards_louta}  score = {self._score_max} level = {self._level}"

    @property
    def list_gamers(self):
        return self._list_gamers

    @list_gamers.setter
    def list_gamers(self, value):
        self._list_gamers = value

    @property
    def list_cards_louta(self):
        return self._list_cards_louta

    @list_cards_louta.setter
    def list_cards_louta(self, value):
        self._list_cards_louta = value

    @property
    def score_max(self):
        return self._score_max

    @score_max.setter
    def score_max(self, value):
        self._score_max = value

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, value):
        self._level = value
