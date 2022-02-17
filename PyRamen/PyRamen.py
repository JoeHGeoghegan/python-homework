# -*- coding: UTF-8 -*-
"""PyRamen Homework"""
"""
Created by Joe Geoghegan

The purpose of this code is to utilize a ramen menu (csv file) and sales data and generate a report dictionary to a text file. The report outputs each ramen type as the keys of the dictionary. 
    Dictionary: <ramen type>{01-count, 02-revenue, 03-cogs, 04-profit metrics}
"""

# Import libraries
import csv
from pathlib import Path

# Set file paths for menu_data.csv and sales_data.csv
menu_filepath = Path('./Resources/menu_data.csv')
sales_filepath = Path('./Resources/sales_data.csv')

# Initialize list objects to hold our menu and sales data
menu = []
sales = []

## Helper Function(s)
# Returns a list of lists from a csv
    # Instructions specified using a list of lists, however list of dict reads better
    # Created to reduce repeat code as multiple files are being read
    # Inputs:
        # a csv file pathway (String)
        # header titles (List of strings)
def readCSV(path,dict_categories):
    result = []
    with open(path) as csv_data: # Open Menu CSV File
        csv_reader = csv.reader(csv_data) # Create csv reader
        next(csv_reader) #skip header
        for row in csv_reader: #read CSV by rows
            add_dict = {} #init empty dict
            row_count = 0 #init row count for dict_categories loop
            for key in dict_categories:
                add_dict[key] = row[row_count]
                row_count += 1
            result.append(add_dict) #append the collumn's information as a dict
            #to make list of list, use row variable instead and remove above for loop, variables, and input
    return result

# Read in the menu data into the menu list
menu = readCSV(menu_filepath, ['Item','Category','Description','Price','Cost'])
# Read in the sales data into the sales list
sales = readCSV(sales_filepath, ['Line_Item_ID','Date','Credit_Card_Number','Quantity','Menu_Item'])

# Initialize dict object to hold our key-value pairs of items and metrics
report = {}

# Initialize a row counter variable
# row_count = 0 #never had to use, directions didn't say to use

# Loop over every row in the sales list object
for sale_data in sales: #KEYS: 'Line_Item_ID','Date','Credit_Card_Number','Quantity','Menu_Item'
    # Initialize sales data variables
    Quantity = int(sale_data['Quantity']) # Quanity Reference
    Menu_Item = sale_data['Menu_Item'] # Menu_Item Reference
    
    # If the item value not in the report, add it as a new entry with initialized metrics
    if Menu_Item not in report.keys(): # If this is the first instance of a menu item, initalize its dictionary entry
        # Naming convention allows the keys to be ordered in logical fashion, count, revenue, cost, profit
        report[Menu_Item] = {
            "01-count": 0,
            "02-revenue": 0,
            "03-cogs": 0,
            "04-profit": 0,
        }

    # For every row in our sales data, loop over the menu records to determine a match
    for menu_item in menu: #KEYS: 'Item','Category','Description','Price','Cost'
        # Initialize menu data variables
        Item = menu_item['Item'] # Item Reference
        Price = float(menu_item['Price']) # Price Reference
        Cost = float(menu_item['Cost']) # Cost Reference
            
        # If the item value in our sales data is equal to the any of the items in the menu, then begin tracking metrics for that item
        if Item == Menu_Item:
            # Calculate profit of each item in the menu data.
                # moved for efficiency, no reason to calculate if menu item is wrong
                # would be even more efficient to generate at list creation
            profit = Price - Cost
            
            # Print out matching menu data # Silencing, listed as a TODO but directions do not have this
            # print(f"Menu Match: {Menu_Item} is being updated")
            
            # Cumulatively add up the metrics for each item key
            report[Menu_Item]["01-count"] += Quantity
            report[Menu_Item]["02-revenue"] += Price
            report[Menu_Item]["03-cogs"] += Cost
            report[Menu_Item]["04-profit"] += profit
        # Else, the sales item does not equal any fo the item in the menu data, therefore no match
        else:
            pass
        
        # Increment the row counter by 1
        #row_count += 1 # never had to use, directions didn't say to use

# Print total number of records in sales data
# Assembling report to later print to txt file
reportString = "----------REPORT----------"
reportString += f"\nNumber of unique records captured: {len(report)}"
reportString += f"\nNumber of sales analyized: {len(sales)}" #same as row_count if it was used
for item, stats in report.items():
    reportString += f"\n{item}: {stats}"
print(reportString)

# @TODO: Write out report to a text file (won't appear on the command line output)
report_Filepath = Path('./Resources/Report.txt') # Only keeps the most recent report
with open(report_Filepath,'w') as archive_report:
    archive_report.write(reportString)