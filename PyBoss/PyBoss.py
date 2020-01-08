#Import file
import os
import csv

#Path to the csvfiles
csvpath = os.path.join('employee_data.csv')
outputfilename = 'formatted_employee_data.csv'

#Initializing variables 
emp_id = []
first_name = []
last_name = []
dob =[]
ssn = []
state = []
name = []
us_state_abbrev = {
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
        emp_id.append(row[0])
        #Split name up
        first_name.append(row[1].split(" ")[0])
        last_name.append(row[1].split(" ")[1])
        #Format dob
        dob.append(row[2].split('-')[1] + '/' + row[2].split('-')[2] + '/' + row[2].split('-')[0])
        #Amend SSN
        ssn.append("***-**-" + row[3].split("-")[2])
        #Abbreviate state
        state.append(us_state_abbrev[row[4]])

#Structure new data
New_List = zip(emp_id, first_name, last_name, dob, ssn, state)

#Open the file using "write" mode. Set variable to hold the contents
with open(outputfilename, 'w', newline='') as f:
    #Write data
    csvwriter = csv.writer(f, delimiter=',')
    csvwriter.writerow(['Emp ID','First Name','Last Name','DOB','SSN','State'])
    csvwriter.writerows(list(New_List))
