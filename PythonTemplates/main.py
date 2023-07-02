from src.settings import Colors
from src.menu import menu
from src.functions import *

print(f"{Colors.YELLOW}Some templates in Python. Rather for devs than users :){Colors.END}")

menu()
choice = input(f'{Colors.CYAN}Choose option: {Colors.END}')


# simple match case
match(choice):
    case '1':
        file_reader()
    case '2':
        print(try_except(5, 0))
    case '3':
        json_save_data()
    case '4':
        json_load_data()
    case '5':
        csv_load_data()