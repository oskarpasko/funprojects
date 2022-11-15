def file_reader():
    absolute_path = '/Users/oskarpasko/Documents/GitHub/FunProjects/PythonTemplates/files/pi_digits.txt'
    with open(absolute_path) as file_object:
        contents = file_object.read()
    print(contents)

# function with try except block
def try_except(first, second):

    # block where the error could be
    try:
        # example: 5/0
        return first / second
    # block with Error Division
    except ZeroDivisionError:
        return "Nie dzielimy przez 0!"
    # else:
    #   operations
    # finally:
    #   operations