from pathlib import Path

from tools.terminal_cleaner import clear_terminal
from modern_cryptography.aes.file_encryption import encrypt_file, decrypt_file

AES_FILES_DIR = Path(__file__).resolve().parent / "aes_files"

MESSAGE_FILE = AES_FILES_DIR / "message.txt"
ENCRYPTED_FILE = AES_FILES_DIR / "encrypted_message.txt"
DECRYPTED_FILE = AES_FILES_DIR / "decrypted_message.txt"

def info():
    print("AES (Advanced Encryption Standard) is a modern")
    print("symmetric encryption algorithm used to protect")
    print("digital information.")
    print("It uses the same secret key for encryption and")
    print("decryption and supports key sizes of 128, 192,")
    print("and 256 bits.")
    print("AES is widely used because it is efficient and")
    print("secure when implemented and used correctly.")

def display_menu():
    print("---- AES Encryption ----")
    print("1) Encrypt a message")
    print("2) Decrypt a message")
    print("R) Return")
    print()

def encrypt_message():
    message = input("Enter the message to encrypt: ")
    password = input("Enter a password: ")

    AES_FILES_DIR.mkdir(parents=True, exist_ok=True)
    MESSAGE_FILE.write_text(message, encoding="utf-8")

    encrypt_file(
        str(MESSAGE_FILE),
        str(ENCRYPTED_FILE),
        password
    )

    print()
    print("Message encrypted successfully.")
    print(f"Original message: {MESSAGE_FILE.name}")
    print(f"Encrypted message: {ENCRYPTED_FILE.name}")

def decrypt_message():
    password = input("Enter the password: ")

    success = decrypt_file(
        str(ENCRYPTED_FILE),
        str(DECRYPTED_FILE),
        password
    )

    print()

    if success:
        print("Message decrypted successfully.")
        print(f"Decrypted message: {DECRYPTED_FILE.name}")
    else:
        print("Decryption failed.")
        print("The password may be incorrect or the data was modified.")


def aes_menu():
    while True:
        clear_terminal()

        info()
        print()
        input("Press Enter to continue...")

        display_menu()

        choice = input("Enter your choice: ").lower()

        if choice == "1":
            clear_terminal()
            encrypt_message()
            input("\nPress Enter to continue...")

        elif choice == "2":
            clear_terminal()

            if not ENCRYPTED_FILE.exists():
                print("No encrypted message found.")
                print("Encrypt a message first.")
            else:
                decrypt_message()

            input("\nPress Enter to continue...")

        elif choice == "r":
            clear_terminal()
            break

        else:
            print("Invalid choice. Try again.")
            input("\nPress Enter to continue...")