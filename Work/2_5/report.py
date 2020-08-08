# report.py
#
import csv


def read_portfolio(filename):
    portfolio = []
    with open(filename, "rt") as infile:
        csv_reader = csv.reader(infile)
        next(csv_reader)  # skip the headers on the 1st line
        for row in csv_reader:
            portfolio.append(
                {"name": row[0], "shares": int(row[1]), "price": float(row[2])}
            )

    return portfolio
