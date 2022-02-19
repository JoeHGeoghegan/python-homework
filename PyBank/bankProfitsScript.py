"""
Created by Joe Geoghegan

Purpose of this code is analyzing the financial records of a company. The resources folder contains a CSV file called "budget_data.csv" which contains the simple financial records. This dataset is composed of two columns, Date and Profit/Losses.

The Analysis calculates each of the following:
    The total number of months included in the dataset.
    The net total amount of Profit/Losses over the entire period.
    The average of the changes in Profit/Losses over the entire period.
    The greatest increase in profits (date and amount) over the entire period.
    The greatest decrease in losses (date and amount) over the entire period.
"""

## Imports
import csv # Used for reading CSV file
from pathlib import Path # Used for ensuring readable file paths
#from pathlib import Path # Used in establishing CSV file location/path
## Variables
#Path Variables
data_path = Path("./Resources/budget_data.csv")

# Working Data Variables
budget_data = {} #Dictionary to contain csv data

# Results Variables
total_months = 0 # The total number of months included in the dataset.
net = 0.0 # The net total amount of Profit/Losses over the entire period.
average = 0.0 # The average of the changes in Profit/Losses over the entire period.
max_increase_timestamp = None # The month and year the greatest increase in profits occured
max_increase = 0.0 # The amount of the greatest increase in time stamped year
max_decrease_timestamp = None # The month and year the greatest decrease in profits occured
max_decrease = 0.0 # The amount of the greatest decrease in time stamped year

""" Main Code """
# Read CSV and convert to dictionary
with open(data_path, 'r') as data_file:
    csv_reader = csv.reader(data_file)
    budget_data = {rows[0]:rows[1] for rows in csv_reader}

# Pop (remove) header off of dictionary
budget_data.pop('Date')

# Loop through until data no more data
for month in budget_data:
    total_months+=1 #Increase count for total months
    month_budget = int(budget_data[month]) #extract month's budget casted as integer
    net += month_budget #Roll year's budget into net profit/loss

    # Check if a max increase (If Equal, keep first found)
    if month_budget > max_increase:
        max_increase = month_budget
        max_increase_timestamp = month
    # Check if a max decrease (If Equal, keep first found)
    elif month_budget < max_decrease:
        max_decrease = month_budget
        max_decrease_timestamp = month
    #else statement is unnecessary, line added for clarity

#Calculate Average Profit/Losses
average = net / total_months

# Print Results
print("Financial Analysis\n----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net:.2f}")
print(f"Average  Change: ${average:.2f}")
print(f"Greatest Increase in Profits: {max_increase_timestamp} ({max_increase:.2f})")
print(f"Greatest Decrease in Profits: {max_decrease_timestamp} (${max_decrease:.2f})")