import csv
import sys
from itertools import islice

input_csv_filename = sys.argv[1]

number_of_written_transactions = 0

# pf (short for PostFinance)
tags = f'pf'

with open(input_csv_filename, 'r', encoding='utf-8') as input_csv:
    csv_reader = csv.reader(input_csv, delimiter=';')

    with open('OUTPUT.csv', 'w') as output_csv:
        csv_writer = csv.writer(output_csv, delimiter=';', quoting=csv.QUOTE_NONE)

        # Ignore the first 7 lines (because they are not transactions)
        for row in islice(csv_reader, 7, None):
            # If the row is not a valid transaction, skip it
            if len(row) < 5:
                continue

            # Columns in the output CSV (http://homebank.free.fr/help/misc-csvformat.html):
            # date, payment, info, payee, memo, amount, category, tags
            if row[2].strip():
                # Income
                csv_writer.writerow([row[0], 0, '', '', row[1], row[2], '', tags])
            else:
                # Expense
                csv_writer.writerow([row[0], 0, '', '', row[1], row[3], '', tags])
            number_of_written_transactions += 1

print("Number of written transactions: " + str(number_of_written_transactions))
