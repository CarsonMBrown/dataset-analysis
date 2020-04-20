import pandas as pd
import sys
import textwrap
from FileHelper import *

def main():
    for arg in sys.argv[1:] :
        data = readFile(arg)
        if data is not None :
            arxivCitations(data)
            avgCitatations(data)
            mostCommonCitations(data)

def indentDataFrame(toIndent):
    return "\t" + toIndent.to_string().replace("\n", "\n\t") + "\n"

def arxivCitations(data):
    arxivCitations = data.query("type == \"arxiv\"")
    onlyYears = arxivCitations["timestamp"].str.slice(stop=4)
    yearCounts = onlyYears.value_counts()
    print("Number Of ArXiv Citations By Year: ")
    print(indentDataFrame(yearCounts))


def avgCitatations(data):
    valueCount = data["page_id"].value_counts()
    mean = valueCount.mean()
    median = valueCount.median()
    print("Average Citations:")
    print("\tMean:   " + str(mean))
    print("\tMedian: " + str(median) + "\n")

def toUpper(s):
    return s.upper()

def mostCommonCitations(data):
    print("The 10 Most Cited Sources Are: ")
    citations = data["type"].apply(toUpper) + " " + data["id"]
    citationCount = citations.value_counts().head(10)
    print(indentDataFrame(citationCount))

if __name__ == '__main__':
    main()
