# ZenZorrito-Task

## Description

I want to analyze my Company data so that I could take advantage of this info and make more money for my company (this is a highly competitive sector). No DB usage is needed, we just need to read the csv file and show the results on the screen.

## Details

The analysis involves the following tasks:

1. Retrieve the customer with the earliest check-in date.
2. Retrieve the customer with the latest check-in date.
3. Retrieve a list of customer’s full names ordered alphabetically.
4. Retrieve a list of the companies user’s jobs ordered alphabetically.

The required fields in the CSV file are Street, Zip, City, Last Check-in Date, and Company. 

Exception Handling:

- Ensure that every exception is handled appropriately.
- Log exceptions if a required field is empty for a row, but continue processing the rest of the file.
- Log an exception if a row contains fewer fields than expected, but continue processing the rest of the file.
- Log an exception if a row does not contain any data, but continue processing the rest of the file.

## Functional Notes

- The CSV file has the following headers: First Name, Last Name, Street, Zip, City, Type, Job, Phone, Last Check-In Date, and Company.
- The full name of customers is composed of First Name + Last Name.

## Technical Notes

- The example file provided contains 10 rows of data (excluding the header), but the script is designed to work with any file.
- It is recommended to log exceptions to provide detailed information about any issues encountered during processing.
