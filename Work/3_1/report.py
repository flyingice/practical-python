# Modified based on Exercise 2.16

import csv


def read_portfolio(filename):
    portfolio = []
    with open(filename, "rt") as infile:
        csv_reader = csv.reader(infile)
        header = next(csv_reader)  # skip the headers on the 1st line
        for row in csv_reader:
            record = dict(zip(header, row))
            portfolio.append(
                {
                    "name": record["name"],
                    "shares": int(record["shares"]),
                    "price": float(record["price"]),
                }
            )

    return portfolio


def read_prices(filename):
    prices = {}
    with open(filename, "rt") as infile:
        rows = csv.reader(infile)
        for row in rows:
            if row:
                prices[row[0]] = float(row[1])

    return prices


def make_report(portfolios: list, prices: dict):
    report = []
    for stock in portfolios:
        if stock["name"] in prices:
            report.append(
                (
                    stock["name"],
                    stock["shares"],
                    prices[stock["name"]],
                    prices[stock["name"]] - stock["price"],
                )
            )
        else:
            print("Share {name} doesn't exist. Skip".format_map(stock))

    return report


def print_header(header: tuple):
    print(" ".join([f"{h:>10s}" for h in header]))


def print_separator(header: tuple):
    print(" ".join(["-" * 10 for h in header]))


def print_report(report: list):
    # f-string can be nested
    for row in report:
        print(f"{row[0]:10s} {row[1]:10d} {f'${row[2]:.2f}':>10s} {row[3]:10.2f}")


portfolios = read_portfolio("Work/Data/portfoliodate.csv")
prices = read_prices("Work/Data/prices.csv")
report = make_report(portfolios, prices)

headers = ("Name", "Shares", "Price", "Change")
print_header(headers)
print_separator(headers)
print_report(report)
