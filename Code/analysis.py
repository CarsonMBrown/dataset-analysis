import pandas as pd
import sys
import textwrap
from FileHelper import *

def main():
    for arg in sys.argv[1:] :
        data = readFile(arg)
        if data is not None :
            totalRecords(data)
            rangeOfDate(data)
            recordsByType(data)
            recordsByPercentage(data)
            zenodoByYear(data)

            
def indentDataFrame(toIndent):
    return "\t" + toIndent.to_string().replace("\n", "\n\t") + "\n"


def totalRecords(data):
    print("Number of records:", data.shape[0], "\n")
   

def rangeOfDate(data):
    date_data = pd.to_datetime(data['timestamp'])
    date_data = date_data.sort_values(ascending = True)

    print("Earliest date (ns, UTC):", date_data.iloc[0])
    print("Earliest date:", date_data.iloc[0].date())

    print("Latest date (ns, UTC):", date_data.iloc[-1])
    print("Latest date:", date_data.iloc[-1].date(), "\n")

    
def recordsByType(data):
    counts = data['type'].value_counts()
    # use of value_counts that has been optimised for object type
    table = counts.rename_axis('Record type').reset_index(name = 'Record count')
    print(table, "\n")


def recordsByPercentage(data):
    percent = data['type'].value_counts(normalize = True).mul(100).round(1).astype(str)
    table = percent.rename_axis('Record type').reset_index(name = 'Percentage %')
    print(table, "\n")
    

def zenodoByYear(data):
    zenodo_data = data[data['id'].str.contains('zenodo', case = False)]
    zenodo_data = pd.to_datetime(zenodo_data['timestamp']).dt.year
    counts = zenodo_data.value_counts()
    table = counts.rename_axis('Year').reset_index(name = 'Number of Zenodo cited')
    
    print("Sort by number of citations:\n")
    print(table, "\n")

    print("Sort by year of appearance:\n")
    table = table.sort_values(table.columns[0])
    print(table, "\n")


if __name__ == '__main__':
    main()
