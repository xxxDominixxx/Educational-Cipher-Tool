from tools.terminal_cleaner import clear_terminal

alphabet_uppercase = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
                      "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
alphabet_lowercase = [letter.lower() for letter in alphabet_uppercase]

# Function that acquires the letter key
def get_key():
    while True:
        key = input("Enter letter key: ")

        # Convert key to uppercase
        key = key.upper()

        # Check that the key is exactly one letter
        if key in alphabet_uppercase:
            break
        else:
            print()
            print("Please enter a single letter.")

    return key


# Function that converts the letter key into a numeric shift
def key_to_shift(key):
    return alphabet_uppercase.index(key)


# Letter encryption/decryption function
def crypt_letter(character, alphabet, shift):
    position = alphabet.index(character)
    new_position = (position + shift) % 26

    return alphabet[new_position]


# Text encryption/decryption function
def crypt_text(text, shift):
    result = ""

    character_list = list(text)

    for character in character_list:

        # Handles Upper Case Letters
        if character in alphabet_uppercase:
            result = result + crypt_letter(character, alphabet_uppercase, shift)

        # Handles Lower Case Letters
        elif character in alphabet_lowercase:
            result = result + crypt_letter(character, alphabet_lowercase, shift)

        # Handles everything else that is not a letter
        else:
            result = result + character

    return result


# Function that formats the result
def display_result(original, result, key, shift, operation):
    print()
    print("Original message:", original)
    print(operation + " message:", result)
    print("Key:", key)
    print("Shift:", shift)


# =======================================================================================

def caesar_letter_key_menu():
    while True:
        print()
        print("=== Caesar Letter Key ===")
        print("1) Encrypt")
        print("2) Decrypt")
        print("I) Info")
        print("R) Return")

        choice = input("Enter your choice: ")
        choice = choice.lower()

        if choice == "1":
            text = input("Enter text you would like to encrypt: ")

            key = get_key()
            shift = key_to_shift(key)

            result = crypt_text(text, shift)

            display_result(text, result, key, shift, "Encrypted")

        elif choice == "2":
            text = input("Enter encrypted text you would like to decrypt: ")

            key = get_key()
            shift = key_to_shift(key)

            result = crypt_text(text, -shift)

            display_result(text, result, key, shift, "Decrypted")

        elif choice == "r":
            clear_terminal()
            break

        else:
            print("Invalid choice. Try again.")