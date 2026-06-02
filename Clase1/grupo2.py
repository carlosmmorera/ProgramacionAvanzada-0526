from typing import Optional
from grupo1 import check_stock


def update_stock(product: dict, sold_units: int) -> dict:

    if product is None:
        print(f"Error: Product not found.")
        return {}
    
    enough_stock, verified_sold_units = check_stock(product, sold_units)
    if enough_stock:
        product["current_stock"]=product["current_stock"]-verified_sold_units
    else:
        print(f"Error: Insufficient stock for {product['name']}. Available: {product['current_stock']}, Requested: {sold_units}")

    return product



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

product = {"name": "Laptop", "sku": "SKU123", "price": 1200, "current_stock": 10, 
           #"categories": [categories[0]], "tags": [tags[1], tags[2]]
           }
print (product)
product=update_stock(product,2)

print (product)
