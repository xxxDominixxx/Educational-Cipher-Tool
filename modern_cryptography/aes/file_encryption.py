import base64

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

from modern_cryptography.aes.aes_ctr import (
    enc_ctr,
    dec_ctr,
    generate_mac,
    verify_mac,
    gen_key,
)

# ======================== FILE ENCRYPTION ======================== #

def encrypt_file(input_file, output_file, password):
    # Read the plaintext from the input file
    with open(input_file, "rb") as f:
        plaintext = f.read()

    # Generate a salt and derive a key from the password
    seed, key = gen_key(password)

    # Split the key into encryption and MAC keys
    encryption_key = key[:16]
    mac_key = key[16:]

    # Encrypt the plaintext
    ciphertext = enc_ctr(plaintext, encryption_key)

    # Generate a MAC of the plaintext
    mac = generate_mac(plaintext, mac_key)

    # Combine the salt, ciphertext, and MAC
    data = seed + ciphertext + mac

    # Encode the data using Base64
    encoded_data = base64.b64encode(data)

    # Write the encrypted data to the output file
    with open(output_file, "wb") as f:
        f.write(encoded_data)


# ======================== FILE DECRYPTION ======================== #

def decrypt_file(input_file, output_file, password):
    # Read the Base64-encoded encrypted data
    with open(input_file, "rb") as f:
        encoded_data = f.read()

    # Decode the Base64 data into bytes
    try:
        data = base64.b64decode(encoded_data, validate=True)
    except (ValueError, base64.binascii.Error):
        return False

    # Check that the data contains at least the salt, IV, and MAC
    if len(data) < 64:
        return False

    # Extract the salt, MAC, and ciphertext
    seed = data[:16]
    mac = data[-32:]
    ciphertext = data[16:-32]

    # Derive the same key using the supplied password and stored salt
    password_bytes = password.encode()

    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=seed,
        iterations=1600000
    )

    key = kdf.derive(password_bytes)

    # Split the key into encryption and MAC keys
    encryption_key = key[:16]
    mac_key = key[16:]

    # Decrypt the ciphertext
    plaintext = dec_ctr(ciphertext, encryption_key)

    # Verify the MAC before saving the plaintext
    if not verify_mac(plaintext, mac_key, mac):
        return False

    # Save the decrypted file only if verification succeeds
    with open(output_file, "wb") as f:
        f.write(plaintext)

    return True