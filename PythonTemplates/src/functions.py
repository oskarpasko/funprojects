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
