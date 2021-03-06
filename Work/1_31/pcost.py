# Modified based on Exercise 1.30
def portfolio_cost(filename):
    total = 0.0
    with open(filename, "rt") as infile:
        next(infile)  # skip the headers on the 1st line
        for portfolio in infile:
            _, shares, price = portfolio.split(",")
            try:
                total += int(shares) * float(price)
            except ValueError:
                print("Bad line. Skip.")
        return total


cost = portfolio_cost("Work/Data/missing.csv")
print("Total cost", cost)
