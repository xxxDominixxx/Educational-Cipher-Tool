from tools.terminal_cleaner import clear_terminal
from modern_cryptography.aes.aes_menu import aes_menu
from modern_cryptography.rsa.rsa_menu import rsa_menu

def info():
    print("Modern cryptography uses mathematical algorithms")
    print("and computational techniques to protect information.")
    print("It provides methods for encryption, authentication,")
    print("data integrity, digital signatures, and key exchange.")
    print("These methods help protect confidentiality, verify")
    print("the authenticity of information, detect modifications,")
    print("and establish shared secret keys for secure communication.")
    print("Modern cryptographic methods are designed to resist")
    print("attacks using current computational techniques.")

def display_menu():
    print("---- Modern Cryptography ----")
    print("1) AES - Advanced Encryption Standard")
    print("2) RSA - Asymmetric Key Pairs")
    print("R) Return.")
    print()

def modern_cryptography_menu():
    while True:

        info()
        print()
        input("Press Enter to continue...")

        clear_terminal()
        display_menu()

        choice = input("Enter your choice: ")
        choice = choice.lower()

        if choice == "1":
            clear_terminal()
            aes_menu()

        elif choice == "2":
            clear_terminal()
            rsa_menu()

        elif choice == "r":
            clear_terminal()
            break

        else:
            print("Invalid choice. Try again.")