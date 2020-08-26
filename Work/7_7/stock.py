from typedproperty import typedproperty


class Stock:
    name = typedproperty("name", str)
    shares = typedproperty("shares", int)
    price = typedproperty("price", float)

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
