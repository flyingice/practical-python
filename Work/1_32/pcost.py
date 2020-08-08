# Modified based on Exercise 1.31
import csv


def portfolio_cost(filename):
    total = 0.0
    with open(filename, "rt") as infile:
        csv_reader = csv.reader(infile)
        next(csv_reader)  # skip the headers on the 1st line
        for portfolio in csv_reader:
            try:
                total += int(portfolio[1]) * float(portfolio[2])
            except (csv.Error, ValueError):
                print("Bad line. Skip.")
        return total


cost = portfolio_cost("Work/Data/portfolio.csv")
print("Total cost", cost)
