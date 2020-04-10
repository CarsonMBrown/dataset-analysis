import pandas as pd
import sys
import os

def main():
    for arg in sys.argv[1:]:
        data = readFile(arg)
        if data is not None :
            checkTypes(data)
            checkDuplicates(data)

def fileValid(filepath):
    valid = os.access(filepath, os.R_OK)
    return valid

def readFile(filename):
    filepath = "../Data/" + filename + ".tsv"
    if (fileValid(filepath)):
        print("Reading From: " + filepath)
        data = pd.read_csv(filepath, error_bad_lines=False, warn_bad_lines=False, delim_whitespace=True)
        return data
    else:
        print("File Unable To Be Read")
        return None

def checkTypes(data):
    allValid = True
    for i in range(0,6):
        if i == 0 or i == 2 :
            if data.dtypes[i] != "int64" :
                print("Column \"" + movies_df.columns[i] + "\" Contains Invalid Type")
                allValid = False
        else :
            if data.dtypes[i] != "object" :
                print("Column \"" + movies_df.columns[i] + "\" Contains Invalid Type")
                allValid = False
    if allValid :
        print("All Data Is Of The Correct Type")

def checkDuplicates(data):
    newRows = data.drop_duplicates().shape[0]
    dataRows = data.shape[0]
    print("There are " + str(dataRows - newRows) + " Duplicate Rows in the Data")


if __name__ == '__main__':
    main()
