#Import file
import os
import csv

#Path to the csvfile
csvpath = os.path.join('..', 'Resources', 'election_data.csv')

#Initializing variables 
Total_Votes = 0
Correy = 0
Khan = 0
OTooley = 0
Li = 0

#Open the CSV
with open(csvpath, newline='') as csvfile:

    #CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    
    #Read The Header Row First
    csv_header = next(csvfile)
    
    #Read each row of data after the header
    for row in csvreader:
        
        #Total Vote Calculation
        Total_Votes = Total_Votes + 1
        
        #Calculate votes by candidate
        if (row[2] == "Khan"):
            Khan = Khan + 1
        elif (row[2] == "Correy"):
            Correy = Correy + 1
        elif (row[2] == "Li"):
            Li = Li + 1
        else:
            OTooley = OTooley + 1
    #Calculate the percent of votes
    Khan_Percent = Khan / Total_Votes
    Correy_Percent = Correy / Total_Votes
    Li_Percent = Li / Total_Votes
    OTooley_Percent = OTooley / Total_Votes

    #Determining winner
    Winner = max(Khan_Percent, Correy_Percent, Li_Percent, OTooley_Percent)
    if Winner == Khan_Percent:
        Winner_Name = "Khan"
    elif Winner == Correy_Percent:
        Winner_Name = "Correy"
    elif Winner == Li_Percent:
        Winner_Name = "Li"
    else: 
        Winner_Name = "O'Tooley"
    
#Printing all values
print(f"Election Results")
print(f"-------------------------")
print(f"Total Votes: {Total_Votes}")
print(f"-------------------------")
print(f"Khan: {Khan_Percent:.3%} ({Khan})")
print(f"Correy: {Correy_Percent:.3%} ({Correy})")
print(f"Li: {Li_Percent:.3%} ({Li})")
print(f"O'Tooley: {OTooley_Percent:.3%} ({OTooley})")
print(f"-------------------------") 
print(f"Winner: {Winner_Name}")
print(f"-------------------------")  

#Specify the file to write to
output_path = os.path.join('..', 'Resources', 'Poll Results.txt')

#Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', ) as txtfile:

    #Write data
    txtfile.write(f"Election Results\n")
    txtfile.write(f"-------------------------\n")
    txtfile.write(f"Total Votes: {Total_Votes}\n")
    txtfile.write(f"-------------------------\n")
    txtfile.write(f"Khan: {Khan_Percent:.3%} ({Khan})\n")
    txtfile.write(f"Correy: {Correy_Percent:.3%} ({Correy})\n")
    txtfile.write(f"Li: {Li_Percent:.3%} ({Li})\n")
    txtfile.write(f"O'Tooley: {OTooley_Percent:.3%} ({OTooley})\n")
    txtfile.write(f"-------------------------\n") 
    txtfile.write(f"Winner: {Winner_Name}\n")
    txtfile.write(f"-------------------------\n") 