import csv


def read_prices(filename):
    d = {}
    with open(filename, "rt") as infile:
        rows = csv.reader(infile)
        for row in rows:
            if row:
                d[row[0]] = float(row[1])

    return d
