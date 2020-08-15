class TableFormatter:
    def headings(self, headers: list):
        """Emit the table headings."""
        raise NotImplementedError()

    def row(self, rowdata):
        """Emit a single row of table data."""
        raise NotImplementedError()


class TextTableFormatter(TableFormatter):
    """Emit a table in plain-text format"""

    def headings(self, headers: list):
        for h in headers:
            print(f"{h:>10s}", end=" ")
        print()
        print(("-" * 10 + " ") * len(headers))

    def row(self, rowdata):
        for d in rowdata:
            print(f"{d:>10s}", end=" ")
        print()


class CSVTableFormatter(TableFormatter):
    """Output portfolio data in CSV format."""

    def headings(self, headers: list):
        print(",".join(headers))

    def row(self, rowdata):
        print(",".join(rowdata))


class HTMLTableFormatter(TableFormatter):
    """Output portfolio data in HTML format."""

    def headings(self, headers: list):
        print(
            "<tr>{}</tr>".format(
                "".join(["<th>" + colname + "</th>" for colname in headers])
            )
        )

    def row(self, rowdata):
        print(
            "<tr>{}</tr>".format(
                "".join(["<td>" + coldata + "</td>" for coldata in rowdata])
            )
        )