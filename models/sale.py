from datetime import datetime


class Sale:
    def __init__(self, price: float, product: str, date: str):
        self.date = date
        self.price = price
        self.product = product

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        float(price)
        if price < 0:
            raise ValueError('Price cannot be negative')
        self._price = price

    @property
    def product(self):
        return self._product

    @product.setter
    def product(self, product):
        if not product.isalpha():
            raise ValueError('Only characters, no accents')
        else:
            self._product = product

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, date):
        datetime.strptime(date, '%d/%m/%Y')
        self._date = date

    def __repr__(self) -> str:
        class_type = type(self).__name__
        return (
            f"{class_type}"
            f"date={self.date},\n"
            f"price={self.price},\n"
            f"product={self.product},\n"
            )
         