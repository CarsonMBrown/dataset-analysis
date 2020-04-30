import os
import pandas as pd

def fileValid(filepath):
    valid = os.access(filepath, os.R_OK)
    return valid

def readFile(filename):
    """
    Opens a file as a pandas dataframe and checks if it is a valid file.
    Returns either the dataframe or None.
    """
    filepath = "../Data/" + filename + ".tsv"
    if fileValid(filepath) :
        print("Reading From: " + filepath)
        data = pd.read_csv(filepath, encoding='utf8', error_bad_lines=False, warn_bad_lines=False, delimiter="\t")
        return data
    else:
        print("File Unable To Be Read")
        return None
