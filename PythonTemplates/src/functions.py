def file_reader():
    absolute_path = '/Users/oskarpasko/Documents/GitHub/FunProjects/PythonTemplates/files/pi_digits.txt'
    with open(absolute_path) as file_object:
        contents = file_object.read()
    print(contents)