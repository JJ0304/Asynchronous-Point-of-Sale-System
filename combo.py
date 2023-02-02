class Combo:
    DISCOUNT = 0.15

    def __init__(self, burger, side, drink):
        self.burger = burger
        self.side = side
        self.drink = drink
        self.price = self._calculate_price()