from errors import OutOfStockError
from errors import InvalidDataError
class Product:
    def __init__(self, code: int, name: str, price: int, quantity: int):
        if price <= 0:
            raise InvalidDataError("Nieprawidłowa cena")
        if quantity < 0:
            raise InvalidDataError("Nieprawidłowa ilość")
        self._code = code
        self._name = name
        self._price = price
        self._quantity = quantity

    @property
    def code(self):
        return self._code
    @property
    def name(self):
        return self._name
    @property
    def price(self):
        return self._price
    @property
    def quantity(self):
        return self._quantity

    def decrease_quantity(self):
        if self._quantity <=0:
            raise OutOfStockError("brak wybranego produktu")
        self._quantity -= 1

    def show_what_you_picked(self):
        print(f"You picked {self.name}")
