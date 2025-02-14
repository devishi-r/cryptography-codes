# Function to construct the 5x5 key matrix
def construct_key_matrix(key):
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # Excluding 'J'
    key = key.upper().replace("J", "I")  # Convert key to uppercase and replace J with I
    unique_key = "".join(dict.fromkeys(key + alphabet))  # Remove duplicates and append remaining letters
    key_matrix = [unique_key[i:i+5] for i in range(0, 25, 5)]  # Convert to 5x5 matrix
    return key_matrix

# Function to preprocess plaintext
def preprocess_plaintext(plaintext):
    plaintext = plaintext.upper().replace("J", "I")  # Convert to uppercase and replace J with I
    processed_text = ""
    i = 0
    while i < len(plaintext):
        processed_text += plaintext[i]
        # Add 'X' if duplicate letters appear in a digraph
        if i + 1 < len(plaintext) and plaintext[i] == plaintext[i + 1]:
            processed_text += "X"
        i += 1
    if len(processed_text) % 2 != 0:
        processed_text += "X"  # Add 'X' if the length is odd
    return processed_text

# Function to find positions of letters in the key matrix
def get_positions(letter, key_matrix):
    for row in range(5):
        if letter in key_matrix[row]:
            return row, key_matrix[row].index(letter)
    return None

# Encryption function
def encrypt(plaintext, key_matrix):
    ciphertext = ""
    for i in range(0, len(plaintext), 2):
        a, b = plaintext[i], plaintext[i + 1]
        ax, ay = get_positions(a, key_matrix)
        bx, by = get_positions(b, key_matrix)

        if ax == bx:  # Same row
            ciphertext += key_matrix[ax][(ay + 1) % 5] + key_matrix[bx][(by + 1) % 5]
        elif ay == by:  # Same column
            ciphertext += key_matrix[(ax + 1) % 5][ay] + key_matrix[(bx + 1) % 5][by]
        else:  # Forming a rectangle
            ciphertext += key_matrix[ax][by] + key_matrix[bx][ay]
    return ciphertext

# Decryption function
def decrypt(ciphertext, key_matrix):
    plaintext = ""
    for i in range(0, len(ciphertext), 2):
        a, b = ciphertext[i], ciphertext[i + 1]
        ax, ay = get_positions(a, key_matrix)
        bx, by = get_positions(b, key_matrix)

        if ax == bx:  # Same row
            plaintext += key_matrix[ax][(ay - 1) % 5] + key_matrix[bx][(by - 1) % 5]
        elif ay == by:  # Same column
            plaintext += key_matrix[(ax - 1) % 5][ay] + key_matrix[(bx - 1) % 5][by]
        else:  # Forming a rectangle
            plaintext += key_matrix[ax][by] + key_matrix[bx][ay]
    return plaintext

# Main program to take input and display output
key = input("Enter the key: ")
plaintext = input("Enter the plaintext: ")

key_matrix = construct_key_matrix(key)
print("\nGenerated Key Matrix:")
for row in key_matrix:
    print(" ".join(row))

processed_plaintext = preprocess_plaintext(plaintext)
ciphertext = encrypt(processed_plaintext, key_matrix)
decrypted_text = decrypt(ciphertext, key_matrix)

print("\nCiphertext:", ciphertext)
print("Decrypted Text:", decrypted_text)
