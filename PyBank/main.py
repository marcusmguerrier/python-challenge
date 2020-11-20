#import OS module
import os

#import module to read CSV files
import csv

#assign os.path.join to a variable
budgetData = os.path.join("Resources", "budget_data.csv") 

with open(budgetData) as csvfile:
    csvreader = csv.reader(csvfile)

    print(csvreader)

    csv_header = next(csvreader)
    print(f"{csv_header}")

    #read each row of data after the header
    for row in csvreader:
        print(row)
