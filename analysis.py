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
print(len(state_data))

new_data = [row for row in state_data if row['AVG_READING_4_SCORE']]
print(len(new_data))
"""Potential fuctions
get_highest_gdp(data, year):
get_lowest_gdp(data, year):
get_state_gdp(data, state, year):"""