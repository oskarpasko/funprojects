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
            N = int(input(f"{Colors.CYAN}Podaj n: {Colors.END}"))
            print(f"{Colors.LIGHT_GREEN}{N}! = {factorial(N)}{Colors.END}")
        case '3':
            print(f"{Colors.CYAN}Podaj n oraz k, (0<=k<=n){Colors.END}")
            N = int(input(f"{Colors.CYAN}Podaj n: {Colors.END}"))
            K = int(input(f"{Colors.CYAN}Podaj k: {Colors.END}"))
            if(K >= 0 and N >= K):
                print(f"{Colors.LIGHT_GREEN}{N}! / {K}!({N} - {K})! = {newton_symbol(N, K)}{Colors.END}")
        case '4':
            quadratic_function()
        case '5':
            errors()
        case '6':
            exit()
        case _:
            print('Error 890!')
