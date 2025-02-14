from copy import deepcopy

# AES MixColumns transformation matrix
MIX_COLUMNS_MATRIX = [
    [0x02, 0x03, 0x01, 0x01],
    [0x01, 0x02, 0x03, 0x01],
    [0x01, 0x01, 0x02, 0x03],
    [0x03, 0x01, 0x01, 0x02]
]

# Function to perform ShiftRows transformation
def shift_rows(state):
    new_state = deepcopy(state)
    # Second row - shift left by 1
    new_state[1] = new_state[1][1:] + new_state[1][:1]
    # Third row - shift left by 2
    new_state[2] = new_state[2][2:] + new_state[2][:2]
    # Fourth row - shift left by 3
    new_state[3] = new_state[3][3:] + new_state[3][:3]
    return new_state

# Galois Field multiplication function
def galois_mult(a, b):
    result = 0
    for i in range(8):
        if b & 0x01:
            result ^= a
        high_bit_set = a & 0x80
        a <<= 1
        if high_bit_set:
            a ^= 0x1B  # Irreducible polynomial for AES (x^8 + x^4 + x^3 + x + 1)
        b >>= 1
    return result & 0xFF

# Function to perform MixColumns transformation
def mix_columns(state):
    new_state = deepcopy(state)
    for col in range(4):
        for row in range(4):
            new_state[row][col] = (
                galois_mult(MIX_COLUMNS_MATRIX[row][0], state[0][col]) ^
                galois_mult(MIX_COLUMNS_MATRIX[row][1], state[1][col]) ^
                galois_mult(MIX_COLUMNS_MATRIX[row][2], state[2][col]) ^
                galois_mult(MIX_COLUMNS_MATRIX[row][3], state[3][col])
            )
    return new_state

# Standard input matrix
standard_matrix = [
    [0x32, 0x88, 0x31, 0xE0],
    [0x43, 0x5A, 0x31, 0x37],
    [0xF6, 0x30, 0x98, 0x07],
    [0xA8, 0x8D, 0xA2, 0x34]
]

print("Standard Matrix:")
for row in standard_matrix:
    print(" ".join(format(x, '02X') for x in row))

# Perform ShiftRows transformation on standard matrix
shifted_state = shift_rows(standard_matrix)
print("\nAfter ShiftRows:")
for row in shifted_state:
    print(" ".join(format(x, '02X') for x in row))

# Example 4x4 AES state matrix (input in hexadecimal format)
state = [
    [0xD4, 0xBF, 0x5D, 0x30],
    [0xE0, 0xB4, 0x52, 0xAE],
    [0xB8, 0x41, 0x11, 0xF1],
    [0x1E, 0x27, 0x98, 0xE5]
]

print("\nBefore MixColumns:")
for row in state:
    print(" ".join(format(x, '02X') for x in row))

# Perform MixColumns transformation
mixed_state = mix_columns(state)

print("\nAfter MixColumns:")
for row in mixed_state:
    print(" ".join(format(x, '02X') for x in row))