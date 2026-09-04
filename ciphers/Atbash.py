from tools.terminal_cleaner import clear_terminal

alphabet_uppercase = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
                      "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
alphabet_lowercase = [letter.lower() for letter in alphabet_uppercase]

def info():
    print("The Atbash cipher is a simple way to encrypt messages.")
    print("It replaces each letter with its corresponding letter")
    print("from the opposite end of the alphabet.")
    print()
    print("For example, A becomes Z, B becomes Y, C becomes X,")
    print("and so on until Z becomes A.")
    print()
    print("The same process is used for both encryption and decryption.")

# Letter encryption/decryption function
def crypt_letter(character, alphabet):
    position = alphabet.index(character)
    new_position = 25 - position

    return alphabet[new_position]


# Text encryption/decryption function --- uses crypt_letter function
def crypt_text(text):
    result = ""

    character_list = list(text)     # Divide original text into a list of characters

    for character in character_list:

        # Handles Upper Case Letters
        if character in alphabet_uppercase:
            result = result + crypt_letter(character, alphabet_uppercase)

        # Handles Lower Case Letters
        elif character in alphabet_lowercase:
            result = result + crypt_letter(character, alphabet_lowercase)

        # Handles everything else that is not a letter
        else:
            result = result + character

    return result


# Function that formats the result
def display_result(original, result, operation):
    print()
    print("Original message:", original)
    print(operation + " message:", result)


#=======================================================================================#
def atbash_menu():

    info()      #Prints information once

    while True:
        print()
        print("=== Atbash Cipher ===")
        print("1) Encrypt")
        print("2) Decrypt")
        print("I) Information")
        print("R) Return")

        choice = input("Enter your choice: ")
        choice = choice.lower()

        if choice == "1":
            text = input("Enter text you would like to encrypt: ")

            result = crypt_text(text)

            display_result(text, result, "Encrypted")

        elif choice == "2":
            text = input("Enter encrypted text you would like to decrypt: ")

            result = crypt_text(text)

            display_result(text, result, "Decrypted")

        elif choice == "i":
            info()
            print()

        elif choice == "r":
            clear_terminal()
            break

        else:
            print("Invalid choice. Try again.")