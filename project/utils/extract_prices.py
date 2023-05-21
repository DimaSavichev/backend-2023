from models.product import Product


def extract_prices(products: list[Product]) -> list[float]:
    return list(map(lambda x: x.get_price(), products))
