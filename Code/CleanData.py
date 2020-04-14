import sys
import os
from FileHelper import *
import difflib

def main():
    for arg in sys.argv[1:] :
        cleanInvalidLines(arg)

def cleanInvalidLines(filename):
    filepath = "../Data/" + filename + ".tsv"
    if fileValid(filepath) :
        print("Cleaning Invalid Lines From: " + filepath)
        file = open(filepath, "r", errors='ignore')
        checkTabs(file)

def checkTabs(file):
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
