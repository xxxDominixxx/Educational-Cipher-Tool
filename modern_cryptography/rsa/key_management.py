from pathlib import Path

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa

# Store RSA key files in the rsa_files directory
RSA_FILES_DIR = Path(__file__).resolve().parent / "rsa_files"

PRIVATE_KEY_FILE = RSA_FILES_DIR / "myPrivate.pem"
PUBLIC_KEY_FILE = RSA_FILES_DIR / "myPublic.pem"

def generate_key_pair(password):
    # Create the directory if it does not exist
    RSA_FILES_DIR.mkdir(parents=True, exist_ok=True)

    # Generate a 2048-bit RSA private key
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )

    # Extract the corresponding public key
    public_key = private_key.public_key()

    # Convert the password to bytes
    password_bytes = password.encode("utf-8")

    # Serialize and password-protect the private key
    private_key_data = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.BestAvailableEncryption(
            password_bytes
        )
    )

    # Serialize the public key
    public_key_data = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

    # Save both keys
    PRIVATE_KEY_FILE.write_bytes(private_key_data)
    PUBLIC_KEY_FILE.write_bytes(public_key_data)

def load_private_key(password):
    # Read the encrypted private key
    private_key_data = PRIVATE_KEY_FILE.read_bytes()

    # Load and unlock the private key
    return serialization.load_pem_private_key(
        private_key_data,
        password=password.encode("utf-8")
    )

def load_public_key():
    # Read and load the public key
    public_key_data = PUBLIC_KEY_FILE.read_bytes()

    return serialization.load_pem_public_key(public_key_data)