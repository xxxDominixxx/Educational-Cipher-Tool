from pathlib import Path

from tools.terminal_cleaner import clear_terminal

from modern_cryptography.rsa.key_management import (
    RSA_FILES_DIR,
    PRIVATE_KEY_FILE,
    PUBLIC_KEY_FILE,
    generate_key_pair,
)
from modern_cryptography.rsa.digital_signatures import (
    sign_file,
    verify_signature,
)
from modern_cryptography.rsa.hybrid_encryption import (
    encrypt_file,
    decrypt_file,
)
from modern_cryptography.rsa.secure_workflow import (
    encrypt_and_sign_file,
    decrypt_and_verify_file,
)

def info():
    print("RSA is an asymmetric cryptographic algorithm that")
    print("uses a pair of mathematically related keys:")
    print("a public key and a private key.")
    print("The public key can be used for encryption, while")
    print("the private key can decrypt the protected data.")
    print("RSA can also be used for digital signatures,")
    print("allowing signatures to be created with a private")
    print("key and verified using the corresponding public key.")
    print("RSA is computationally more expensive than AES,")
    print("so it is often used alongside AES in hybrid")
    print("encryption systems.")

def display_menu():
    print("---- RSA Cryptography ----")
    print("1) Generate RSA keys")
    print()
    print("-- Individual Operations --")
    print("2) Sign a file")
    print("3) Verify a signature")
    print("4) Encrypt a file")
    print("5) Decrypt a file")
    print()
    print("-- Combined Workflow --")
    print("6) Encrypt and sign a file")
    print("7) Decrypt and verify a file")
    print("R) Return")
    print()

def get_file_path():
    filename = input("Enter the filename in rsa_files: ").strip()
    return RSA_FILES_DIR / filename

def rsa_menu():
    RSA_FILES_DIR.mkdir(parents=True, exist_ok=True)

    while True:
        clear_terminal()
        display_menu()
        choice = input("Enter your choice: ").strip().lower()

        try:
            if choice == "1":
                clear_terminal()
                if PRIVATE_KEY_FILE.exists() or PUBLIC_KEY_FILE.exists():
                    confirm = input(
                        "Existing keys may be overwritten. Continue? (y/n): "
                    ).strip().lower()

                    if confirm != "y":
                        continue

                password = input("Choose a password for the private key: ")
                if not password:
                    print("Password cannot be empty.")
                else:
                    generate_key_pair(password)
                    print("RSA key pair generated successfully.")

            elif choice == "2":
                clear_terminal()
                file_path = get_file_path()
                password = input("Private-key password: ")
                signature_path = sign_file(file_path, password)
                print(f"Signature saved: {signature_path.name}")

            elif choice == "3":
                clear_terminal()
                file_path = get_file_path()
                if verify_signature(file_path):
                    print("Signature is valid.")
                else:
                    print("Signature is invalid.")

            elif choice == "4":
                clear_terminal()
                file_path = get_file_path()
                encrypted_path, key_path = encrypt_file(file_path)
                print(f"Encrypted file: {encrypted_path.name}")
                print(f"Encrypted session key: {key_path.name}")

            elif choice == "5":
                clear_terminal()
                file_path = get_file_path()
                password = input("Private-key password: ")
                decrypted_path = decrypt_file(file_path, password)
                print(f"Decrypted file saved: {decrypted_path.name}")

            elif choice == "6":
                clear_terminal()
                file_path = get_file_path()
                password = input("Private-key password: ")
                encrypted_path, key_path, signature_path = (
                    encrypt_and_sign_file(file_path, password)
                )
                print("File encrypted and signed successfully.")
                print(f"Encrypted file: {encrypted_path.name}")
                print(f"Encrypted session key: {key_path.name}")
                print(f"Signature: {signature_path.name}")

            elif choice == "7":
                clear_terminal()
                file_path = get_file_path()
                password = input("Private-key password: ")

                if decrypt_and_verify_file(file_path, password):
                    print("Signature verified. Decrypted file is valid.")
                    print(f"Output: {file_path.name}.dec")
                else:
                    print("Decryption or signature verification failed.")
                    print("No verified output was kept.")

            elif choice == "r":
                clear_terminal()
                break

            else:
                print("Invalid choice.")

        except (OSError, ValueError, TypeError) as error:
            print(f"Operation failed: {error}")

        input("\nPress Enter to continue...")