from pathlib import Path

from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding

from modern_cryptography.rsa.key_management import (
    load_private_key,
    load_public_key,
)

def sign_file(filename, password):
    file_path = Path(filename)

    # Read the file that needs to be signed
    file_data = file_path.read_bytes()

    # Load the private key using the supplied password
    private_key = load_private_key(password)

    # Create the digital signature
    signature = private_key.sign(
        file_data,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )

    # Save the signature beside the original file
    signature_path = Path(str(file_path) + ".sig")
    signature_path.write_bytes(signature)

    return signature_path

def verify_signature(filename):
    file_path = Path(filename)
    signature_path = Path(str(file_path) + ".sig")

    # Read the original file and its signature
    file_data = file_path.read_bytes()
    signature = signature_path.read_bytes()

    # Load the public key
    public_key = load_public_key()

    try:
        public_key.verify(
            signature,
            file_data,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return True

    except InvalidSignature:
        return False