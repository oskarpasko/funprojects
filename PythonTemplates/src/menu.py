from .settings import Colors

def menu():
    print(f"{Colors.BLUE}1. File Reader{Colors.END}")
    print(f"{Colors.BLUE}2. Try Except{Colors.END}")

if __name__ == '__main__':
    menu()