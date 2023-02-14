from exceptions import (
    NoCoinException,
    NoElementsException,
    NoSugarException)
 

class CoffeeMachine:
    def __init__(self):
        self.coins = 0
        self.coffee = 0
        self.sugar = 0

    def insert_coin(self):
        self.coins += 1

    def insert_coffee(self, coffee):
        self.coffee += coffee

    def insert_sugar(self, sugar):
        self.sugar += sugar

    def get_coffee(self):
        if self.coins == 0:
            raise NoCoinException('No hay monedas')
        if self.count_coffee_left() == 0:
            raise NoElementsException('No hay elementos')
        # DESCONTAR
        self.coffee -= 30
        self.sugar -= 5
        self.coins -= 1
        return True

    def count_coffee_left(self):
        count_coffee_because_coffee = self.coffee // 30
        count_coffee_because_sugar = self.sugar // 5
        return min(count_coffee_because_coffee, count_coffee_because_sugar)


