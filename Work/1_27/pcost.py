# pcost.py
#
# Exercise 1.27

with open("Work/Data/portfolio.csv", "rt") as infile:
    next(infile)  # skip the headers on the 1st line
    total = 0.0
    for portfolio in infile:
        _, shares, price = portfolio.split(",")
        total += int(shares) * float(price)

    print("Total cost", total)
