# fileparse.py
#
# Modified bases on Exercise 3.6

import csv


def parse_csv(
    filename: str,
    select: list = None,
    types: list = None,
    has_headers: bool = True,
    delimiter: str = ",",
):
    """
    Parse a CSV file into a list of records
    """
    with open(filename, "rt") as f:
        rows = csv.reader(f, delimiter=delimiter)
        # Read the file handlers
        headers = next(rows) if has_headers else []

        if select:
            indices = [headers.index(colname) for colname in select]
            headers = select
        else:
            indices = []

        records = []
        for row in rows:
            if not row:  # Skip rows with no data
                continue

            if indices:
                row = [row[index] for index in indices]

            if types:
                row = [func(val) for func, val in zip(types, row)]

            if headers:
                record = dict(zip(headers, row))
            else:
                record = tuple(row)
            records.append(record)

        return records
