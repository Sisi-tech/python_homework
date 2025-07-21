# Re-push assignment2. Didn't push assignment2 successfully last time.
# Task 2: Read a CSV File
import csv
import sys 
import os 
import custom_module
from datetime import datetime 

def read_employees():
    data = {}
    rows = []
    try:
        with open("../csv/employees.csv", newline="") as file:
            reader = csv.reader(file)
            for index, row in enumerate(reader):
                if index == 0:
                    data["fields"] = row 
                else:
                    rows.append(row)
        data["rows"] = rows 
        return data 
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        sys.exit(1)

employees = read_employees()
print(employees)

# Task 3: Find the Column Index
def column_index(value):
    return employees["fields"].index(value)

employee_id_column = column_index("employee_id")
print(employee_id_column)

# Task 4: Find the Employee First Name
def first_name(row_num):
    col_index = column_index("first_name")
    return employees["rows"][row_num][col_index]

print(first_name(0))

# Task 5: Find the Employee: a Function in a Function
def employee_find(employee_id):
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id 
    matches = list(filter(employee_match, employees["rows"]))
    return matches 

# Task 6: Find the Employee with a Lambda
def employee_find_2(employee_id):
    matches = list(filter(lambda row : int(row[employee_id_column]) == employee_id, employees["rows"])) 
    return matches 

# Task 7: Sort the Rows by last_name Using a Lambda
def sort_by_last_name():
    last_name_index = column_index("last_name")
    employees["rows"].sort(key=lambda row: row[last_name_index])
    return employees["rows"]

# Task 8: Create a dict for an Employee
def employee_dict(row):
    res = {}
    for key, value in zip(employees["fields"], row):
        if key != "employee_id":
            res[key] = value
    return res 

# Task 9: A dict of dicts, for All Employees
def all_employees_dict():
    res = {}
    for row in employees["rows"]:
        employee_id = int(row[employee_id_column])
        res[employee_id] = employee_dict(row)
    return res 

# Task 10: Use the os Module
def get_this_value():
    return os.getenv("THISVALUE")

print(get_this_value())

# Task 11: Creating Your Own Module
def set_that_secret(secret):
    custom_module.set_secret(secret)
set_that_secret("this is a secret")
print(custom_module.secret)

# Task 12: Read minutes1.csv and minutes2.csv
def read_csv_to_dict(path):
    data = {}
    rows = []
    try:
        with open(path, newline="") as file:
            reader = csv.reader(file)
            for index, row in enumerate(reader):
                if index == 0:
                    data["fields"] = row 
                else:
                    rows.append(tuple(row))
            data["rows"] = rows 
    except Exception as e:
        print(f"Error reading file {path}: {e}")
        sys.exit(1)
    return data 

def read_minutes():
    minutes1 = read_csv_to_dict("../csv/minutes1.csv")
    minutes2 = read_csv_to_dict("../csv/minutes2.csv")
    return minutes1, minutes2 

minutes1, minutes2 = read_minutes()
print(minutes1)
print(minutes2)

# Task 13: Create minutes_set
def create_minutes_set():
    set1 = set(minutes1["rows"])
    set2 = set(minutes2["rows"])
    combined = set1.union(set2)
    return combined 

# Task 14: Convert to datetime
def create_minutes_list():
    global minutes_set
    minutes_raw_list = list(minutes_set)
    converted = list(map(lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")), minutes_raw_list))

    return converted 

minutes_set = create_minutes_set()
minutes_list = create_minutes_list()
print(minutes_list)

# Task 15: Write Out Sorted List
def write_sorted_list():
    sorted_list = sorted(minutes_list, key=lambda x: x[1])
    formatted = list(map(lambda x: (x[0], x[1].strftime("%B %d, %Y")), sorted_list))
    try:
        with open("minutes.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(minutes1["fields"])
            writer.writerows(formatted)
    except Exception as e:
        print(f"Error writing file: {e}")
        sys.exit(1)
    return formatted 

final_minutes = write_sorted_list()
print(final_minutes)
