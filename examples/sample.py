# Sample encryption demo using TFHE-rs
from tfhe import *

# Initialize keys
secret_key, cloud_key = generate_keys()

# Encrypt data
plaintext = 42
ciphertext = encrypt(secret_key, plaintext)
print(f"Encrypted: {ciphertext}")

# Decrypt data
decrypted = decrypt(secret_key, ciphertext)
print(f"Decrypted: {decrypted}")
