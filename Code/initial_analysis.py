import pandas as pd

# Output the total number of records in the data file (.tsv)
filename = 'enwiki.tsv' # Needs to be integrated with command line arguments and cleaning

eng_data = pd.read_csv(filename, sep = '\t', parse_dates = ['timestamp'])

print("Number of rows, number of columns:", eng_data.shape)

# Output range of dates represented in the data (timestamp)
eng_date = eng_data['timestamp']

print("Sorting date of records...\n")

eng_date = eng_date.sort_values(ascending = True)

print("Earliest date (ns, UTC):", eng_date.iloc[0])
print("Earliest date:", eng_date.iloc[0].date())

print("Latest date (ns, UTC):", eng_date.iloc[-1])
print("Latest date:", eng_date.iloc[-1].date())

# Output a table with the total number of records of each identifier type (pmid, pmcid, doi, isbn, arxiv)
eng_type = eng_data['type']
print("\nCounting occurances of each record type:\n")

# use of value_counts that has been optimised for object type
print(eng_type.value_counts())