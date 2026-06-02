from Clase1.grupo2 import Product


def show_inventory_report(inventory: dict) -> None:
    print("\nInventory Report:\n")
    for product in inventory.values():
        categories = product.get("categories") or []
        tags = product.get("tags") or []
        category_names = ", ".join(cat.get("name", "") for cat in categories) or "None"
        tag_names = ", ".join(tag.get("name", "") for tag in tags) or "None"
        print(f"Product: {product['name']} (SKU: {product['sku']}) - Price: ${product['price']:.2f}, Stock: {product['current_stock']}, Categories: [{category_names}], Tags: [{tag_names}]")



class Inventory:
    def __init__(self):
        pass

    def add_product(self, product: Product) -> None:
        pass

    def get_product(self, sku: str) -> Product | None:
        pass

    def generate_inventory_report(self) -> str:
        pass

    def __repr__(self) -> str:
        pass

