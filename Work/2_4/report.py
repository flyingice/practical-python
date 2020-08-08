# report.py
#
# Exercise 2.4
import csv


def read_portfolio(filename):
    portfolio = []
    with open(filename, "rt") as infile:
        csv_reader = csv.reader(infile)
        next(csv_reader)  # skip the headers on the 1st line
        for row in csv_reader:
            portfolio.append((row[0], int(row[1]), float(row[2])))

    return portfolio
