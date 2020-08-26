import typedproperty


class Stock:
    name = typedproperty.String("name")
    shares = typedproperty.Integer("shares")
    price = typedproperty.Float("price")

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
