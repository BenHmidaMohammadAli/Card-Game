class Gamer:
    def __init__(self, pseudo):
        self._pseudo = pseudo
        self._score = 0
        self._kaf = []
        self._box_score = []
        self._last_killer = False

    def __str__(self):
        return f"Gamer  : {self.pseudo} -> {self.score}  kaf = {self.kaf}"

    def __repr__(self):
        return f"Gamer  : {self.pseudo} -> {self.score}  kaf = {self.kaf}"

    @property
    def pseudo(self):
        return self._pseudo
    
    @pseudo.setter
    def pseudo(self, value):
        self._pseudo = value

    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, value):
        self._score = value

    @property
    def kaf(self):
        return self._kaf
    
    @kaf.setter
    def kaf(self, value):
        self._kaf = value

    @property
    def box_score(self):
        return self._box_score

    @box_score.setter
    def box_score(self, value):
        self._box_score = value

    @property
    def last_killer(self):
        return self._last_killer
    
    @last_killer.setter
    def last_killer(self, value):
        self._last_killer = value

    def add_score(self, value):
        self.score = self.score + value

    def minus_score(self, value):
        self.score = self.score - value
