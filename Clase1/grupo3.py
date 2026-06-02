from Clase1.grupo2 import Product

def show_inventory_report(inventory: dict) -> None:
    pass


class Inventory:
    def __init__(self):
        ...

    def add_product(self, product: Product) -> None:
        ...

    def get_product(self, sku: str) -> Product | None:
        ...

    def generate_inventory_report(self) -> str:
        ...

    def __repr__(self) -> str:
        ...