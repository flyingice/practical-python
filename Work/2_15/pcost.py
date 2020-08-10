# Modified based on Exercise 1.31
import csv


def portfolio_cost(filename):
    total = 0.0
    with open(filename, "rt") as infile:
        rows = csv.reader(infile)
        next(rows)  # skip the headers on the 1st line
        for lineno, row in enumerate(rows, start=1):
            try:
                total += int(row[1]) * float(row[2])
            except ValueError:
                print(f"Row {lineno}: Couldn't convert: {row}")

    return total


cost = portfolio_cost("Work/Data/missing.csv")
print("Total cost", cost)
