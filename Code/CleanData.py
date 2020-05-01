import sys
import os
from FileHelper import *
import difflib


def main():
    for arg in sys.argv[1:]:
        data = readFile(arg)
        if data is not None:
            checkNumberOfCols(data)
            handleEmptyValues(data)
            removeDuplicates(data)


def checkNumberOfCols(data):
    i = 0
    for key in data.keys():
        i = i + 1
    if i == 6:
        return True
    print("Invalid number of columns")
    return False


def handleEmptyValues(data):
    # Get columns with empty cells
    num_of_empty_in_col = data.isnull().sum()
    num_of_empty_in_col = num_of_empty_in_col[num_of_empty_in_col != 0]
    if not num_of_empty_in_col.empty:
        print("The following columns have empty fields")
        print(num_of_empty_in_col)
        for key in num_of_empty_in_col.keys():
            if data[key].dtype == 'object':
                data[key].fillna('*')
            if data[key].dtype == 'int64':
                data[key].dropna()

def removeDuplicates(data):
    data.drop_duplicates(data)

if __name__ == '__main__':
    main()

# def cleanInvalidLines(filename):
#     """
#     Removes all the invalid lines from the data.
#     """
#     filepath = "../Data/" + filename + ".tsv"
#     if fileValid(filepath) :
#         print("Cleaning Invalid Lines From: " + filepath)
#         file = open(filepath, "r", encoding='utf8')
#         checkTabs(file)
#
# def checkTabs(file):
#     """
#     Checks for lines that don't contain the correct number of tabs.
#     """
#     print("Checking Tabs...")
#     count = 0
#     for line in file.readlines():
#         line = line.strip()
#         numTabs = line.count("\t")
#         if numTabs != 5 :
#             print("\tInvalid Number Of Tabs On Line: ", count)
#         count = count + 1
