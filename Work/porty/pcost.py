# Modified based on Exercise 1.31
from . import report


def portfolio_cost(filename):
    portfolios = report.read_portfolio(filename)
    return portfolios.total_cost


def main(args):
    if len(args) != 2:
        raise SystemExit("Invalid parametes")
    print("Total cost:", portfolio_cost(args[1]))


if __name__ == "__main__":
    import sys

    main(sys.argv)
