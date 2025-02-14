import numpy as np

# Convert text to numbers (A=0, B=1, ..., Z=25)
def text_to_numbers(text):
    return [ord(char) - ord('A') for char in text.upper() if char.isalpha()]

# Convert numbers back to text
def numbers_to_text(numbers):
    return ''.join(chr(num + ord('A')) for num in numbers)

# Encryption function
def encrypt(plaintext, key_matrix):
    plaintext = plaintext.replace(" ", "").upper()
    block_size = len(key_matrix)  # Determine block size based on key size

    # Padding plaintext to match block size
    while len(plaintext) % block_size != 0:
        plaintext += 'X'

    # Convert plaintext to numbers and reshape it without transposing
    plaintext_nums = text_to_numbers(plaintext)
    plaintext_matrix = np.array(plaintext_nums).reshape(-1, block_size)

    # Multiply plaintext blocks (rows) with the key matrix
    ciphertext_matrix = (plaintext_matrix @ key_matrix) % 26
    ciphertext_nums = ciphertext_matrix.flatten()

    ciphertext = numbers_to_text(ciphertext_nums)
    return ciphertext

# Decryption function
def decrypt(ciphertext, key_matrix):
    block_size = len(key_matrix)
    ciphertext_nums = text_to_numbers(ciphertext)
    ciphertext_matrix = np.array(ciphertext_nums).reshape(-1, block_size)

    # Compute the modular inverse of the determinant
    det = int(round(np.linalg.det(key_matrix)))
    try:
        det_inv = pow(det, -1, 26)
    except ValueError:
        raise ValueError("Key matrix is not invertible under mod 26. Choose a different key.")

    # Calculate the inverse key matrix modulo 26
    adjugate_matrix = np.round(det * np.linalg.inv(key_matrix)).astype(int) % 26
    inverse_key_matrix = (det_inv * adjugate_matrix) % 26

    # Multiply ciphertext blocks (rows) with the inverse key matrix
    decrypted_matrix = (ciphertext_matrix @ inverse_key_matrix) % 26
    decrypted_nums = decrypted_matrix.flatten()

    plaintext = numbers_to_text(decrypted_nums)
    return plaintext

# Input plaintext and key matrix
plaintext = input("Enter plaintext (A-Z only): ").strip().upper()
key_matrix = np.array([[17, 17, 5], [21, 18, 21], [2, 2, 19]])

print("\nKey Matrix:")
print(key_matrix)

# Encrypt and decrypt
ciphertext = encrypt(plaintext, key_matrix)
decrypted_text = decrypt(ciphertext, key_matrix)

# Display results
print("\nPlaintext:  ", plaintext)
print("Ciphertext: ", ciphertext)
print("Decrypted Text:", decrypted_text)
