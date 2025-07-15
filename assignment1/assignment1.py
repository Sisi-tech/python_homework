# Write your code here.
# Task 1: Hello
def print_hello():
    print("Hello!")

print_hello()

# Task 2: Greet with a Formatted String
def greet(name):
    print("Hello ", + name.toUppercase() + "!")

greet("Jean")

# Task 3: Calculator
def calc(first, second, third="multiply"):
    try:
        if third == "add":
            return first + second
        elif third == "subtract":
            return first - second
        elif third == "multiply":
            return first * second
        elif third == "divide":
            return first / second
        elif third == "modulo":
            return first % second
        elif third == "int_divide":
            return first // second
        elif third == "power":
            return first ** second
        else:
            return "Invalid operation"
    except ZeroDivisionError:
        return "You can't divide by 0!"
    except TypeError:
        return "You can't multiply those values!"


def calc(first, second, third="multiply"):
    try:
        match third:
            case "add":
                return first + second
            case "subtract":
                return first - second
            case "multiply":
                return first * second
            case "divide":
                return first / second
            case "modulo":
                return first % second
            case "int_divide":
                return first // second
            case "power":
                return first ** second
            case _:
                return "Unknown operation"
    except ZeroDivisionError:
        return "You can't divide by 0!"
    except TypeError:
        return "You can't multiply those values!"
# Task 4: Data type conversion
def data_type_conversion(value, data_type):
    try:
        if data_type == "int":
            return int(value)
        elif data_type == "float":
            return float(value)
        elif data_type == "str":
            return str(value)
        else:
            return f"Unsupported data type: {data_type}"
    except (ValueError, TypeError):
        return f"You can't convert {value} into a {data_type}."
# Task 5: Grading system, using *args
def grade(*args):
    average = sum(args) / len(args)
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "Below 60"
    
# Task 6: Use a for loop with a range
def repeat(string, count):
    result = ""
    for _ in range(count):
        result += string 
    return result 

# Task 7: Student Scores, Using **kwargs
def student_scores(positional, **kwargs):
    if not kwargs:
        return "No student data provided."
    if positional == "best":
        best_student = max(kwargs, key=kwargs.get)
        return best_student
    elif positional == "mean":
        average_score = sum(kwargs.values()) / len(kwargs)
        return average_score
    else:
        return "Invalid positional selected."
    
print(student_scores("best", Alice=92, Bob=87, Charlie=78))   
print(student_scores("mean", Alice=92, Bob=87, Charlie=78))  
print(student_scores("top", Alice=92, Bob=87))                
print(student_scores("best")) 



    
    
    



