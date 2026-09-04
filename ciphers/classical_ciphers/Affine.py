from tools.terminal_cleaner import clear_terminal
from tools.alphabets import alphabet_uppercase, alphabet_lowercase


def info():
    print("The Affine cipher is a substitution cipher that uses two keys,")
    print("a and b, to determine how each letter is transformed.")
    print()
    print("The encryption formula is:")
    print("E(x) = (a * x + b) mod 26")
    print()
    print("The decryption formula is:")
    print("D(x) = a^-1 * (x - b) mod 26")
    print()
    print("The value of a must be relatively prime to 26.")
    print("The value of b can be any number from 0 to 25.")


# Finds the modular inverse of a
def modular_inverse(a):
    for number in range(26):
        if (a * number) % 26 == 1:
            return number
    return None


# Finds all valid values for a
def valid_a_values():
    valid_values = []
    for number in range(26):
        if modular_inverse(number) is not None:
            valid_values.append(number)
    return valid_values


# Letter encryption/decryption function
def crypt_letter(character, a, b, alphabet, encrypt=True):

    character_position = alphabet.index(character)

    if encrypt:
        new_position = (a * character_position + b) % 26

    else:
        inverse_a = modular_inverse(a)
        new_position = (inverse_a * (character_position - b)) % 26

    return alphabet[new_position]


# Text encryption/decryption function
def crypt_text(text, a, b, encrypt=True):

    result = ""

    for character in text:

        # Handles Upper Case Letters
        if character in alphabet_uppercase:

            result = result + crypt_letter(character, a, b, alphabet_uppercase, encrypt)

        # Handles Lower Case Letters
        elif character in alphabet_lowercase:

            result = result + crypt_letter(character, a, b, alphabet_lowercase, encrypt)

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
def affine_menu():

    info()      # Prints information once

    while True:
        print()
        print("=== Affine Cipher ===")
        print("1) Encrypt")
        print("2) Decrypt")
        print("I) Information")
        print("R) Return")

        choice = input("Enter your choice: ")
        choice = choice.lower()

        if choice == "1":

            text = input("Enter text you would like to encrypt: ")

            print()
            print("Valid values for a:")
            print(valid_a_values())

            a = int(input("Enter value for a: "))
            b = int(input("Enter value for b (0-25): "))

            if a not in valid_a_values():
                print("Invalid value for a.")
                continue

            result = crypt_text(text, a, b, True)

            display_result(text, result, "Encrypted")

        elif choice == "2":

            text = input("Enter encrypted text you would like to decrypt: ")

            print()
            print("Valid values for a:")
            print(valid_a_values())

            a = int(input("Enter value for a: "))
            b = int(input("Enter value for b (0-25): "))

            if a not in valid_a_values():
                print("Invalid value for a.")
                continue

            result = crypt_text(text, a, b, False)

            display_result(text, result, "Decrypted")

        elif choice == "i":
            info()
            print()

        elif choice == "r":
            clear_terminal()
            break

        else:
            print("Invalid choice. Try again.")