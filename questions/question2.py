#!/usr/bin/env python
'''
question3.py
  Author(s): Puneet Chaudhary (1231356), Krish Garg (1275663), Yash Tandon (1258096)

  Project: Job Vacancies in Canada
  Date of Last Update: April 1, 2024

  Functional Summary
    This script processes a CSV file containing job vacancy data across Canada, focusing on
    filtering and displaying data based on the minimum experience required for the jobs.

    Expected fields in the dataset include:
      1. The date of the report
      2. The geographic location of the report (e.g., Canada or specific province)
      3. The type of National Occupational Classification
      4. The minimum experience required for the job vacancies
      5. The job vacancy count

    Users are prompted to select the type of minimum experience required, and the script
    filters and displays matching job vacancy data to the console.

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
    print("Usage: question2.py <file_name> <province/Canada>")
    sys.exit(1)

  # 
  #   The name of the file that we will read
  #
  file_name = argv[1]
   
  #
  # National Occupation Classification (NOC) selection
  #
  print("Enter the number of the type of National Occupation Classification you are looking for: \n"
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
  noc_choice = get_valid_integer(1, 11)

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
  if noc_choice in occupation_choices_dict:
    selected_noc = occupation_choices_dict[noc_choice]
  else:
    print("Invalid choice. Please try again.")
    sys.exit(1)

    #
    # User input for selection of the minimum education level required
    #
  print("Enter the type of minimum education level required: \n"
          "1. Minimum level of education required, all levels \n"
          "2. No minimum level of education required \n"
          "3. High school diploma or equivalent \n"
          "4. Non-university certificate or diploma \n"
          "5. University certificate or diploma below bachelor's level \n"
          "6. Bachelor's degree \n"
          "7. University certificate, diploma or degree above the bachelor's level")
  education_choice = get_valid_integer(1, 7)

  #
  #  Define dictionary for the different education levels
  #
  education_levels = {
        1: "Minimum level of education required, all levels",
        2: "No minimum level of education required",
        3: "High school diploma or equivalent",
        4: "Non-university certificate or diploma",
        5: "University certificate or diploma below bachelor's level",
        6: "Bachelor's degree",
        7: "University certificate, diploma or degree above the bachelor's level"
    }
  if education_choice in education_levels:
    selected_education_level = education_levels[education_choice]
  else:
    print("Invalid choice. Please try again.")
    sys.exit(1)

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

            # Matching user-selected criteria
          if (national_occupation_classification == selected_noc and job_characteristic == selected_education_level):
              # Print rows with valid 'value'
            print(f"{ref_date}, {geo}, {national_occupation_classification}, {job_characteristic}, {statistics}, {value or 0}")
            data_row = [ref_date, geo, national_occupation_classification, job_characteristic, statistics, value or 0]
            print_and_write_csv(csv_writer, data_row)
            
        except ValueError as e:
                print(f"Error processing row: {e}, row data: {row}")   
          
  except FileNotFoundError:
          print(f"File not found: {file_name}")
          sys.exit(2)
  except Exception as e:
          print(f"An unexpected error occurred: {e}")
          sys.exit(3)

def get_valid_integer(lower_bound, upper_bound):
    '''
    Utility function to ensure user input is a valid integer within specified bounds.
    '''
    while True:
        try:
            user_input = int(input("Please enter your choice: "))
            if lower_bound <= user_input <= upper_bound:
                return user_input
            else:
                print(f"Please enter an integer between {lower_bound} and {upper_bound}.")
        except ValueError:
            print("Please enter a valid integer.")

def print_and_write_csv(csv_writer, data):
  # Convert all items in 'data' to strings and join with commas for printing
  print_str = ', '.join(map(str, data))
  print(print_str)  # Print to terminal
  csv_writer.writerow(data)  # Write to CSV

if __name__ == "__main__":
    main(sys.argv)