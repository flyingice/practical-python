# Modified based on Exercise 1.32
import csv
import sys


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


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = "Work/Data/portfolio.csv"
cost = portfolio_cost(filename)
print("Total cost", cost)
