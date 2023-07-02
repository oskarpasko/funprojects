from .settings import Colors

def menu():
    print(f"{Colors.BLUE}1. File Reader{Colors.END}")
    print(f"{Colors.BLUE}2. Try Except{Colors.END}")
    print(f"{Colors.BLUE}3. JSON save data{Colors.END}")
    print(f"{Colors.BLUE}4. JSON load data{Colors.END}")
    print(f"{Colors.BLUE}5. CSV load data{Colors.END}")


if __name__ == '__main__':
    menu()