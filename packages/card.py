class Card:
    def __init__(self, symbol, value):
        self._symbol = symbol
        self._value = value
        self._img = "null"

    def __str__(self):
        return f"card is : {self.symbol} -> {self.value} "

    def __repr__(self):
        return f"card is : {self.symbol} -> {self.value} "

    @property
    def symbol(self):
        return self._symbol

    @property
    def value(self):
        return self._value
