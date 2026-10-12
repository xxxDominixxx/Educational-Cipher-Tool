from tools.terminal_cleaner import clear_terminal

def info():
    print("The Rail Fence cipher is a transposition cipher that rearranges")
    print("characters by writing them in a zigzag pattern across multiple rows.")
    print()
    print("The number of rows is called the number of rails.")
    print()
    print("For example, with 3 rails:")
    print()
    print("W . . . E . . . C")
    print(". E . R . D . S .")
    print(". . L . . . F . .")
    print()
    print("The encrypted message is created by reading each rail from top to bottom.")
    print()
    print("The number of rails must be at least 2.")
    print("If the number of rails is equal to or greater than the")
    print("number of characters, the message will remain unchanged.")


# Creates the zigzag pattern used by the cipher
def rail_pattern(length, rails):

    pattern = []

    current_rail = 0
    direction = 1

    for number in range(length):

        pattern.append(current_rail)

        # Change direction when reaching the top or bottom rail
        if current_rail == 0:
            direction = 1

        elif current_rail == rails - 1:
            direction = -1

        current_rail = current_rail + direction

    return pattern


# Encrypts the text using the Rail Fence cipher
def encrypt_text(text, rails):

    pattern = rail_pattern(len(text), rails)

    result = ""

    # Read the characters rail by rail
    for rail in range(rails):

        for position in range(len(text)):

            if pattern[position] == rail:
                result = result + text[position]

    return result


# Decrypts the text using the Rail Fence cipher
def decrypt_text(text, rails):

    pattern = rail_pattern(len(text), rails)

    result = [""] * len(text)

    position = 0

    # Put encrypted characters back into their correct rails
    for rail in range(rails):

        for index in range(len(text)):

            if pattern[index] == rail:
                result[index] = text[position]
                position = position + 1

    return "".join(result)


# Function that formats the result
def display_result(original, result, operation):

    print()
    print("Original message:", original)
    print(operation + " message:", result)


#=======================================================================================#
def rail_fence_menu():

    info()      # Prints information once

    while True:
        print()
        print("=== Rail Fence Cipher ===")
        print("1) Encrypt")
        print("2) Decrypt")
        print("I) Information")
        print("R) Return")

        choice = input("Enter your choice: ")
        choice = choice.lower()

        if choice == "1":

            text = input("Enter text you would like to encrypt: ")

            rails = int(input("Enter number of rails: "))

            if rails < 2:
                print("Invalid number of rails. Must be at least 2.")
                continue

            result = encrypt_text(text, rails)

            display_result(text, result, "Encrypted")

        elif choice == "2":

            text = input("Enter encrypted text you would like to decrypt: ")

            rails = int(input("Enter number of rails: "))

            if rails < 2:
                print("Invalid number of rails. Must be at least 2.")
                continue

            result = decrypt_text(text, rails)

            display_result(text, result, "Decrypted")

        elif choice == "i":
            info()
            print()

        elif choice == "r":
            clear_terminal()
            break

        else:
            print("Invalid choice. Try again.")