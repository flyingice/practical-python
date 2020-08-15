# Modified based on Exercise 3.1

import fileparse
import stock


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


def print_report(report: list):
    header = ("Name", "Shares", "Price", "Change")
    print(" ".join([f"{h:>10s}" for h in header]))
    print(" ".join(["-" * 10 for h in header]))
    # f-string can be nested
    for row in report:
        print(f"{row[0]:>10s} {row[1]:>10d} {f'${row[2]:.2f}':>10s} {row[3]:10.2f}")


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
