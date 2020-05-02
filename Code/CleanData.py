import sys
import os
from FileHelper import *
import difflib


def main():
    for arg in sys.argv[1:]:
        data = readFile(arg)
        if data is not None:
            checkData(data)
            refineData(data)


def checkData(data):
    x = checkNumberOfCols(data)
    x = x and checkColNames(data)
    x = x and checkTypes(data)
    if not x:
        sys.exit(1)


def checkColNames(data):
    col_names = ['page_id', 'page_title', 'rev_id', 'timestamp', 'type', 'id']
    x = True
    for name in col_names:
        if not (name in data.columns):
            print(name + " column is not in table")
            x = False
    return x


def checkNumberOfCols(data):
    i = 0
    for key in data.keys():
        i = i + 1
    if i == 6:
        return True
    print("Invalid number of columns")
    return False


def checkTypes(data):
    x = True
    col_names = ['page_id', 'page_title', 'rev_id', 'timestamp', 'type', 'id']
    possible_values_for_type = ["doi", "isbn", "pmid", "pmc", "arxiv"]
    for name in col_names:
        if name == 'page_id' or name == 'rev_id':
            if data.dtypes[name] != "int64":
                print("Column \"" + name + "\" contains Invalid Type")
                x = False
        elif name == 'timestamp':
            try:
                data[name] = pd.to_datetime(data[name])
            except TypeError:
                x = False
                print("Column \"" + name + "\" contains Invalid Type")
        elif name == 'type':
            for value in data[name].unique():
                if not(value in possible_values_for_type):
                    x = False
                    print("Column \"" + name + "\" contains Invalid Value")
        else:
            if data.dtypes[name] != "object":
                print("Column \"" + name + "\" contains Invalid Type")
                x = False
    return x

def refineData(data):
    handleEmptyValues(data)
    removeDuplicates(data)


def handleEmptyValues(data):
    # Get columns with empty cells
    num_of_empty_in_col = data.isnull().sum()
    num_of_empty_in_col = num_of_empty_in_col[num_of_empty_in_col != 0]
    if not num_of_empty_in_col.empty:
        print("The following columns have empty fields")
        print(num_of_empty_in_col)
        data = data.dropna()


def removeDuplicates(data):
    data_rows = data.shape[0]
    data = data.drop_duplicates()
    print("There are " + str(data_rows - data.shape[0]) + " Duplicate Rows in the Data")


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
