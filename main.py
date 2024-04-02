#!/usr/bin/env python
'''
main.py
  Author(s): Puneet Chaudhary (1231356), Krish Garg (1275663), Yash Tandon (1258096)

  Project: Job Vacancies in Canada
  Date of Last Update: April 1, 2024

  Functional Summary

    There are expected to be  fields:
      1. User choice of the function it wants to use 

      The script asks users to input the choice of the function they want to use. It then calls the function based on the user's choice.
      
    Commandline Parameters: 0

'''
#
#  The os module in Python provides a portable way of using operating system dependent functionality. It allows Python code to interact with the operating system by providing
#  functions to operate on file paths, directories, processes, and environment variables. The os module is particularly useful for tasks such as file manipulation, directory          #   operations, and executing system commands.
import os


#
# Define any "constants" for the file here.
# Names of constants should be in UPPER_CASE.
#
def main():
  '''
    Main function in the script. Putting the body of the
    script into a function allows us to separate the local
    variables of this function from the global constants
    declared outside.
    '''

  user_choice = int(
      input(
          "Enter the question number to execute (1-4): \n"
          "1. Question 1: What is the proportion of job vacancies for people who got their job through social media quarterly, without adjusting for seasonality, in Canada? \n"
          "2. Question 2: What is the proportion of job vacancies for people with more than 8 years of experience quarterly, without adjusting for seasonality, in Canada? \n"
          "3. What is the proportion of job vacancies, with no minimum level of education required quarterly, without adjusting for seasonality, in Canada? \n"
          "4. What is the proportion of job vacancies  last for less than 15 days on the market before they are filled quarterly, without adjusting for seasonality, in Canada? \n"
        "Enter your choice: "
      ))

  #
  #  Runnning the function based on the user choice
  #    
  if user_choice == 1:
    os.system("python questions/question1.py dataFiles/dataForQuestion1.csv")
    os.system("python plotting.py dataForPlotting.csv")
  elif user_choice == 2:
    os.system("python questions/question2.py dataFiles/dataForQuestion2.csv")
    os.system("python plotting.py dataForPlotting.csv")
  elif user_choice == 3:
    os.system("python questions/question3.py dataFiles/dataForQuestion3.csv")
    os.system("python plotting.py dataForPlotting.csv")
  elif user_choice == 4:
    os.system("python questions/question4.py dataFiles/dataForQuestion4.csv")
    os.system("python plotting.py dataForPlotting.csv")

  else:
    print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
  main()
