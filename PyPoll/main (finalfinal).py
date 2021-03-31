# Import those modules
import os
import csv

# File path
csvpath = os.path.join("..", "PyPoll", "Resources", "election_data.csv")

#The Variables
total_votes = 0
candidate = ""
candidate_list = []
vote_list = []
percent_list = []
winner = ""

# Open the CSV (Thx GitHub)
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # Read the header row first
    csv_header = next(csvreader)
    
    # Read each row of data after the header
    for row in csvreader:
        # count the total number of months
        total_votes += 1
        
        if row[2] not in candidate_list:
            candidate_list.append(row[2])
            vote_list.append(1)
        else:
            vote_list[candidate_list.index(row[2])] += 1