import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import hashes, hmac
from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

# ======================== AES-CTR ENCRYPTION ======================== #

def enc_ctr(plaintext, key):
    # Generate a random 16-byte IV
    iv = os.urandom(16)

    # Create the AES cipher using CTR mode and the IV
    cipher = Cipher(algorithms.AES(key), modes.CTR(iv))

    # Create the encryption object
    encryptor = cipher.encryptor()

    # Encrypt the plaintext
    ciphertext = encryptor.update(plaintext) + encryptor.finalize()

    # Return the IV followed by the ciphertext
    return iv + ciphertext

# ======================== AES-CTR DECRYPTION ======================== #

def dec_ctr(data, key):
    # Extract the IV and ciphertext
    iv = data[:16]
    ciphertext = data[16:]

    # Create the AES cipher using the same key and IV
    cipher = Cipher(algorithms.AES(key), modes.CTR(iv))

    # Create the decryption object
    decryptor = cipher.decryptor()

    # Decrypt the ciphertext
    plaintext = decryptor.update(ciphertext) + decryptor.finalize()

    return plaintext

# ======================== MESSAGE AUTHENTICATION ======================== #

def generate_mac(message, key):
    # Create an HMAC object using SHA-256
    h = hmac.HMAC(key, hashes.SHA256())

    # Provide the message to authenticate
    h.update(message)

    # Return the calculated MAC
    return h.finalize()


def verify_mac(message, key, mac_value):
    # Create an HMAC object using SHA-256
    h = hmac.HMAC(key, hashes.SHA256())

    # Provide the message to authenticate
    h.update(message)

    # Verify the supplied MAC
    try:
        h.verify(mac_value)
        return True
    except InvalidSignature:
        return False

# ======================== PASSWORD-BASED KEY DERIVATION ======================== #

def gen_key(password):
    # Convert the password to bytes
    password = password.encode()

    # Generate a random 16-byte salt
    seed = os.urandom(16)

    # Configure PBKDF2 using SHA-256
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=seed,
        iterations=1600000
    )

    # Derive a 32-byte key from the password
    key = kdf.derive(password)

    # Return the salt and derived key
    return seed, key