class Sale:
    def __init__(self, custumer: str, price: float, product: str, date: str):
        self.date = date
        self.custumer = custumer
        self.price = price
        self.product = product

    def __repr__(self) -> str:
        class_type = type(self).__name__
        return (
            f"{class_type} custurmer={self.custumer},\n"
            f"date={self.date},\n"
            f"price={self.price},\n"
            f"product={self.product},\n"
            )
