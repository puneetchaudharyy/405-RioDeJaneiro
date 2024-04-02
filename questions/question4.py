#!/usr/bin/env python
'''
question4.py
  Author(s): Puneet Chaudhary (1231356), Krish Garg (1275663), Yash Tandon (1258096)

  Project: Job Vacancies in Canada
  Date of Last Update: April 1, 2024

  Functional Summary

    There are expected to be  fields:
      1. The date of the report
      2. The geographic location of the report (here, Canada)
      3. The type of National Occupational Classifiation
      4. The criteria of job vacancy classifications (here, duration of job vacancies)
      5. The type of value (here, Job vacancies)
      6. The number of job vacancies 

        - The script will read the data from the file and print the relevant data to the 
        console which can be redirected to a file.
        - question4.py extracts the data from the CSV file and logs it onto the console based 
        on inputs from the user.

    Commandline Parameters: 1
      argv[1] = path to the input file

'''

#
#   Packages and modules
#

# The 'csv' module gives us access to a tool that will read CSV
# (Comma Separated Value) files and provide us access to each of
# the fields on each line in turn
import csv

# The 'sys' module gives us access to system tools, including the
# command line parameters, as well as standard input, output and error
import sys

#
# Define any "constants" for the file here.
# Names of constants should be in UPPER_CASE.
#


def main(argv):
  '''
    Main function in the script. Putting the body of the
    script into a function allows us to separate the local
    variables of this function from the global constants
    declared outside.
    '''

  #
  #   Check that we have been given the right number of parameters,
  #   and store the following two command line arguments variables with
  #   better names
  #
  if len(argv) != 2:
    print("Usage: question4.py <file_name> <province/Canada>")
    sys.exit(1)

  #
  #   The name of the file that we will read
  #
  file_name = argv[1]

  #
  # Ask the user for the duration of job vacancy
  #
  print(
      "Enter the number of the duration of job vacancy you are looking for: \n"
      "Your choices are: \n"
      "1. All job vacancies \n"
      "2. Less than 15 days \n"
      "3. 15 to 29 days \n"
      "4. 30 to 59 days \n"
      "5. 60 to 89 days \n"
      "6. 90 days or more \n"
      "7. 90 to 119 days \n"
      "8. 120 days or more")
  #
  #   Get the users input (although we focus on "less than 15 days" in our question)
  #
  int_choice_duration = get_valid_integer(1, 8)

  #
  #  Define dictionary for duration of job vacancy
  #
  job_vacancy_duration_dict = {
      1: 'Duration of job vacancy, all durations',
      2: 'Less than 15 days',
      3: '15 to 29 days',
      4: '30 to 59 days',
      5: '60 to 89 days',
      6: '90 days or more',
      7: '90 to 119 days',
      8: '120 days or more'
  }

  #
  #  Check if the choice exists in the dictionary
  #
  if int_choice_duration in job_vacancy_duration_dict:
    duration_of_job_vacancy = job_vacancy_duration_dict[int_choice_duration]
  else:
    print("Invalid choice. Please try again.")
    sys.exit(1)

  #
  #  Ask the user for the type of National Occupation Classification
  #
  print(
      "Enter the number of the type of National Occupation Classification you are looking for: \n"
      "Your choices are: \n"
      "1. All Occupations \n"
      "2. Management occupations \n"
      "3. Business, finance and administration occupations \n"
      "4. Natural and applied sciences and related occupations \n"
      "5. Health occupations \n"
      "6. Occupations in education, law and social, community and government services \n"
      "7. Occupations in art, culture, recreation and sport \n"
      "8. Sales and service occupations \n"
      "9. Trades, transport and equipment operators and related occupations \n"
      "10. Natural resources, agriculture and related production occupations \n"
      "11. Occupations in manufacturing and utilities")

  #
  #  Validate the input
  #
  int_choice_occupation = get_valid_integer(1, 11)

  #
  #  Define dictionary for the different occupation choices
  #
  occupation_choices_dict = {
    1: 'Total, all occupations',
    2: 'Management occupations [0]',
    3: 'Business, finance and administration occupations [1]',
    4: 'Natural and applied sciences and related occupations [2]',
    5: 'Health occupations [3]',
    6: 'Occupations in education, law and social, community, and government services [4]',
    7: 'Occupations in art, culture, recreation, and sport [5]',
    8: 'Sales and service occupations [6]',
    9: 'Trades, transport, and equipment operators and related occupations [7]',
    10: 'Natural resources, agriculture, and related production occupations [8]',
    11: 'Occupations in manufacturing and utilities [9]',
    12: 'Unclassified occupations'
  }

  #
  #  Check if the choice exists in the dictionary
  #
  if int_choice_occupation in occupation_choices_dict:
    occupation_choice = occupation_choices_dict[int_choice_occupation]
  else:
    print("Invalid choice. Please try again.")
    sys.exit(1)

  #
  #  Now we try to open the file for reading
  #
  try:
    # Open the file for reading
    with open(file_name, encoding="utf-8") as csv_file, open('dataForPlotting.csv', 'w', newline='', encoding='utf-8') as out_file:

        # Create a reader object that will read from the opened csv file
        csv_reader = csv.reader(csv_file, delimiter=',')
        csv_writer = csv.writer(out_file)


        # Print the header
        header = ["Ref Date", "Geo", "National Occupation Classification", "Recruitment Strategy", "Statistics", "Value"]
        print_and_write_csv(csv_writer, header)
        for row in csv_reader:

            # Check if the row is empty
            if not row:  # If row is empty, skip to the next iteration
              continue

            # Attempt to unpack the row into variables
            try:
              ref_date = row[0]
              geo = row[1]
              national_occupation_classification = row[3]
              job_characteristic = row[4]
              statistics = row[5]
              value = row[12]
              # print(f"{ref_date}, {geo}, {national_occupation_classification}, {job_characteristic}, {statistics}, {value or 0}")

              # Matching user-selected criteria
              if (national_occupation_classification == occupation_choice and job_characteristic == duration_of_job_vacancy):
                # Print rows with valid 'value'
                print(f"{ref_date}, {geo}, {national_occupation_classification}, {job_characteristic}, {statistics}, {value or 0}")
                data_row = [ref_date, geo, national_occupation_classification, job_characteristic, statistics, value or 0]
                print_and_write_csv(csv_writer, data_row)
            except ValueError as e:
                print(f"Error processing row: {e}, row data: {row}")

  # Handle file not found error
  except FileNotFoundError:
    print(f"File not found: {file_name}")

  # Handle unexpected errors
  except Exception as e:
    print(f"An unexpected error occurred: {e}")

#
#  Defining the function to get a valid integer value
#
def get_valid_integer(lower_bound, upper_bound):
  while True:
    try:
      user_input = int(input("Enter your choice: "))
      if lower_bound <= user_input <= upper_bound:
        return user_input
      else:
        print(
            f"Please enter an integer between {lower_bound} and {upper_bound}."
        )
    except ValueError:
      print("Please enter a valid integer.")

def print_and_write_csv(csv_writer, data):
  # Convert all items in 'data' to strings and join with commas for printing
  print_str = ', '.join(map(str, data))
  print(print_str)  # Print to terminal
  csv_writer.writerow(data)  # Write to CSV

if __name__ == "__main__":
  main(sys.argv)
