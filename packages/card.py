class Card:
    def __init__(self, symbol, value):
        self.symbol = symbol
        self.value = value
        self.img = "null"

    def __str__(self):
        return f"card is : {self.symbol} -> {self.value} "

    def __repr__(self):
        return f"card is : {self.symbol} -> {self.value} "

    @property
    def symbol(self):
        return self.symbol

    @property
    def value(self):
        return self.value
