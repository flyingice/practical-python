from follow import follow
import csv


def select_columns(rows, indices):
    for row in rows:
        yield [row[index] for index in indices]


def convert_types(rows, types):
    for row in rows:
        yield [func(val) for func, val in zip(types, row)]


def make_dicts(rows, headers):
    return (dict(zip(headers, row)) for row in rows)


def parse_stock_data(lines):
    rows = csv.reader(lines)
    rows = select_columns(rows, [0, 1, 4])
    rows = convert_types(rows, [str, float, float])
    rows = make_dicts(rows, ["name", "price", "change"])
    return rows


def filter_symbols(rows, names):
    return (row for row in rows if row["name"] in names)


def ticker(portfile, logfile, fmt):
    import report
    import tableformat

    portfolio = report.read_portfolio(portfile)
    rows = parse_stock_data(follow(logfile))
    rows = filter_symbols(rows, portfolio)
    fmt = tableformat.create_formatter(fmt)
    fmt.headings(["Name", "Price", "Change"])
    for row in rows:
        fmt.row([row["name"], str(row["price"]), str(row["change"])])


if __name__ == "__main__":
    import report

    portfolio = report.read_portfolio("Work/Data/portfolio.csv")
    lines = follow("Work/Data/stocklog.csv")
    rows = parse_stock_data(lines)
    rows = filter_symbols(rows, portfolio)
    for row in rows:
        print(row)
