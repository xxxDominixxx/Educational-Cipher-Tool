from pathlib import Path
import os

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.asymmetric import padding

from modern_cryptography.rsa.key_management import (
    load_private_key,
    load_public_key,
)

def encrypt_file(filename):
    file_path = Path(filename)
    file_data = file_path.read_bytes()

    # Generate a random AES-256 session key and AES-CTR IV
    session_key = os.urandom(32)
    iv = os.urandom(16)

    # Encrypt the file using AES-CTR
    cipher = Cipher(algorithms.AES(session_key), modes.CTR(iv))
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(file_data) + encryptor.finalize()

    # Save IV followed by ciphertext
    encrypted_path = Path(str(file_path) + ".enc")
    encrypted_path.write_bytes(iv + ciphertext)

    # Encrypt the AES session key using the RSA public key
    public_key = load_public_key()
    encrypted_key = public_key.encrypt(
        session_key,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    # Save the encrypted session key
    key_path = Path(str(file_path) + ".key")
    key_path.write_bytes(encrypted_key)

    return encrypted_path, key_path

def decrypt_file(filename, password):
    file_path = Path(filename)

    encrypted_path = Path(str(file_path) + ".enc")
    key_path = Path(str(file_path) + ".key")

    # Read the encrypted file and encrypted session key
    encrypted_data = encrypted_path.read_bytes()
    encrypted_key = key_path.read_bytes()

    # The file must contain at least the 16-byte IV
    if len(encrypted_data) < 16:
        raise ValueError("Encrypted file is too short.")

    iv = encrypted_data[:16]
    ciphertext = encrypted_data[16:]

    # Load the private key and decrypt the AES session key
    private_key = load_private_key(password)
    session_key = private_key.decrypt(
        encrypted_key,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    # Decrypt the file using AES-CTR
    cipher = Cipher(algorithms.AES(session_key), modes.CTR(iv))
    decryptor = cipher.decryptor()
    plaintext = decryptor.update(ciphertext) + decryptor.finalize()

    # Save the decrypted file
    decrypted_path = Path(str(file_path) + ".dec")
    decrypted_path.write_bytes(plaintext)

    return decrypted_path