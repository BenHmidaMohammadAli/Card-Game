class Gamer:
    def __init__(self, pseudo):
        self.pseudo = pseudo
        self.score = 0
        self.kaf = []
        self.box_score = []
        self.last_killer = False

    def __str__(self):
        return f"Gamer  : {self.pseudo} -> {self.score}  kaf = {self.kaf}"

    def __repr__(self):
        return f"Gamer  : {self.pseudo} -> {self.score}  kaf = {self.kaf}"

    def set_pseudo(self, pseudo):
        self.pseudo = pseudo

    def set_score(self, score):
        self.score = score

    def set_kaf(self, kaf):
        self.kaf = kaf

    def set_box_score(self, box_score):
        self.box_score = box_score

    def set_last_killer(self, last_killer):
        self.last_killer = last_killer

    # --
    def get_pseudo(self):
        return self.pseudo

    def get_score(self):
        return self.score

    def get_kaf(self):
        return self.kaf

    def get_box_score(self):
        return self.box_score

    def get_last_killer(self):
        return self.last_killer
        # --

    def add_score(self, value):
        self.score = self.score + value

    def minus_score(self, value):
        self.score = self.score - value
