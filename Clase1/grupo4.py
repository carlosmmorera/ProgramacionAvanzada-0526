from Clase1.grupo2 import Product

def process_orders(orders: list[dict], inventory: dict) -> None:
    for order in orders:
        order_id = order['order_id']
        items = order['items']
        order_instance = Order(order_id)    

        for sku, quantity in items:
            if sku in inventory:
                product = inventory[sku]
                
                if product.current_stock >= quantity:
                    order_instance.add_product(product, quantity)
                    product.current_stock -= quantity
                    product.price *= quantity
                    total += product["price"] * quantity
                    print(f"Order ID: {order_id} - Total: ${total:.2f} - Purchase Completed")
                else:
                    print(f"Error, no hay stock suficiente para el producto {product.name}")




class Order:
    def __init__(self, order_id: str):
        ...

    def add_product(self, product: Product, quantity: int) -> None:
        ...

    def buy(self) -> str:
        ...

    def __repr__(self) -> str:
        ...