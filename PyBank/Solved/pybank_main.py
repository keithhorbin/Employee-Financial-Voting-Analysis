#Import file
import os
import csv

#Path to the csvfile
csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

#Initializing variables 
Month = 0
Revenue = 0
Delta = []
Date_Count = []
Great_Inc = 0
Great_Dec = 0
Great_Inc_Month = 0
Great_Dec_Month = 0

#Open the CSV
with open(csvpath, newline = '') as csvfile:

    #CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter = ',')
     #Read The Header Row First
    csv_header = next(csvfile)
    
    #Read each row of data after the header
    for row in csvreader:
        #Calculating the total number of months and total revenue
        Previous_Profit = int(row[1])
        Month = Month + 1
        Revenue = Revenue + int(row[1])
        Great_Inc = int(row[1])
        Great_Inc_Month = row[0]
        Great_Dec = int(row[1])
        Great_Dec_Month = row[0]

        for row in csvreader:
            Month = Month + 1
            Revenue = Revenue + int(row[1])

            #Calculate month over month change
            Change = int(row[1]) - Previous_Profit
            Delta.append(Change)
            Previous_Profit = int(row[1])
            Date_Count.append(row[0])
        
            #Calculate greatest increase
            if int(row[1]) > Great_Inc:
                Great_Inc = int(row[1])
                Great_Inc_Month = row[0]
        
            #Calculate greatest decrease
            if int (row[1]) < Great_Dec:
                Great_Dec = int(row[1])
                Great_Dec_Month = row[0]
        
        #Calculate the average, best, worst changes
        Average = round(sum(Delta) / len(Delta), 2)
        Best = max(Delta)
        Worst = min(Delta)

#Printing all values
print(f"Total Months: {Month}")
print(f"Total Revenue: ${Revenue}")
print(f"Average Change: ${Average}")
print(f"Greatest Increase in Profits: {Great_Inc_Month} (${max(Delta)})")
print(f"Greatest Decrease in Profits: {Great_Dec_Month} (${min(Delta)})")

#Specify the file to write to
output_path = os.path.join('..', 'Resources', 'Bank Results.txt')

#Open the file using "write" mode. Set variable to hold the contents
with open(output_path, 'w', ) as txtfile:

    #Write data
    txtfile.write(f"Financial Analysis\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Total Months: {Month}\n")
    txtfile.write(f"Total: ${Revenue}\n")
    txtfile.write(f"Average Change: ${Average}\n")
    txtfile.write(f"Greatest Increase in Profits:, {Great_Inc_Month}, (${max(Delta)})\n")
    txtfile.write(f"Greatest Decrease in Profits:, {Great_Dec_Month}, (${min(Delta)})\n")