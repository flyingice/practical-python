# Modified based on Exercise 3.1

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


def print_report(report: list):
    header = ("Name", "Shares", "Price", "Change")
    print(" ".join([f"{h:>10s}" for h in header]))
    print(" ".join(["-" * 10 for h in header]))
    # f-string can be nested
    for row in report:
        print(f"{row[0]:10s} {row[1]:10d} {f'${row[2]:.2f}':>10s} {row[3]:10.2f}")


def portfolio_report(portfolio_filename: str, prices_filename: str):
    portfolios = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    report = make_report(portfolios, prices)
    print_report(report)


def main(args):
    if len(args) != 3:
        raise SystemExit("Invalid parameters")
    portfolio_report(args[1], args[2])


if __name__ == "__main__":
    import sys

    main(sys.argv)
