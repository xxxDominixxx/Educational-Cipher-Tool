from tools.terminal_cleaner import clear_terminal
from tools.alphabets import alphabet_uppercase, alphabet_lowercase

def info():
    print("The Vigenère cipher is a method of encrypting messages using a keyword.")
    print("Each letter of the keyword determines how far the corresponding")
    print("letter of the message is shifted through the alphabet.")
    print()
    print("For example, if the keyword is CAT:")
    print("C shifts a letter by 2 positions, A shifts by 0,")
    print("and T shifts by 19 positions.")
    print()
    print("The keyword repeats when the end of the keyword is reached.")
    print()
    print("The same keyword is used for encryption and decryption.")

# Letter encryption/decryption function
def crypt_letter(character, key_character, alphabet, encrypt=True):

    character_position = alphabet.index(character)
    key_position = alphabet.index(key_character)

    if encrypt:
        new_position = (character_position + key_position) % 26
    else:
        new_position = (character_position - key_position) % 26

    return alphabet[new_position]

# Text encryption/decryption function
def crypt_text(text, keyword, encrypt=True):

    result = ""

    # Convert keyword to uppercase so it can be used with the
    # uppercase alphabet when calculating positions.
    keyword = keyword.upper()

    key_position = 0

    for character in text:

        # Handles Upper Case Letters
        if character in alphabet_uppercase:

            key_character = keyword[key_position % len(keyword)]

            result = result + crypt_letter(
                character,
                key_character,
                alphabet_uppercase,
                encrypt
            )

            key_position = key_position + 1

        # Handles Lower Case Letters
        elif character in alphabet_lowercase:

            key_character = keyword[key_position % len(keyword)]

            result = result + crypt_letter(
                character,
                key_character.lower(),
                alphabet_lowercase,
                encrypt
            )

            key_position = key_position + 1

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
def vigenere_menu():

    info()      # Prints information once

    while True:
        print()
        print("=== Vigenère Cipher ===")
        print("1) Encrypt")
        print("2) Decrypt")
        print("I) Information")
        print("R) Return")

        choice = input("Enter your choice: ")
        choice = choice.lower()

        if choice == "1":
            text = input("Enter text you would like to encrypt: ")
            keyword = input("Enter keyword: ")

            result = crypt_text(text, keyword, True)    #Boolean value passes that its encryption

            display_result(text, result, "Encrypted")

        elif choice == "2":
            text = input("Enter encrypted text you would like to decrypt: ")
            keyword = input("Enter keyword: ")

            result = crypt_text(text, keyword, False)   #Boolean value passes that its decryption

            display_result(text, result, "Decrypted")

        elif choice == "i":
            info()
            print()

        elif choice == "r":
            clear_terminal()
            break

        else:
            print("Invalid choice. Try again.")