

import csv
import datetime

# our I/O files that will be used to perform the project with
file_input = "raw_data/employee_data1.csv"
file_output = "Answer/reformatted_employee_data.csv"

# Dictionary of states with abbreviations as the value
us_state_abbrev = {
    "Alabama": "AL",
    "Alaska": "AK",
    "Arizona": "AZ",
    "Arkansas": "AR",
    "California": "CA",
    "Colorado": "CO",
    "Connecticut": "CT",
    "Delaware": "DE",
    "Florida": "FL",
    "Georgia": "GA",
    "Hawaii": "HI",
    "Idaho": "ID",
    "Illinois": "IL",
    "Indiana": "IN",
    "Iowa": "IA",
    "Kansas": "KS",
    "Kentucky": "KY",
    "Louisiana": "LA",
    "Maine": "ME",
    "Maryland": "MD",
    "Massachusetts": "MA",
    "Michigan": "MI",
    "Minnesota": "MN",
    "Mississippi": "MS",
    "Missouri": "MO",
    "Montana": "MT",
    "Nebraska": "NE",
    "Nevada": "NV",
    "New Hampshire": "NH",
    "New Jersey": "NJ",
    "New Mexico": "NM",
    "New York": "NY",
    "North Carolina": "NC",
    "North Dakota": "ND",
    "Ohio": "OH",
    "Oklahoma": "OK",
    "Oregon": "OR",
    "Pennsylvania": "PA",
    "Rhode Island": "RI",
    "South Carolina": "SC",
    "South Dakota": "SD",
    "Tennessee": "TN",
    "Texas": "TX",
    "Utah": "UT",
    "Vermont": "VT",
    "Virginia": "VA",
    "Washington": "WA",
    "West Virginia": "WV",
    "Wisconsin": "WI",
    "Wyoming": "WY",
}

# variabels for reformatted values
emp_ids = []
emp_first_names = []
emp_last_names = []
emp_dobs = []
emp_ssns = []
emp_states = []

# Read the csv and convert it into a list of dictionaries
with open(file_input) as data:
    file = csv.DictReader(data)

    # Loop through each row, re-grab each field and store in a new list
    for row in file:

        # Grab emp_ids and store it into a list
        emp_ids = emp_ids + [row["Emp ID"]]

        # Grab names, split them, and store them in a temporary variable
        split_name = row["Name"].split(" ")

        # Then save first and last name in separate lists
        emp_first_names = emp_first_names + [split_name[0]]
        emp_last_names = emp_last_names + [split_name[1]]

        # Grab DOB and reformat it
        reformatted_dob = datetime.datetime.strptime(row["DOB"], "%Y-%m-%d")
        #set date to be 00/00/0000
        reformatted_dob = reformatted_dob.strftime("%m/%d/%Y")

        # Then store it into a list
        emp_dobs = emp_dobs + [reformatted_dob]

        # Grab SSN and reformat it
        split_ssn = list(row["SSN"])
        split_ssn[0:3] = ("*", "*", "*")
        split_ssn[4:6] = ("*", "*")
        joined_ssn = "".join(split_ssn)

        # Then store it into a list
        emp_ssns = emp_ssns + [joined_ssn]

        # Grab the states and use the dictionary to find the replacement by using key and value method
        state_abbrev = us_state_abbrev[row["State"]]

        # Then store the abbreviation into a list
        emp_states = emp_states + [state_abbrev]

# Zip all of the new lists together
empdb = zip(emp_ids, emp_first_names, emp_last_names,
            emp_dobs, emp_ssns, emp_states)

# output election data to the answer file
with open(file_output, "w", newline="") as df:
    writer = csv.writer(df)
    writer.writerow(["Emp ID", "First Name", "Last Name",
                     "DOB", "SSN", "State"])
    writer.writerows(empdb)
