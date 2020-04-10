import pandas as pd
import sys

def main():
    for arg in sys.argv[1:]:
        readFile(arg)

def readFile(filename):
    filepath = "../Data/" + filename + ".tsv"
    print("Reading From: " + filepath)

    data = pd.read_csv(filepath, error_bad_lines=False, warn_bad_lines=False)
    print(data)

if __name__ == '__main__':
    main()
