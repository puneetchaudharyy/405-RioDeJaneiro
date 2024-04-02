#!/usr/bin/env python
'''
plotting.py
  Author(s): Puneet Chaudhary (1231356), Krish Garg (1275663), Yash Tandon (1258096)

  Project: Job Vacancies in Canada Visualization Tool
  Date of Last Update: April 1, 2024

  Functional Summary:
    This script visualizes job vacancy data in Canada based on user-selected job characteristics and National Occupational Classification (NOC). It outputs the data as a bar graph to display trends over time.

    The script prompts users to input their choice of job characteristics and NOC categories. It then processes the data and generates a bar graph reflecting the trends.

    Commandline Parameters: 1
    1. A path to a CSV file that contains the job vacancy data to be plotted.

  This script is part of a suite of tools designed to provide insights into the Canadian job market.
'''
#
#   Packages and modules
#
# The following imports are necessary for the script to process data and generate visualizations.
# 'sys' is used for accessing command line parameters
#
import sys

#
# 'matplotlib.pyplot' for creating visualizations
#
import matplotlib.pyplot as plt

#
# pandas' for handling data in a structured way.
#
import pandas as pd


def main(csv_file):
  '''
    Main function of the script. This function is responsible for reading the CSV file,
    processing the job vacancy data, and plotting it on a bar graph to visualize trends
    based on user-selected job characteristics and NOC categories.

    Parameters:
    csv_file (str): The path to the CSV file containing job vacancy data.

    Returns:
    None: This function does not return any value; its purpose is to generate a plot.
  '''

  # Read the CSV file into a pandas DataFrame
  data = pd.read_csv(csv_file)

  # Convert the 'Ref Date' column to datetime objects for proper plotting
  data['Ref Date'] = pd.to_datetime(data['Ref Date'], format='%Y-%m')

  # Initialize the plot with a specified figure size
  plt.figure(figsize=(10, 6))

  # Create a line plot of 'Ref Date' vs 'Value' with markers and a solid line style
  plt.plot(data['Ref Date'], data['Value'], marker='o', linestyle='-')

  # Set the title of the plot
  plt.title('Job Vacancies Over Time')

  # Label the x-axis as 'Date'
  plt.xlabel('Date')

  # Label the y-axis as 'Number of Job Vacancies'
  plt.ylabel('Number of Job Vacancies')

  # Rotate the x-axis date labels for better readability
  plt.xticks(rotation=45)

  # Adjust the layout to ensure labels and titles are not cut off
  plt.tight_layout()

  # Display the plot to the user
  plt.show()  

#
#   Main control flow
#
if __name__ == "__main__":
  if len(sys.argv) != 2:
    print("Usage: python plotting.py <csv_file>")
    sys.exit(1)
  csv_file = sys.argv[1]
  main(csv_file)