from src.algorithms import *
from src.errors import errors
from src.menu import display_menu

print(' =================================== ')
print('        Welcome in Mathmatica')
print(' =================================== ')

print('\n')

while(True):

    display_menu()

    choice = input("Choose option: ")

    match(choice):
        case '1':
            exponentation()
        case '2':
            errors()
        case '3':
            exit()
        case _:
            print('Error 890!')
