class Stock:
    def __init__(self, name: str, shares: int, price: float):
        self.name = name
        self.shares = shares
        self.price = price

    def __repr__(self):
        """The convention for __repr__() os to return a string that, when fed to eval(),
        will create the underlying object, if possible."""
        return f"Stock({self.name}, {self.shares}, {self.price})"

    def cost(self):
        return self.shares * self.price

    def sell(self, sold: int):
        self.shares -= sold
