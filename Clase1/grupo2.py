from typing import Optional

def update_stock(product: dict, sold_units: int) -> dict:
    return {}



class Product:
    def __init__(self, name: str, sku: str, price: float, current_stock: int = 0,
                 categories: Optional[list] = None, tags: Optional[list] = None):
        ...

    def check_stock(self, requested_units: int) -> tuple[bool, int]:
        ...

    def update_stock(self, amount: int) -> None:
        ...

    def get_info(self) -> str:
        ...

    def __repr__(self) -> str:
        ...

        ...