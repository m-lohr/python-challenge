import os
import csv
import numpy


election_data = os.path.join("C:/Users/Michael/Desktop/bootcamp/python-challenge/PyPoll", "Resources", "election_data.csv")

# Lists to store data
voterID = []
county = []
candidate = []

# Read csv
with open(election_data, encoding = "utf-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csvheader = next(csvfile)

    for row in csvreader:
        
        # Add voter IDs to list
        voterID.append(row[0])

        # Add counties to list
        county.append(row[1])

        # Add cancicates to list
        candidate.append(row[2])

    # Count total votes
    total_votes = (len(voterID))

    # Count Stockham votes
    count1 = candidate.count("Charles Casper Stockham")
    percent1 = round(((count1/total_votes) * 100), 3)

    # Count DeGette votes
    count2 = candidate.count("Diana DeGette")

    # Count Doane votes
    count3 = candidate.count("Raymon Anthony Doane")

    # Print results
    print("Election Results")
    print("-----------------")
    print("Total Votes: " + str(total_votes))
    print("-----------------")
    print("Charles Casper Stockham: " + "(" + str(count1) + ")")
    print("Diana DeGette: " + str(percent1) + "% (" + str(count2) +")")
    print("Raymon Anthony Doane: " + "(" + str(count3) + ")")
    print("Winner: ")

