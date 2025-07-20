# Write your code here.
# Task 1: Hello
def print_hello():
    return "Hello!"

print_hello()

# Task 2: Greet with a Formatted String
def greet(name):
    return "Hello " + name + "!"

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
    try: 
        average = sum(args) / len(args)
    except:
        return "Invalid data was provided."
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"
   
    
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

# Task 8: Titleize, with String and List Operations
def titleize(text):
    little_words = ["a", "on", "an", "the", "of", "and", "is", "in"]
    words = text.lower().split()

    result = []
    for i, word in enumerate(words):
        if i == 0 or i == len(words) - 1 or word not in little_words:
            result.append(word.capitalize())
        else:
            result.append(word)

    return " ".join(result)

# Task 9: Hangman, with more String Operations
def hangman(secret, guess):
    result = ""
    for letter in secret:
        if letter in guess:
            result += letter
        else:
            result += "_"
    return result

# Task 10: Pig Latin, Another String Manipulation Exercise
def pig_latin(text):
    vowels = "aeiou"
    words = text.split()
    result = []

    for word in words:
        if word.startswith("qu"):
            # Move "qu" to the end
            pig_word = word[2:] + "quay"
        elif word[0] in vowels:
            # Starts with a vowel
            pig_word = word + "ay"
        else:
            # Starts with one or more consonants
            index = 0
            while index < len(word) and word[index] not in vowels:
                if word[index] == 'q' and index + 1 < len(word) and word[index + 1] == 'u':
                    index += 2
                    break
                index += 1
            pig_word = word[index:] + word[:index] + "ay"
        result.append(pig_word)

    return " ".join(result)



    
    
    



