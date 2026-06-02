from grupo2 import Product
from grupo2 import update_stock

def process_orders(orders: list[dict], inventory: dict) -> None:
    for order in orders:
        items = order['items']

        for sku, quantity in items.items():
            if sku in inventory:
                product = inventory[sku]

                inventory[sku] = update_stock(product, quantity)



class Order:
    def __init__(self, order_id: str):
        ...

    def add_product(self, product: Product, quantity: int) -> None:
        ...

    def buy(self) -> str:
        ...

    def __repr__(self) -> str:
        ...