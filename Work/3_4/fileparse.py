# fileparse.py
#
# Modified bases on Exercise 3.3

import csv


def parse_csv(filename: str, select: list = None):
    """
    Parse a CSV file into a list of records
    """
    with open(filename, "rt") as f:
        rows = csv.reader(f)
        # Read the file handlers
        headers = next(rows)

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

            record = dict(zip(headers, row))
            records.append(record)

        return records
