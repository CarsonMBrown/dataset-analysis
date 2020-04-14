import os
import pandas as pd

def fileValid(filepath):
    valid = os.access(filepath, os.R_OK)
    return valid

def readFile(filename):
    filepath = "../Data/" + filename + ".tsv"
    if fileValid(filepath) :
        print("Reading From: " + filepath)
        data = pd.read_csv(filepath, encoding='utf8', error_bad_lines=False, warn_bad_lines=False, delim_whitespace=True)
        return data
    else:
        print("File Unable To Be Read")
        return None
