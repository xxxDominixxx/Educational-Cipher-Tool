from ciphers.classical_ciphers.Caesar.caesar_menu import caesar_menu
from ciphers.classical_ciphers.Atbash import atbash_menu
from ciphers.classical_ciphers.Vigenere import vigenere_menu
from ciphers.classical_ciphers.Affine import affine_menu
from ciphers.classical_ciphers.Rail_Fence import rail_fence_menu
from ciphers.classical_ciphers.Columnar_Transposition import columnar_transposition_menu
from tools.terminal_cleaner import clear_terminal

def info():
    print("Classical ciphers are historical encryption methods that")
    print("rely on manual techniques or simple mechanical devices")
    print("rather than digital computers.")
    print("Most classical ciphers are relatively easy to break")
    print("using modern technology and can often be solved manually as well.")

def display_menu():
    print("---- Classical Ciphers ----")
    print("1) Caesar cipher")
    print("2) Atbash cipher")
    print("3) Vigenere cipher")
    print("4) Affine cipher")
    print("5) Rail Fence cipher")
    print("6) Columnar Transposition cipher")
    print("R) Return.")
    print()

def classical_ciphers_menu():
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
            caesar_menu()

        elif choice == "2":
            clear_terminal()
            atbash_menu()

        elif choice == "3":
            clear_terminal()
            vigenere_menu()

        elif choice == "4":
            clear_terminal()
            affine_menu()

        elif choice == "5":
            clear_terminal()
            rail_fence_menu()

        elif choice == "6":
            clear_terminal()
            columnar_transposition_menu()

        elif choice == "r":
            clear_terminal()
            break

        else:
            print("Invalid choice. Try again.")