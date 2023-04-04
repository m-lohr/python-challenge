import os
import csv
import numpy
from statistics import mode


election_data = os.path.join("C:/Users/Michael/Desktop/bootcamp/python-challenge/PyPoll", "Resources", "election_data.csv")

# Lists to store data
voterID = []
county = []
candidate = []
cand_ind = []

#def count(votes)
#    for i in range(len(votes)):
#        counter = 0
#        if candidate[i] == candidate[i + 1]:
#            counter = counter + 1
#    return counter

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

    # Find individual candidates
    for i in range(len(candidate)):
        if candidate[i] != candidate[i-1]:
            cand_ind.append(candidate[i-1])
    
    # Count votes for individual candidates and analyze
    cand1 = candidate.count(cand_ind[1])
    percent1 = round(((cand1/total_votes) * 100), 3)

    cand2 = candidate.count(cand_ind[2])
    percent2 = round(((cand2/total_votes) * 100), 3)

    cand3 = candidate.count(cand_ind[3])
    percent3 = round(((cand3/total_votes) * 100), 3)

    # Find candidate with most votes
    winner = mode(candidate)

    # Count Stockham votes
    #count1 = candidate.count("Charles Casper Stockham")
    #percent1 = round(((count1/total_votes) * 100), 3)

    # Count DeGette votes
    #count2 = candidate.count("Diana DeGette")

    # Count Doane votes
    #count3 = candidate.count("Raymon Anthony Doane")

    # Print results
    print("Election Results")
    print("-----------------")
    print("Total Votes: " + str(total_votes))
    print("-----------------")
    print(str(cand_ind[1]) + ": " + str(percent1) + "% (" + str(cand1) + ")")
    print(str(cand_ind[2]) + ": " + str(percent2) + "% (" + str(cand2) + ")")
    print(str(cand_ind[3]) + ": " + str(percent3) + "% (" + str(cand3) + ")")
    print("-----------------")
    print("Winner: " + str(winner))
    print("-----------------")


# Set variable for output file
output_file = os.path.join("C:/Users/Michael/Desktop/bootcamp/python-challenge/PyPoll", "Analysis", "Poll_Results.txt")

#  Open the output file
with open(output_file, "w") as datafile:

    # Write to txt file
    datafile.write("Election Results \n")
    datafile.write("----------------- \n")
    datafile.write("Total Votes: " + str(total_votes) + "\n")
    datafile.write("----------------- \n")
    datafile.write(str(cand_ind[1]) + ": " + str(percent1) + "% (" + str(cand1) + ") \n")
    datafile.write(str(cand_ind[2]) + ": " + str(percent2) + "% (" + str(cand2) + ") \n")
    datafile.write(str(cand_ind[3]) + ": " + str(percent3) + "% (" + str(cand3) + ") \n")
    datafile.write("----------------- \n")
    datafile.write("Winner: " + str(winner) + "\n")
    datafile.write("----------------- \n")

