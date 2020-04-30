import sys
import os
from FileHelper import *
import difflib

def main():
    for arg in sys.argv[1:] :
        cleanInvalidLines(arg)

def cleanInvalidLines(filename):
    """
    Removes all the invalid lines from the data.
    """
    filepath = "../Data/" + filename + ".tsv"
    if fileValid(filepath) :
        print("Cleaning Invalid Lines From: " + filepath)
        file = open(filepath, "r", encoding='utf8')
        checkTabs(file)

def checkTabs(file):
    """
    Checks for lines that don't contain the correct number of tabs.
    """
    print("Checking Tabs...")
    count = 0
    for line in file.readlines():
        line = line.strip()
        numTabs = line.count("\t")
        if numTabs != 5 :
            print("\tInvalid Number Of Tabs On Line: ", count)
        count = count + 1

if __name__ == '__main__':
    main()
