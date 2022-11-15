def file_reader():
    absolute_path = '/Users/oskarpasko/Documents/GitHub/FunProjects/PythonTemplates/files/pi_digits.txt'
    with open(absolute_path) as file_object:
        contents = file_object.read()
    print(contents)

def try_except(first, second):
    try:
        first / second
    except ZeroDivisionError:
        return "Nie dzielimy przez 0!"
    else:
        return first / second