class Product:
    def __init__(self, name: str, category: str, price: int):
        self.name = name
        self.category = category
        self.price = price
        self.sale = 0

    def edit_category(self, new_category: str):
        self.category = new_category

    def edit_price(self, new_price: float):
        self.price = new_price

    def set_sale(self, sale: int):
        self.sale = sale

    def cancel_sale(self):
        self.sale = 0

    def get_price(self) -> float:
        return self.price * (1 - self.sale / 100)

    def __repr__(self):
        return "Product<name={}, category={}, price={}, sale={}%>".format(self.name, self.category, self.price, self.sale)
