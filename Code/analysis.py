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
            data = CleanData.refineData(data)
            CleanData.checkData(data)

            print("\n--- Beginning of Initial Analysis ---\n")

            totalRecords(data)
            rangeOfDate(data)
            recordsByType(data)

            print("--- End of Initial Analysis ---\n")
            print("--- Beginning of Easy Extensions ---\n")

            recordsByPercentage(data)
            avgDaysSinceCitation(data)
            arxivCitations(data)

            print("--- End of Easy Extensions ---\n")
            print("--- Beginning of Medium Extensions ---\n")

            avgCitatations(data)
            zenodoByYear(data)
            tenLargestPagesBySources(data)

            print("--- End of Medium Extensions ---\n")
            print("--- Beginning of Hard Extensions ---\n")

            mostCommonCitations(data)
            numberAndPercentageOfCitations(data)

            print("--- End of Hard Extensions ---\n")


def indentDataFrame(toIndent):
    """Helper Function For Use in Formatting."""
    return "\t" + toIndent.to_string().replace("\n", "\n\t") + "\n"


def indentWithoutIndex(toIndent):
    """Helper Function For Use in Formatting"""
    return "\t" + toIndent.to_string(index = False).replace("\n", "\n\t") + "\n"

def totalRecords(data):
    """Basic: Outputting number of records after pre-processing"""
    print("Number of records:", data.shape[0], "\n")


def rangeOfDate(data):
    """Basic: Outputting the range of date"""
    date_data = data['timestamp']
    date_data = date_data.sort_values(ascending = True)

    print("The Range of Dates Represented in the Data:")

    print("\tEarliest date (ns, UTC):", date_data.iloc[0])
    print("\tEarliest date:", date_data.iloc[0].date())

    print("\tLatest date (ns, UTC):", date_data.iloc[-1])
    print("\tLatest date:", date_data.iloc[-1].date(), "\n")


def recordsByType(data):
    """Basic: Sort records by citation type"""
    counts = data['type'].value_counts()
    # use of value_counts that has been optimised for object type
    table = counts.rename_axis('Record type').reset_index(name = 'Record count')

    print("Records By Type: ")
    print(indentWithoutIndex(table))


def recordsByPercentage(data):
    """Easy: Outputting percentage of each record type"""
    percent = data['type'].value_counts(normalize = True).mul(100).round(1).astype(str) # normalize parameter calculates percentage as a decimal number
    table = percent.rename_axis('Record type').reset_index(name = 'Percentage %')
    print("Percent of Records for Each Citation Type:")
    print(indentWithoutIndex(table))


def arxivCitations(data):
    """Easy: Output a table with the number of citations from arXiv by the year of their appearance."""
    arxivCitations = data.query("type == \"arxiv\"")
    onlyYears = arxivCitations["timestamp"].dt.year
    yearCounts = onlyYears.value_counts()
    print("Number Of ArXiv Citations By Year: ")
    print(indentDataFrame(yearCounts))


def avgDaysSinceCitation(data):
    """Easy: Calcuate average number od days since citation apppeared on Wikipedia"""
    average_date = data.timestamp.mean()
    average_difference = datetime.datetime(2018, 3, 1) - average_date.tz_localize(None)
    print("The Average Number Of Days Since A Citation Was Added Is: " + str(average_difference.days), "\n")


def zenodoByYear(data):
    """Medium: Outputting citations referencing Zenodo by year"""
    zenodo_data = data[data['id'].str.contains('zenodo', case = False)]  # This make sure all letter cases are included.
    zenodo_data = pd.to_datetime(zenodo_data['timestamp']).dt.year
    counts = zenodo_data.value_counts()
    table = counts.rename_axis('Year').reset_index(name = 'Number of Zenodo cited')  # Rename axis name of output table

    print("Number of Citations from Zenodo: ")
    print("\tSorted by Number of Citations:")
    print(indentWithoutIndex(table))

    print("\tSorted by Year of Appearance:")
    table = table.sort_values(table.columns[0])
    print(indentWithoutIndex(table))


def avgCitatations(data):
    """Medium: Find an average number of citations per page."""
    valueCount = data["page_id"].value_counts()
    mean = valueCount.mean()
    median = valueCount.median()
    print("Average Citations:")
    print("\tMean:   " + str(mean))
    print("\tMedian: " + str(median), "\n")


def tenLargestPagesBySources(data):
    """Medium: Ten pages citing the largest number of sources"""
    title_group_counts = data.groupby('page_title').count()
    ten_largest = title_group_counts.nlargest(10, 'timestamp').index.values
    print("The First 10 Pages Citing The Largest Number of Sources Are:")
    for values in ten_largest:
        print("\t" + values)
    print()


def numberAndPercentageOfCitations(data):
    """Hard: Output a table with number and percentage of citations by number of years"""
    citations_by_year = data.groupby(data.timestamp.dt.year).count()
    citations_by_year = citations_by_year['id']
    citations_by_year = citations_by_year.to_frame()
    citations_by_year.index.name = 'Years'
    citations_by_year = citations_by_year.rename(columns={'id': 'Citations'})
    total_citations = citations_by_year['Citations'].sum()
    citations_by_year['Percentage'] = citations_by_year.apply(
        lambda x: citations_by_year['Citations'] * 100 / total_citations)
    print("The Number and Percentage of Citations Added Per Year:")
    print(indentDataFrame(citations_by_year))


def toUpper(s):
    """Helper function: allows for a whole list to be converted to uppercase using the .apply() function in the mostCommonCitations() function."""
    return s.upper()


def mostCommonCitations(data):
    """Hard: Find first ten most highly cited sources (for the given language version)."""
    print("The 10 Most Cited Sources Are: ")
    citations = data["type"].apply(toUpper) + " " + data["id"]
    citationCount = citations.value_counts().head(10)
    print(indentDataFrame(citationCount))


if __name__ == '__main__':
    main()
