# fileparse.py
#
# Modified bases on Exercise 3.10

import csv


def parse_csv(
    infile,
    select: list = None,
    types: list = None,
    has_headers: bool = True,
    delimiter: str = ",",
    silence_errors: bool = False,
):
    """
    Parse a CSV file into a list of records
    """

    # Sanity checks on the paramters
    if select and not has_headers:
        raise RuntimeError("select argument requires column headers")

    rows = csv.reader(infile, delimiter=delimiter)
    # Read the file handlers
    headers = next(rows) if has_headers else []

    if select:
        indices = [headers.index(colname) for colname in select]
        headers = select
    else:
        indices = []

    records = []
    for lineno, row in enumerate(rows, start=1):
        try:
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
        except ValueError as e:
            if not silence_errors:
                print(f"Row {lineno}: Couldn't convert {row}")
                print("Reason", e)

    return records
