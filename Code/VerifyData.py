import pandas as pd
import sys
from fileHelper import *

def main():
    for arg in sys.argv[1:] :
        data = readFile(arg)
        if data is not None :
            removeDuplicates(data)
            removeNullData(data)
            checkTypes(data)
            checkRangesValid(data)


def removeDuplicates(data):
    """
    Removes any duplicates from the data. Displays the number of duplicate lines that were removed.
    """
    newRows = data.drop_duplicates().shape[0]
    dataRows = data.shape[0]
    print("There are " + str(dataRows - newRows) + " Duplicate Rows in the Data")


def removeNullData(data):
    """
    Removes any lines with missing data and displays the number of lines that were removed.
    """
    numRows = data.shape[0]
    data.dropna(inplace=True)
    print(str(numRows - data.shape[0]) + " Lines with missing data removed")


def checkTypes(data):
    """
    Checks that the types of each column are correct and displays the name of any column that does not
    contain the correct type.
    """
    allValid = True
    for i in range(0,6) :
        if i == 0 or i == 2 :
            if data.dtypes[i] != "int64" :
                print("Column \"" + data.columns[i] + "\" Contains Invalid Type")
                allValid = False
        else :
            if data.dtypes[i] != "object" :
                print("Column \"" + data.columns[i] + "\" Contains Invalid Type")
                allValid = False
    if allValid :
        print("All Data Is Of The Correct Type")



# Can be expanded to each row with a new list of valid types or a new range
def checkRangesValid(data):
    """
    Checks that the range of values in each column is valid.
    """
    invalidData = data.query("type not in [\"doi\", \"isbn\", \"pmid\", \"pmc\", \"arxiv\"]")
    if invalidData.shape[0] != 0 :
        print("Invalid Type(s) Found, Removing Lines:")
        print(invalidData)
    else :
        print("No Invalid Data Found")
    data = data.query("type in [\"doi\", \"isbn\", \"pmid\", \"pmc\", \"arxiv\"]")


if __name__ == '__main__':
    main()
