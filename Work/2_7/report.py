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


portfolios = read_portfolio("Work/Data/portfolio.csv")
prices = read_prices("Work/Data/prices.csv")
gain = 0.0
for portfolio in portfolios:
    if portfolio["name"] in prices:
        gain += (prices[portfolio["name"]] - portfolio["price"]) * portfolio["shares"]
    else:
        print("Share {} doesn't exist. Skip.".format(portfolio["name"]))

print(f"{gain:.2f}")
if gain > 0:
    print("You can retire")
else:
    print("You can not retire yet")
