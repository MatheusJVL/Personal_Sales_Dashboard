class Sale:
    def __init__(self, price: float, product: str, date: str):
        self.date = date
        self.price = price
        self.product = product

    def __repr__(self) -> str:
        class_type = type(self).__name__
        return (
            f"{class_type}"
            f"date={self.date},\n"
            f"price={self.price},\n"
            f"product={self.product},\n"
            )
