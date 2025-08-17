"""
Task 1: Introduction to Pandas - Creating and Manipulating DataFrames
Create a DataFrame from a dictionary:

Use a dictionary containing the following data:
Name: ['Alice', 'Bob', 'Charlie']
Age: [25, 30, 35]
City: ['New York', 'Los Angeles', 'Chicago']
Convert the dictionary into a DataFrame using Pandas.
Print the DataFrame to verify its creation.
save the DataFrame in a variable called task1_data_frame and run the tests.

Add a new column:

Make a copy of the dataFrame you created named task1_with_salary (use the copy() method)
Add a column called Salary with values [70000, 80000, 90000].
Print the new DataFrame and run the tests.
Modify an existing column:

Make a copy of task1_with_salary in a variable named task1_older
Increment the Age column by 1 for each entry.
Print the modified DataFrame to verify the changes and run the tests.
Save the DataFrame as a CSV file:

Save the task1_older DataFrame to a file named employees.csv using to_csv(), do not include an index in the csv file.
Look at the contents of the CSV file to see how it's formatted.
Run the tests.
"""
import pandas as pd
print(pd.__version__)

# 1. Create a DataFrame from a dictionary:
task1_data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

task1_data_frame = pd.DataFrame(task1_data)
print(task1_data_frame)

# 2.Add a new column:
task1_with_salary = task1_data_frame.copy()
task1_with_salary['salary'] = [70000, 80000, 90000]
print(task1_with_salary)

# 3. Modify an existing column:
task1_older = task1_with_salary.copy()
task1_older['Age'] += 1
print(task1_older)

# 4. Save the DataFrame as a CSV file:
task1_older.to_csv('employees.csv', index=False)

read_task1 = pd.read_csv('employees.csv')
print("-- Read task1 ---")
print(read_task1)

"""
Task 2: Loading Data from CSV and JSON
Read data from a CSV file:

Load the CSV file from Task 1 into a new DataFrame saved to a variable task2_employees.
Print it and run the tests to verify the contents.
Read data from a JSON file:

Create a JSON file (additional_employees.json). The file adds two new employees. Eve, who is 28, lives in Miami, and has a salary of 60000, and Frank, who is 40, lives in Seattle, and has a salary of 95000.
Load this JSON file into a new DataFrame and assign it to the variable json_employees.
Print the DataFrame to verify it loaded correctly and run the tests.
Combine DataFrames:

Combine the data from the JSON file into the DataFrame Loaded from the CSV file and save it in the variable more_employees.
Print the combined Dataframe and run the tests.
"""
# 1. Read data from a CSV file:
task2_employees = pd.read_csv('employees.csv')
print("--- Task2: Loading Data from CSV and JSON ---")
print(task2_employees)

# 2. Read data from a JSON file:
json_employees = pd.read_json('additional_employees.json')
print("--print json_employees--")
print(json_employees)

# 3. Combine DataFrames:
more_employees = pd.concat([read_task1, json_employees], ignore_index=True)
print("--print combined DataFrame--")
print(more_employees)

# Task 3: Data Inspection - Using Head, Tail, and Info Methods
# 1. Use the head() method:
first_three = more_employees.head(3)
print("Print first three rows: first_three")
print(first_three)

# 2. Use the tail() method:
last_two = more_employees.tail(2)
print("--Print the last two rows--")
print(last_two)

# 3. Get the shape of a DataFrame
employee_shape = more_employees.shape 
print("--print employee_shape--")
print(employee_shape)

# 4. Use the info() method:
print("--print more_employees.info()--")
more_employees.info()

# Task 4: Data Cleaning
dirty_data = pd.read_csv('dirty_data.csv')
print("print dirty data:")
print(dirty_data)
clean_data = dirty_data.copy()
clean_data = clean_data.drop_duplicates()
print("print clean_data after removing duplicates:")
print(clean_data)
clean_data["Age"] = pd.to_numeric(clean_data["Age"], errors="coerce")
print(clean_data)
clean_data["Salary"] = pd.to_numeric(clean_data["Salary"], errors="coerce")
clean_data["Salary"] = clean_data["Salary"].replace(["unknown", "n/a"], pd.NA)
print(clean_data)
clean_data["Age"] = clean_data["Age"].fillna(clean_data["Age"].mean())
clean_data["Salary"] = clean_data["Salary"].fillna(clean_data["Salary"].median())
print(clean_data)
clean_data["Hire Date"] = pd.to_datetime(clean_data["Hire Date"])
print(clean_data)
clean_data["Name"] = clean_data["Name"].str.strip().str.upper()
clean_data["Department"] = clean_data["Department"].str.strip().str.upper()
print(clean_data)


