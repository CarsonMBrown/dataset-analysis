import pandas as pd
import sys
from FileHelper import *

def main():
    for arg in sys.argv[1:] :
        data = readFile(arg)
        if data is not None :
            avgCitatations(data)


def avgCitatations(data):
    valueCount = data["page_id"].value_counts()
    mean = valueCount.mean()
    median = valueCount.median()
    print("Average Citations:")
    print("\tMean:   " + str(mean))
    print("\tMedian: " + str(median))


if __name__ == '__main__':
    main()
