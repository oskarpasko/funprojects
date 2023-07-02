import json

def file_reader():
    absolute_path = '/Users/oskarpasko/Documents/GitHub/FunProjects/PythonTemplates/files/pi_digits.txt'
    with open(absolute_path) as file_object:
        contents = file_object.read()
    print(contents)

# function with try except block
def try_except(first, second):

    try: 
        # check if error exist
        first / second
    except ZeroDivisionError: 
        # definition which error we except
        return "Nie dzielimy przez 0!" 
    else: 
        # what we do if everything is all right
        return first / second
    # finally:
    #   operations
def json_save_data():
    # import json

    # numbers to save
    numbers = [2, 3, 5, 7, 11, 13]
    # absolute file's path where we'll save numbers
    file_absoulte_path = "/Users/oskarpasko/Documents/GitHub/FunProjects/PythonTemplates/files/numbers.json"

    # save numbers to file named numbers.json
    with open(file_absoulte_path, 'w') as file:
        json.dump(numbers, file)

def json_load_data():
    # import json

    # absolute file's path where we'll save numbers
    file_absoulte_path = "/Users/oskarpasko/Documents/GitHub/FunProjects/PythonTemplates/files/numbers.json"

    with open(file_absoulte_path) as file:
        numbers = json.load(file)
    print(numbers)

def csv_load_data():
    # loading data from csv files
    import csv

    filename = "PythonTemplates\\files\\flights_flightData.csv"
 
    with open(filename, 'r') as data:
        for line in csv.DictReader(data):
            print(line)
