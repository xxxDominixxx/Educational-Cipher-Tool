from pathlib import Path

from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

from modern_cryptography.rsa.digital_signatures import sign_file
from modern_cryptography.rsa.hybrid_encryption import (
    encrypt_file,
    decrypt_file,
)
from modern_cryptography.rsa.key_management import load_public_key

def encrypt_and_sign_file(filename, password):
    # Sign the original file with the sender's private key
    signature_path = sign_file(filename, password)

    # Encrypt the original file and its AES session key
    encrypted_path, key_path = encrypt_file(filename)

    return encrypted_path, key_path, signature_path


def decrypt_and_verify_file(filename, password):
    file_path = Path(filename)
    signature_path = Path(str(file_path) + ".sig")

    # The signature is required to authenticate the decrypted content
    if not signature_path.exists():
        return False

    decrypted_path = Path(str(file_path) + ".dec")

    try:
        # Decrypt the file using the recipient's private key
        decrypt_file(filename, password)

        # Read the recovered content and the sender's signature
        plaintext = decrypted_path.read_bytes()
        signature = signature_path.read_bytes()

        # Verify the recovered content using the sender's public key
        public_key = load_public_key()
        public_key.verify(
            signature,
            plaintext,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH,
            ),
            hashes.SHA256(),
        )

        return True

    except (InvalidSignature, ValueError, TypeError, FileNotFoundError):
        # Do not leave an unverified decrypted file behind
        if decrypted_path.exists():
            decrypted_path.unlink()

        return False