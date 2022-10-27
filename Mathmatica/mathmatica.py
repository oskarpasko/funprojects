from src.algorithms import *
from src.errors import errors
from src.menu import display_menu
from src.settings import Colors

print(f'{Colors.BLUE} =================================== {Colors.END}')
print(f'{Colors.BLUE}        Welcome in Mathmatica{Colors.END}')
print(f'{Colors.BLUE} =================================== {Colors.END}')

print('\n')

while(True):

    display_menu()

    choice = input(f"{Colors.YELLOW}Choose option: {Colors.END}")

    match(choice):
        case '1':
            exponentation()
        case '2':
            errors()
        case '3':
            exit()
        case _:
            print('Error 890!')
