from classical_cryptography.classical_ciphers_menu import classical_ciphers_menu
from modern_cryptography.modern_cryptography_menu import modern_cryptography_menu
from tools.terminal_cleaner import clear_terminal

def display_menu():
    print("---- Menu ----")
    print("1) Classical Cryptography")
    print("2) Modern Cryptography")
    print("Q) Quit.")

def main():
    while True:
        display_menu()
        choice = input("Enter choice: ")
        choice = choice.lower()
        print()

        if choice == "1":
            clear_terminal()
            classical_ciphers_menu()

        elif choice == "2":
            clear_terminal()
            modern_cryptography_menu()

        elif choice == "q":
            clear_terminal()
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()