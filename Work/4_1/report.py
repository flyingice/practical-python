# Modified based on Exercise 3.1

import fileparse
import stock
import tableformat


def read_portfolio(filename):
    with open(filename, "rt") as infile:
        portfolios = fileparse.parse_csv(
            infile, select=["name", "shares", "price"], types=[str, int, float]
        )

    portfolios = [stock.Stock(d["name"], d["shares"], d["price"]) for d in portfolios]
    return portfolios


def read_prices(filename):
    with open(filename, "rt") as infile:
        return dict(fileparse.parse_csv(infile, types=[str, float], has_headers=False))


def make_report(portfolios: list, prices: dict):
    report = []
    for portfolio in portfolios:
        report.append(
            (
                portfolio.name,
                portfolio.shares,
                prices[portfolio.name],
                prices[portfolio.name] - portfolio.price,
            )
        )

    return report


def print_report(report: list, formatter: tableformat.TableFormatter):
    """Print a nicely formated table from a list"""
    formatter.headings(["Name", "Shares", "Price", "Change"])
    for name, shares, price, change in report:
        rowdata = [name, str(shares), f"{price:.2f}", f"{change:.2f}"]
        formatter.row(rowdata)


def portfolio_report(portfolio_filename: str, prices_filename: str, fmt: str = "txt"):
    portfolios = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    report = make_report(portfolios, prices)
    formatter = tableformat.create_formatter(fmt)
    print_report(report, formatter)


def main(args):
    if len(args) != 3:
        raise SystemExit("Invalid parameters")
    portfolio_report(args[1], args[2])


if __name__ == "__main__":
    import sys

    main(sys.argv)
