# AES Key Expansion Algorithm Implementation

# S-box lookup table (partial for demonstration)
SBOX = {
    0x00: 0x63, 0x01: 0x7c, 0x02: 0x77, 0x03: 0x7b, 0x04: 0xf2, 0x05: 0x6b,
    0x10: 0xca, 0x11: 0x82, 0x12: 0xc9, 0x13: 0x7d, 0x14: 0xfa, 0x15: 0x59,
    0x20: 0xb7, 0x21: 0xfd, 0x22: 0x93, 0x23: 0x26, 0x24: 0x36, 0x25: 0x3f,
    0x30: 0x04, 0x31: 0xc7, 0x32: 0x23, 0x33: 0xc3, 0x34: 0x18, 0x35: 0x96
}

# Round constants for rounds 1-3
RCON = [0x01, 0x02, 0x04]

def sub_word(word):
    """Apply S-box substitution to each byte in a word."""
    return [SBOX.get(b, b) for b in word]  # Use get() to handle missing SBOX values

def rot_word(word):
    """Perform cyclic left shift on the word."""
    return word[1:] + word[:1]

def xor_words(word1, word2):
    """XOR two words byte by byte."""
    return [b1 ^ b2 for b1, b2 in zip(word1, word2)]

def key_expansion(master_key, num_rounds=3):
    """
    Expand the master key into round keys.
    master_key: 4x4 matrix representing the initial key
    num_rounds: number of rounds (3 for this example)
    """
    # Convert master key to words (columns)
    key_words = [[master_key[row][col] for row in range(4)] 
                 for col in range(4)]
    
    # Generate additional words
    for round_num in range(4, 16):
        # Take the previous word
        temp = key_words[round_num - 1][:]
        
        if round_num % 4 == 0:
            # Apply transformation
            temp = rot_word(temp)
            temp = sub_word(temp)
            temp[0] ^= RCON[round_num // 4 - 1]
            
        new_word = xor_words(key_words[round_num - 4], temp)
        key_words.append(new_word)
    
    # Convert words back to 4x4 matrices for each round key
    round_keys = []
    for i in range(0, 16, 4):
        round_key = [[key_words[i + col][row] for col in range(4)]
                    for row in range(4)]
        round_keys.append(round_key)
    
    return round_keys

def print_matrix(matrix, title):
    """Print a 4x4 matrix in hexadecimal format."""
    print(f"\n{title}:")
    for row in matrix:
        print(" ".join(format(x, '02X') for x in row))

# Example master key
master_key = [
    [0x75, 0x32, 0x49, 0x5A],
    [0xAE, 0x11, 0x12, 0x13],
    [0xDF, 0x14, 0x15, 0x16],
    [0xCB, 0x17, 0x18, 0x19]
]

# Generate and display round keys
print_matrix(master_key, "Master Key")
round_keys = key_expansion(master_key)

for i in range(1, 4):  # Rounds 1 to 3
    print_matrix(round_keys[i], f"Round {i} Key")