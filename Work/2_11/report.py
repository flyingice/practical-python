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
    # f-string can be nested
    for row in report:
        print(f"{row[0]:10s} {row[1]:10d} {f'${row[2]:.2f}':>10s} {row[3]:10.2f}")


def create_header(header: list):
    return " ".join([f"{h:>10s}" for h in header])


def create_separator(header: list):
    return " ".join(["-" * 10 for h in header])


portfolios = read_portfolio("Work/Data/portfolio.csv")
prices = read_prices("Work/Data/prices.csv")
report = make_report(portfolios, prices)

headers = ["Name", "Shares", "Price", "Change"]
print(create_header(headers))
print(create_separator(headers))
pretty_print(report)
