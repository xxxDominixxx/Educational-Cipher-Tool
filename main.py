from ciphers.classical_ciphers_menu import classical_ciphers_menu
from tools.terminal_cleaner import clear_terminal

def display_menu():
    print("---- Menu ----")
    print("1) Classical ciphers")
    print("2) Other ciphers")
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
            print("Other cipher")   #Replace later when another function is created

        elif choice == "q":
            clear_terminal()
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()