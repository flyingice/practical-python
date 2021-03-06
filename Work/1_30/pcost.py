# Modified based on Exercise 1.27
def portfolio_cost(filename):
    total = 0.0
    with open(filename, "rt") as infile:
        next(infile)  # skip the headers on the 1st line
        for portfolio in infile:
            _, shares, price = portfolio.split(",")
            total += int(shares) * float(price)
        return total


cost = portfolio_cost("Work/Data/portfolio.csv")
print("Total cost", cost)
