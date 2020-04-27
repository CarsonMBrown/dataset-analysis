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
            recordsByPercentage(data) # Easy 1

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
    table = pd.DataFrame({'Records count': counts})
    print(table, "\n")


def recordsByPercentage(data):
    percent = data['type'].value_counts(normalize = True).mul(100).round(1).astype(str)
    table = pd.DataFrame({'percentage %': percent})
    print(table, "\n")
    

if __name__ == '__main__':
    main()
