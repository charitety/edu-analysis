import csv
list_data = []
with open("edu-analysis/states_all.csv", "r") as infile:
    # load in data as DictReader
    reader = csv.DictReader(infile)
    for row in reader:
        list_data.append(row)

#Obtaining the number of rows
print(len(list_data))

#Obtaining the number of columns or keys in data
print(len(list_data[0]))

#Selecting one state to analyze
state_data = [row for row in list_data if row['STATE']=='NEW_YORK']
print(state_data)

#Choosing to analyze reading score for 4th graders and filtering the rows with no data
state_data = [row for row in state_data if row['AVG_READING_4_SCORE'] != '']
print(state_data)

#Getting the value of YEAR by accessing the dictionary
years = [(row['YEAR']) for row in state_data]
print(years)

#Definining a function to analyze percentage of change from one year to another
def percent_change(data, year1, year2, column):
    """
    Calculate the percentage of change in state education
    Parameters
    ----------
    data : list 
        U.S. Education data between 1986 and 2019. Some years are missing.
    year1 : str
        Beginning year of analysis period
    year2 : str
        Final year of analysis period
    column : str
        contains scores per grade in a given category e.g. reading or math
    
    Returns
    -------
    percentage change : float

    """



