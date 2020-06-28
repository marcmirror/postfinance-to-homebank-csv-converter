# PostFinance to HomeBank CSV converter

A _very_ simple script that converts a PostFinance CSV export containing transactions to a CSV which can be imported to
HomeBank (http://homebank.free.fr). Keep in mind that this script is for my own use and your requirements might be
different.

## Requirements

A working Python 3 installation.

## Usage

Run this in the directory where the PostFinance export file is located:
`python3 converter.py sample_postfinance_export.csv` (Replace *sample_postfinance_export.csv* with the name of your
export).

See the [sample file](./sample_postfinance_export.csv) for how a PostFinance export should look like. There should be no
need to manually edit the PostFinance export.

More information about the HomeBank CSV import can be found [here](http://homebank.free.fr/help/misc-csvformat.html).

## Limitations

The script does not categorize the transactions. Please use the "managing the automatic assignments" tool for this,
which seems to be the easier option anyway.

## Other

The file [postfinance_default_categories.csv](./postfinance_default_categories.csv) contains PostFinance's default
categories (German names). This file can also be imported in HomeBank.
