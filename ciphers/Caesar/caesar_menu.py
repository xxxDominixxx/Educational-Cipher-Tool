from .caesar_numeric_shift import caesar_numeric_shift_menu
from .caesar_letter_key import caesar_letter_key_menu
from tools.terminal_cleaner import clear_terminal

# Function used to print information about the cipher
def info():
    print("The Caesar cipher is a simple way to encrypt messages.")
    print("It shifts each letter a set number of places in the alphabet.")
    print("It is named after Julius Caesar, who used it to encode messages in his correspondence.")
    print()
    print("There are two versions of this cipher in this program.")
    print("The numeric shift version uses a number to decide how far")
    print("each letter is shifted.")
    print()
    print("The letter key version uses a letter to decide the shift.")
    print("Each letter has a numerical value based on its position in the alphabet.")
    print("A = 0, B = 1, C = 2, and so on up to Z = 25.")

#=================================================================#

def caesar_menu():
    while True:

        info()
        print()
        input("Press Enter to continue...")

        print()
        print("=== Caesar Cipher ===")
        print("1) Caesar Numeric Shift Variant")
        print("2) Caesar Letter Key Variant")
        print("E) Exit") 

        choice = input("Enter your choice: ")
        choice = choice.lower()

        if choice == "1":
            caesar_numeric_shift_menu()

        elif choice == "2":
            caesar_letter_key_menu()

        elif choice == "e":
            clear_terminal()
            break

        else:
            print("Invalid choice. Try again.")