#Import file
import os
import csv

#Path to the csvfile
csvpath = os.path.join('employee_data.csv')

#Initializing variables 
Emp_Id = []
First_Name = []
Last_Name = []
DOB = []
SSN = []
State = []
Name = []
US_State = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

#Open the CSV
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)
    #Read each row of data after the header
    for row in csvreader:
        #Gather emp_id
        Emp_Id.append(row[0])
        #Split name up
        First_Name.append(row[1].split(" ")[0])
        Last_Name.append(row[1].split(" ")[1])
        #Format dob
        DOB.append(row[2].split('-')[1] + '/' + row[2].split('-')[2] + '/' + row[2].split('-')[0])
        #Amend SSN
        SSN.append("***-**-" + row[3].split("-")[2])
        #Abbreviate state
        State.append(US_State[row[4]])

#Structure new data
New_List = zip(Emp_Id, First_Name, Last_Name, DOB, SSN, State)

#Specify the file to write to
output_path = os.path.join('formatted_employee_data.csv')

#Open the file using "write" mode. Set variable to hold the contents
with open(output_path, 'w', newline='') as f:
    #Write data
    csvwriter = csv.writer(f, delimiter=',')
    csvwriter.writerow(['Emp ID','First Name','Last Name','DOB','SSN','State'])
    csvwriter.writerows(list(New_List))
