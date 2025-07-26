# Test case for FHE encryption version1
from tfhe import *

def test_encryption():
    secret_key, cloud_key = generate_keys()
    plaintext = 100
    ciphertext = encrypt(secret_key, plaintext)
    assert decrypt(secret_key, ciphertext) == plaintext
    print("Test passed!")
