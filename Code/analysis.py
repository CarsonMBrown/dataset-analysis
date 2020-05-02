import pandas as pd
import sys
import textwrap
import datetime
import CleanData
from FileHelper import *


def main():
    for arg in sys.argv[1:]:
        data = readFile(arg)
        if data is not None:
            CleanData.refineData(data)
            CleanData.checkData(data)
            # totalRecords(data)
            # rangeOfDate(data)
            # recordsByType(data)
            # recordsByPercentage(data)
            # zenodoByYear(data)
            avgDaysSinceCitation(data)


def indentDataFrame(toIndent):
    return "\t" + toIndent.to_string().replace("\n", "\n\t") + "\n"


def totalRecords(data):
    """Basic: Outputting number of records after pre-processing"""
    print("Number of records:", data.shape[0], "\n")


def rangeOfDate(data):
    """Basic: Outputting the range of date"""
    date_data = pd.to_datetime(data['timestamp'])  # Parse the column 'timestamp' as datatime type in Pandas
    date_data = date_data.sort_values(ascending=True)

    print("Earliest date (ns, UTC):", date_data.iloc[0])
    print("Earliest date:", date_data.iloc[0].date())

    print("Latest date (ns, UTC):", date_data.iloc[-1])
    print("Latest date:", date_data.iloc[-1].date(), "\n")


def recordsByType(data):
    """Basic: Sort records by citation type"""
    counts = data['type'].value_counts()
    # use of value_counts that has been optimised for object type
    table = counts.rename_axis('Record type').reset_index(name='Record count')
    print(table, "\n")


def recordsByPercentage(data):
    """Easy: Outputting percentage of each record type"""
    percent = data['type'].value_counts(normalize=True).mul(100).round(1).astype(
        str)  # normalize parameter calculates percentage as a decimal number
    table = percent.rename_axis('Record type').reset_index(name='Percentage %')
    print(table, "\n")


def zenodoByYear(data):
    """Medium: Outputting citations referencing Zenodo by year"""
    zenodo_data = data[data['id'].str.contains('zenodo', case=False)]  # This make sure all letter cases are included.
    zenodo_data = pd.to_datetime(zenodo_data['timestamp']).dt.year
    counts = zenodo_data.value_counts()
    table = counts.rename_axis('Year').reset_index(name='Number of Zenodo cited')  # Rename axis name of output table

    print("Sort by number of citations:\n")
    print(table, "\n")

    print("Sort by year of appearance:\n")
    table = table.sort_values(table.columns[0])
    print(table, "\n")


def avgDaysSinceCitation(data):
    average_date = data.timestamp.mean()
    average_difference = datetime.datetime(2018, 3, 1) - average_date.tz_localize(None)
    print("Average days since citation are " + str(average_difference.days))


if __name__ == '__main__':
    main()
