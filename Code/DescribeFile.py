import pandas as pd
import sys
import textwrap
from FileHelper import *

def main():
    for arg in sys.argv[1:] :
        data = readFile(arg)
        if data is not None :
            arxivCitations(data)
            print()
            avgCitatations(data)


def arxivCitations(data):
    arxivCitations = data.query("type == \"arxiv\"")
    onlyYears = arxivCitations["timestamp"].str.slice(stop=4)
    yearCounts = onlyYears.value_counts()
    print("Number Of ArXiv Citations By Year: ")
    print("\t" + yearCounts.to_string().replace("\n", "\n\t"))


def avgCitatations(data):
    valueCount = data["page_id"].value_counts()
    mean = valueCount.mean()
    median = valueCount.median()
    print("Average Citations:")
    print("\tMean:   " + str(mean))
    print("\tMedian: " + str(median))


if __name__ == '__main__':
    main()
