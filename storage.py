from product import Product
from errors import FileProblemError, InvalidDataError

class Storage:
    def __init__(self, filename="list.txt"):
        self._products = {}

        with open(filename,"r",encoding="utf-8") as plik:
            for line in plik:
                if line.strip() == "":
                    continue
                try:
                    #usunięcie spacje i znak końca linii, podzielenie tekstu tam, gdzie są przecinki
                    code, name, price, quantity = line.strip().split(",")
                    product = Product(int(code), name, int(price), int(quantity))
                except(ValueError, InvalidDataError):
                    raise FileProblemError(f"Błąd w linijce {line}")
                if product.code in self._products:
                    raise FileProblemError(f"Powtórzony kod w linii {line}")
                self._products[int(code)] = product

    def print_storage(self):
        print("AUTOMAT Z NAPOJAMI")
        for product in self._products.values():
            #cena w groszach więc podzielenei przez 100
            print(f"[{product.code}] {product.name} - {product.price/100:.2f} zł (Sztuki: {product.quantity})")

    def get_product(self, code:int):
        return self._products.get(code)
