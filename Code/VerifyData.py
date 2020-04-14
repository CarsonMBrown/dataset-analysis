import pandas as pd
import sys
from FileHelper import *

def main():
    for arg in sys.argv[1:] :
        data = readFile(arg)
        if data is not None :
            checkTypes(data)
            removeDuplicates(data)

def checkTypes(data):
    allValid = True
    for i in range(0,6) :
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

def removeDuplicates(data):
    newRows = data.drop_duplicates().shape[0]
    dataRows = data.shape[0]
    print("There are " + str(dataRows - newRows) + " Duplicate Rows in the Data")

if __name__ == '__main__':
    main()
