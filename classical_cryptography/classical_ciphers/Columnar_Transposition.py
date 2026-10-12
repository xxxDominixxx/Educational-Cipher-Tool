from tools.terminal_cleaner import clear_terminal

def info():
    print("The Columnar Transposition cipher is a method of encrypting")
    print("messages by rearranging the characters according to a keyword.")
    print()
    print("The message is written into rows underneath the keyword.")
    print("The columns are then read from top to bottom in alphabetical")
    print("order of the keyword's letters.")
    print()
    print("For example, if the keyword is CAT:")
    print()
    print("C A T")
    print("H e l")
    print("l o W")
    print("o r l")
    print("d !")
    print()
    print("The same keyword is used for encryption and decryption.")
    print()
    print("Spaces, punctuation and other characters are preserved.")

# Creates the order in which the columns should be read
def get_column_order(keyword):

    columns = []

    for position in range(len(keyword)):
        columns.append((keyword[position], position))

    # Sorts the columns alphabetically by their characters
    columns.sort()

    order = []

    for character, position in columns:
        order.append(position)

    return order

# Text encryption function
def encrypt_text(text, keyword):

    keyword = keyword.upper()

    column_order = get_column_order(keyword)

    result = ""

    # Read each column in alphabetical order
    for column in column_order:

        position = column

        while position < len(text):
            result = result + text[position]
            position = position + len(keyword)

    return result

# Text decryption function
def decrypt_text(text, keyword):

    keyword = keyword.upper()

    column_order = get_column_order(keyword)

    # Calculate how many rows the original grid had
    rows = (len(text) + len(keyword) - 1) // len(keyword)

    # Calculate how many characters are in each column
    column_lengths = []

    for column in range(len(keyword)):

        length = 0

        position = column

        while position < len(text):
            length = length + 1
            position = position + len(keyword)

        column_lengths.append(length)

    # Create an empty grid
    grid = []

    for row in range(rows):
        grid.append([""] * len(keyword))

    key_position = 0

    # Put the encrypted characters back into their columns
    for column in column_order:
        for row in range(column_lengths[column]):
            grid[row][column] = text[key_position]
            key_position = key_position + 1

    # Read the grid from left to right
    result = ""

    for row in range(rows):
        for column in range(len(keyword)):
            if grid[row][column] != "":
                result = result + grid[row][column]
    return result

# Function that formats the result
def display_result(original, result, operation):
    print()
    print("Original message:", original)
    print(operation + " message:", result)

# =======================================================================================#
def columnar_transposition_menu():
    info()      # Prints information once

    while True:
        print()
        print("=== Columnar Transposition Cipher ===")
        print("1) Encrypt")
        print("2) Decrypt")
        print("I) Information")
        print("R) Return")

        choice = input("Enter your choice: ")
        choice = choice.lower()

        if choice == "1":

            text = input("Enter text you would like to encrypt: ")
            keyword = input("Enter keyword: ")

            result = encrypt_text(text, keyword)

            display_result(text, result, "Encrypted")

        elif choice == "2":

            text = input("Enter encrypted text you would like to decrypt: ")
            keyword = input("Enter keyword: ")

            result = decrypt_text(text, keyword)

            display_result(text, result, "Decrypted")

        elif choice == "i":
            info()
            print()

        elif choice == "r":
            clear_terminal()
            break

        else:
            print("Invalid choice. Try again.")