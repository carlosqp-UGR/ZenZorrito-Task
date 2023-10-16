# author: Carlos Quesada Pérez
# date: 13/10/2023
import csv
import logging
from enum import Enum
from datetime import datetime

# Set up logging
logging.basicConfig(filename='error.log', level=logging.ERROR)

### Read data

# Input CSV file (relative path)
csv_file = "./Sample test file - Sheet1.csv"

# Reads the CSV file
with open(csv_file, 'r', encoding='utf-8') as file:

    # Create a structure to save data from CSV file
    data = []

    # Create a CSV DictReader (dictionary reader)
    csv_reader = csv.DictReader(file)

    # Get the field names from the CSV file
    # Define enum to work with CSV fields
    class FieldNames(Enum):
        FIRST_NAME = csv_reader.fieldnames[0]
        LAST_NAME = csv_reader.fieldnames[1]
        STREET = csv_reader.fieldnames[2]               #required
        ZIP = csv_reader.fieldnames[3]                  #required
        CITY = csv_reader.fieldnames[4]                 #required
        TYPE = csv_reader.fieldnames[5]     
        LAST_CHECK_IN_DATE = csv_reader.fieldnames[6]   #required
        JOB = csv_reader.fieldnames[7]
        PHONE = csv_reader.fieldnames[8]
        COMPANY = csv_reader.fieldnames[9]              #required

    # Iterate over each line in the CSV file and save it in data
    for line in csv_reader:
        # A line will not be processed if:
        # 1. It has less fields than expected
        # 2. It has an empty required field
        # 3. It doesn't have any data

        try:
            # Check if the row has less fields than expected
            if len(line) < len(FieldNames):
                raise Exception("Line could not be processed - Less fields than expected ({})".format(line))                
            # Check if any required field is empty
            elif not line[FieldNames.STREET.value] or not line[FieldNames.ZIP.value] or not line[FieldNames.CITY.value] or not line[FieldNames.LAST_CHECK_IN_DATE.value] or not line[FieldNames.COMPANY.value] :
                raise Exception("Line could not be processed - Required field is empty ({})".format(line))
            # Process data
            else :
                data.append(line)
        except Exception as e:
            logging.error(str(e))

# Close the CSV file
file.close()

### Analysise processed data

## Retrieve the customer with the earliest check in date.
# Neccessary conversion from string to datetime for comparison in function min()   
customer_with_earliest_checkin = min(data, key=lambda x: datetime.strptime(x[FieldNames.LAST_CHECK_IN_DATE.value], "%d/%m/%Y"))
print("\nCustomer with earliest check-in date:\n\t" + str(customer_with_earliest_checkin))

## Retrieve the customer with the latest check in date.
customer_with_latest_checkin = max(data, key=lambda x: datetime.strptime(x[FieldNames.LAST_CHECK_IN_DATE.value], "%d/%m/%Y"))
print("\nCustomer with latest check-in date:\n\t" + str(customer_with_latest_checkin))

## Retrieve a list of customer’s full names ordered alphabetically.
# Add 'Full Name' field to sort the list
for entry in data:
    entry['Full Name'] = entry[FieldNames.FIRST_NAME.value] + " " + entry[FieldNames.LAST_NAME.value]

data_sorted_by_name = sorted(data, key=lambda x: x['Full Name'])

print("\nList of customer’s full names ordered alphabetically:")
for entry in data_sorted_by_name:
    print("\t" + str(entry['Full Name']))

## Retrieve a list of the companies user’s jobs ordered alphabetically.

# List of different companies in our data (ordered alfabetically)
companies = sorted(set(entry[FieldNames.COMPANY.value] for entry in data))

#  Dictionary to store jobs for each company
company_jobs = {company: [] for company in companies}

# Iterate over data to add jobs
for entry in data:
    company = entry[FieldNames.COMPANY.value]
    job = entry[FieldNames.JOB.value]

    # If job is not already in the list, add it
    if job not in company_jobs[company]:
        company_jobs[company].append(job)

# Sort jobs for each company alphabetically
for company in company_jobs:
    company_jobs[company] = sorted(company_jobs[company])

# Print the result
print("\nList of companies user’s jobs ordered alphabetically:")
for company in company_jobs:
    print("\tCompany: " + company)
    for job in company_jobs[company]:
        print("\t\tJob: " + job)

'''
# Another way to iterate a dictionary, method company_jobs.items() 
# returns a view of tuples where each tuple has two elements: 
# the key (in this case, the company name) and the value (the list of
# jobs associated with that company).
for company, jobs in company_jobs.items():
    print(f"\tCompany: {company}")
    for job in jobs:
        print(f"\t\tJob: {job}")
'''

