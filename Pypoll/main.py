import os
import csv

# Define the file path for reading
csvpath = os.path.join('Pypoll', 'Resources', 'election_data.csv')

# Variables
total_votes = 0
candidates = {}
winner = ""
highest_votes = 0

# Read the CSV file
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Skip the header row
    next(csvreader)
    
    # Loop through the rows
    for row in csvreader:
        # Increment total votes
        total_votes += 1
        
        # Get the candidate name
        candidate = row[2]
        
        # If candidate is not in the dictionary, add them with a vote count of 1
        # Otherwise, increment their vote count
        if candidate not in candidates:
            candidates[candidate] = 1
        else:
            candidates[candidate] += 1

# Print the results and find the winner
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    print(f"{candidate}: {percentage:.3f}% ({votes})")
    if votes > highest_votes:
        highest_votes = votes
        winner = candidate
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Define the output path for writing
output_path = os.path.join('Pypoll', 'Analysis', 'election_results.txt')

# Write the results to a text file
with open(output_path, 'w') as file:
    file.write("Election Results\n")
    file.write("-------------------------\n")
    file.write(f"Total Votes: {total_votes}\n")
    file.write("-------------------------\n")
    for candidate, votes in candidates.items():
        percentage = (votes / total_votes) * 100
        file.write(f"{candidate}: {percentage:.3f}% ({votes})\n")
    file.write("-------------------------\n")
    file.write(f"Winner: {winner}\n")
    file.write("-------------------------\n")
