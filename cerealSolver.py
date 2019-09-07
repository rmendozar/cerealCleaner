# import modules
import csv
import os

# open csv
cerealCSV = os.path.join(".",'resources',"cereal.csv")
with open (cerealCSV,"r") as csvfile:
    # create csv reader
    csvreader = csv.reader(csvfile,delimiter=",")
    csvHeader = next(csvreader)
    print(csvHeader)
    # iterate each row (for loop)
    for row in csvreader:
        # if statement (if cereal contains 5 or more grams of fiber, print)
        if float(row[7])>=5:
            print(row)


# print row if condition meets