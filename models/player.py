
class Player:
    """Player class"""

    def __init__(self, alias_name):
        self._alias_name = alias_name
        self._price = 0
        self._level_achived = 0
        self._current_level = 1
   
    def set_alias(self, alias):
        self._alias = alias

    def get_alias(self):
        return self._alias_name

    def set_price(self, price):
        self._price += price

    def get_price(self):
        return self._price

