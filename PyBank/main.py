import os
import csv
import numpy


budget_data = os.path.join("C:/Users/Michael/Desktop/bootcamp/python-challenge/PyBank/Resources/budget_data.csv")

# Lists to store data
month = []
profitLoss = []
change_profitLoss = []

# function for average of list
def average(numbers):
    length = len(numbers)
    total = 0.0
    for number in numbers:
        total = total + number
    return total/length

# Function to find max value in list
def max(numbers):
    maximum = numbers[0]
    for i in range(len(numbers)):
        if numbers[i] > maximum:
            maximum = numbers[i]
    return maximum

# Fucntion to find month of max increase
def maxMonth(numbers):
    maximum = numbers[0]
    for i in range(len(numbers)):
        if numbers[i] > maximum:
            maximum = numbers[i]
            # Add 1 to match list length with month
            maxRow = i + 1
    return maxRow

# Function to find min value in list
def min(numbers):
    minimum = numbers[0]
    for i in range(len(numbers)):
        if numbers[i] < minimum:
            minimum = numbers[i]
    return minimum

# Function to find month of max decrease
def minMonth(numbers):
    minimum = numbers[0]
    for i in range(len(numbers)):
        if numbers[i] < minimum:
            minimum = numbers[i]
            # Add 1 to match list length with month
            minRow = i + 1
    return minRow

# Read csv
with open(budget_data, encoding = "utf-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csvheader = next(csvfile)


    for row in csvreader:
        
        # Add month
        month.append(row[0])

        # Add profit/loss
        profitLoss.append(row[1])

    # Find total number of months in dataset
    month_total = len(month)

    # Net total amount of profit/losses
    profitLoss = [int(x) for x in profitLoss]
    total_profitLoss = sum(profitLoss)
    
    # Finds difference between components of list
    change_profitLoss = numpy.diff(profitLoss)
    
    # Print analysis in terminal
    print("Financial Analysis")
    print("------------------------")
    print("Total Months: " + str(month_total))
    print("Total: $" + str(total_profitLoss))
    print("Average Change: $" + str(round(average(change_profitLoss), 2)))

    # Run maxMonth function to find row for 'month'
    x = maxMonth(change_profitLoss)
    print("Greatest Increase in Profits: " + str(month[x]) + " ($" + str(max(change_profitLoss)) + ")")

    # Run minMonth function to find row for 'month'
    y = minMonth(change_profitLoss)
    print("Greatest Decrease in Profits: " + str(month[y]) + " ($" + str(min(change_profitLoss)) + ")")

# Set variable for output file
output_file = os.path.join("C:/Users/Michael/Desktop/bootcamp/python-challenge/PyBank/Analysis/financial_analysis.txt")

#  Open the output file
with open(output_file, "w") as datafile:

    # Write to txt file
    datafile.write("Financial Analysis \n")
    datafile.write("------------------------ \n")
    datafile.write("Total Months: " + str(month_total) + "\n")
    datafile.write("Total: $" + str(total_profitLoss) + "\n")
    datafile.write("Average Change: $" + str(round(average(change_profitLoss), 2)) + "\n")
    datafile.write("Greatest Increase in Profits: " + str(month[x]) + " ($" + str(max(change_profitLoss)) + ") \n")
    datafile.write("Greatest Decrease in Profits: " + str(month[y]) + " ($" + str(min(change_profitLoss)) + ") \n")
