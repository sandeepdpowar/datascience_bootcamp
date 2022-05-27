import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = '/Users/sandeeppowar/Desktop/Analysis_Projects/datascience_bootcamp/Module3/Resources/election_results.csv'

# Create a filename variable to a direct or indirect path to the file.
file_to_save = '/Users/sandeeppowar/Desktop/Analysis_Projects/datascience_bootcamp/Module3/Resources/analysis/election_analysis.txt'

# Open the election results and read the file
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.

    file_reader = csv.reader(election_data)

    # Print the header row.
    headers = next(file_reader)
    print(headers)