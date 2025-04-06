def text_to_numbers(text):
    """Converts text to numbers (A=0, B=1, ..., Z=25)."""
    return [ord(char) - ord('A') for char in text.upper() if char.isalpha()]

def numbers_to_text(numbers):
    """Converts numbers back to text."""
    return ''.join(chr(num + ord('A')) for num in numbers)

def matrix_multiply(matrix_a, matrix_b):
    """Performs matrix multiplication."""
    rows_a = len(matrix_a)
    cols_a = len(matrix_a[0])
    cols_b = len(matrix_b[0])
    result = [[0 for _ in range(cols_b)] for _ in range(rows_a)]

    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                result[i][j] += matrix_a[i][k] * matrix_b[k][j]
            result[i][j] %= 26
    return result

def matrix_determinant(matrix):
    """Calculates the determinant of a 3x3 matrix."""
    return (matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1]) -
            matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0]) +
            matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0]))
def matrix_inverse_mod_26(matrix):
    """Calculates the inverse of a 3x3 matrix modulo 26."""
    det = matrix_determinant(matrix)
    if det == 0:
        raise ValueError("Key matrix is not invertible under mod 26. Determinant is 0.")

    det_inv = -1

    for i in range(26):
        if (det * i) % 26 == 1:
            det_inv = i
            break

    if det_inv == -1:
        raise ValueError("Key matrix is not invertible under mod 26. Modular inverse not found.")

    adjugate_matrix = [
        [(matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1]),
         -(matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0]),
         (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])],
        [-(matrix[0][1] * matrix[2][2] - matrix[0][2] * matrix[2][1]),
         (matrix[0][0] * matrix[2][2] - matrix[0][2] * matrix[2][0]),
         -(matrix[0][0] * matrix[2][1] - matrix[0][1] * matrix[2][0])],
        [(matrix[0][1] * matrix[1][2] - matrix[0][2] * matrix[1][1]),
         -(matrix[0][0] * matrix[1][2] - matrix[0][2] * matrix[1][0]),
         (matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0])]
    ]

    inverse_matrix = [[(adjugate_matrix[i][j] * det_inv) % 26 for j in range(3)] for i in range(3)]
    return inverse_matrix

def encrypt(plaintext, key_matrix):
    """Encrypts plaintext using the Hill cipher."""
    plaintext = plaintext.replace(" ", "").upper()
    block_size = len(key_matrix)

    while len(plaintext) % block_size != 0:
        plaintext += 'X'

    plaintext_nums = text_to_numbers(plaintext)
    ciphertext_nums = []

    for i in range(0, len(plaintext_nums), block_size):
        block = [[plaintext_nums[i + j]] for j in range(block_size)]
        encrypted_block = matrix_multiply(key_matrix, block)
        ciphertext_nums.extend([encrypted_block[j][0] for j in range(block_size)])

    return numbers_to_text(ciphertext_nums)

def decrypt(ciphertext, key_matrix):
    """Decrypts ciphertext using the Hill cipher."""
    block_size = len(key_matrix)
    ciphertext_nums = text_to_numbers(ciphertext)
    decrypted_nums = []

    inverse_key_matrix = matrix_inverse_mod_26(key_matrix)

    for i in range(0, len(ciphertext_nums), block_size):
        block = [[ciphertext_nums[i + j]] for j in range(block_size)]
        decrypted_block = matrix_multiply(inverse_key_matrix, block)
        decrypted_nums.extend([decrypted_block[j][0] for j in range(block_size)])

    return numbers_to_text(decrypted_nums)

plaintext = input("Enter plaintext (A-Z only): ").strip().upper()
key_matrix = [[17, 17, 5], [21, 18, 21], [2, 2, 19]]

print("\nKey Matrix:")
for row in key_matrix:
    print(row)

ciphertext = encrypt(plaintext, key_matrix)
decrypted_text = decrypt(ciphertext, key_matrix)

print("\nPlaintext: ", plaintext)
print("Ciphertext: ", ciphertext)
print("Decrypted Text:", decrypted_text)