from ciphers.Caesar.caesar_menu import caesar_menu
from ciphers.Atbash import atbash_menu
#this loads the entire caesar.py since
#one function from it is needed and therefore 
#all the functions in caesar.py can interract with each other.

from tools.terminal_cleaner import clear_terminal

def display_menu():
    print("---- Menu ----")
    print("1) Caesar cipher")
    print("2) Atbash cipher")
    print("3) Choice 3")
    print("Q) Quit.")

def main():
    while True:
        display_menu()
        choice = input("Enter choice: ")
        choice = choice.lower()
        print()

        if choice == "1":
            clear_terminal()
            caesar_menu()

        elif choice == "2":
            clear_terminal()
            atbash_menu()

        elif choice == "3":
            print("Choice three")
            print()

        elif choice == "q":
            break

if __name__ == "__main__":
    main()