import sys
import os
from fileHelper import *
import difflib
import re

def main():
    """Runs independently to check data, refine data and save data to a new clean .tsv file"""
    for arg in sys.argv[1:]:
        data = readFile(arg)
        if data is not None:
            checkData(data)
            data = refineData(data)
            saveData(arg, data)


def saveData(dataName, data):
    """
    Saves the data to file
    """
    data.to_csv(dataName + "Clean.tsv", sep="\t", index=False)

def checkData(data):
    """
    Checks data is of valid format.
    """
    x = checkNumberOfCols(data)
    x = x and checkColNames(data)
    x = x and checkTypes(data)
    if not x:
        print("Data has inconsistencies, trying to run analysis may result in unexpected errors")
        sys.exit(1)


def checkColNames(data):
    """
    Checks column names.
    """
    col_names = ['page_id', 'page_title', 'rev_id', 'timestamp', 'type', 'id']
    x = True
    for name in col_names:
        if not (name in data.columns):
            print(name + " column is not in table")
            x = False
    return x


def checkNumberOfCols(data):
    """
    Checks number of columns.
    """
    if data.keys().shape[0] == 6:
        return True
    print("Invalid number of columns")
    return False


def checkTypes(data):
    """
    Checks each column has proper type.
    """
    x = True
    col_names = ['page_id', 'page_title', 'rev_id', 'timestamp', 'type', 'id']
    possible_values_for_type = ["doi", "isbn", "pmid", "pmc", "arxiv"]
    for name in col_names:
        if name == 'page_id' or name == 'rev_id':
            if data.dtypes[name] != "int64":
                print("Column \"" + name + "\" contains Invalid Type")
                x = False

        elif name == 'timestamp':
            if data.dtypes[name] != "datetime64[ns, UTC]":
                print("Column \"" + name + "\" contains Invalid Type")
                x = False

        elif name == 'type':
            for value in data[name].unique():
                if not (value in possible_values_for_type):
                    x = False
                    print("Column \"" + name + "\" contains Invalid Value")
        else:
            if data.dtypes[name] != "object":
                print("Column \"" + name + "\" contains Invalid Type")
                x = False
    return x


def refineData(data):
    """
    Calls fns to refine data.
    """
    data = checkTypeIdMismatch(data)
    data = handleEmptyValues(data)
    data = removeDuplicates(data)
    return data


def checkTypeIdMismatch(data):
    """
    Calls fns to check for type id mismatch.
    """
    # possible_values_for_type = ["doi", "isbn", "pmid", "pmc", "arxiv"]
    data = data.reset_index(drop=True)
    data = checkPMIDMismatch(data)
    data = checkISBNMismatch(data)
    return data


def checkPMIDMismatch(data):
    """
    Checks for PMID mismatch and removes any.
    """
    num_rows = data.shape[0]
    rows_with_pmid = data[data.type == 'pmid']
    rows_id_not_valid = rows_with_pmid[~rows_with_pmid.id.str.match("^(0{0,}\d{1,8})$")]
    data.drop(rows_id_not_valid.index, inplace=True)
    print(str(num_rows - data.shape[0]) + " Lines with mismatched pmid removed")
    return data


def checkISBNMismatch(data):
    """
    Checks for isbn mismatch and removes any.
    """
    num_rows = data.shape[0]
    rows_with_pmid = data[data.type == 'isbn']
    rows_id_not_valid = rows_with_pmid[~rows_with_pmid.id.str.match("^(97(8|9))?\d{9}(\d|X)$")]
    data.drop(rows_id_not_valid.index, inplace=True)
    print(str(num_rows - data.shape[0]) + " Lines with mismatched isbn removed")
    return data


def handleEmptyValues(data):
    """
    Drops rows with empty values
    """
    num_of_empty_in_col = data.isnull().sum()
    num_of_empty_in_col = num_of_empty_in_col[num_of_empty_in_col != 0]
    if not num_of_empty_in_col.empty:
        print("The following columns have empty fields")
        print(num_of_empty_in_col)
        data = data.dropna()
    return data


def removeDuplicates(data):
    """
    Removes any duplicates from the data. Displays the number of duplicate lines that were removed.
    """
    data_rows = data.shape[0]
    data = data.drop_duplicates()
    print("There are " + str(data_rows - data.shape[0]) + " Duplicate Rows in the Data")
    return data


if __name__ == '__main__':
    main()
