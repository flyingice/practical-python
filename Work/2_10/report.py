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


def read_prices(filename):
    prices = {}
    with open(filename, "rt") as infile:
        rows = csv.reader(infile)
        for row in rows:
            if row:
                prices[row[0]] = float(row[1])

    return prices


def make_report(portfolio: list, prices: dict):
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


def pretty_print(report: list):
    for row in report:
        print(f"{row[0]:10s} {row[1]:10d} {row[2]:10.2f} {row[3]:10.2f}")


portfolios = read_portfolio("Work/Data/portfolio.csv")
prices = read_prices("Work/Data/prices.csv")
report = make_report(portfolios, prices)
pretty_print(report)
