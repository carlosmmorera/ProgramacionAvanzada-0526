def check_stock(product: dict, requested_units: int) -> tuple[bool, int]:
    return (True, 0)



class Category:
    def __init__(self, name: str, description: str = ""):
        ...

    def __eq__(self, other) -> bool:
        ...

    def __hash__(self) -> int:
        ...

    def __repr__(self) -> str:
        ...



class Tag:
    def __init__(self, name: str):
        ...

    def __eq__(self, other) -> bool:
        ...

    def __hash__(self) -> int:
        ...

    def __repr__(self) -> str:
        ...