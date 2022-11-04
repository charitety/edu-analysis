import csv
list_data = []
with open("edu-analysis/states_all.csv", "r") as infile:
    # load in data as DictReader
    reader = csv.DictReader(infile)
    for row in reader:
        list_data.append(row)

single_state = [row for row in list_data if row['STATE']== 'NEW YORK']

new_data = [row for row in single_state if row["FEDERAL_REVENUE"] != '']
"""Potential fuctions
get_highest_gdp(data, year):
get_lowest_gdp(data, year):
get_state_gdp(data, state, year):"""