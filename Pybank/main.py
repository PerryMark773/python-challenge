# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

# Path to collect data from the Resources folder
csvpath = os.path.join('Pybank', 'Resources', 'budget_data.csv')

# Variables
total_months = 0
total_profit_losses = 0
changes = []
previous_profit_losses = 0
greatest_increase = 0
greatest_decrease = 0
greatest_increase_date = ""
greatest_decrease_date = ""

# Read in the CSV file
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Read the header row first
    header = next(csvreader)
    
    # Loop through the data
    for row in csvreader:
        # Calculate total months
        total_months += 1
        
        # Calculate total profit/losses
        profit_losses = int(row[1])
        total_profit_losses += profit_losses
        
        # Calculate changes in profit/losses
        change = profit_losses - previous_profit_losses
        if total_months > 1:
            changes.append(change)
        
        # Find greatest increase and decrease in profits
        if change > greatest_increase and total_months > 1:
            greatest_increase = change
            greatest_increase_date = row[0]
        if change < greatest_decrease and total_months > 1:
            greatest_decrease = change
            greatest_decrease_date = row[0]
        
        previous_profit_losses = profit_losses

# Calculate the average change
average_change = sum(changes) / len(changes)

# Print the analysis
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit_losses}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")

# Export a text file with the results
output_path = os.path.join('Pybank', 'Analysis', 'financial_analysis.txt')
with open(output_path, 'w') as file:
    file.write("Financial Analysis\n")
    file.write("----------------------------\n")
    file.write(f"Total Months: {total_months}\n")
    file.write(f"Total: ${total_profit_losses}\n")
    file.write(f"Average Change: ${average_change:.2f}\n")
    file.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n")
    file.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n")