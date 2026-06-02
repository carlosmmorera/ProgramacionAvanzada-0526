from Clase1.grupo2 import Product

def process_orders(orders: list[dict], inventory: dict) -> None:
    pass



class Order:
    def __init__(self, order_id: str):
        ...

    def add_product(self, product: Product, quantity: int) -> None:
        ...

    def buy(self) -> str:
        ...

    def __repr__(self) -> str:
        ...