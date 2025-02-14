# DES S-Boxes (only S1, S5, and S8 for demonstration)
S_BOXES = [
    # S1
    [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
     [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
     [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
     [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]],

    # S5
    [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
     [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
     [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
     [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]],

    # S8
    [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
     [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
     [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
     [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]
]

def s_box_substitution(input_48_bits):
    """Performs S-Box substitution for S1, S5, and S8 on a 48-bit input."""
    s_box_indices = [0, 4, 7]  # S1 (index 0), S5 (index 4), S8 (index 7)
    output_bits = {}

    for idx, s_box_num in enumerate(s_box_indices):
        chunk = input_48_bits[s_box_num * 6:(s_box_num + 1) * 6]  # Extract 6-bit chunk
        row = int(chunk[0] + chunk[5], 2)  # Get row using 1st and 6th bits
        col = int(chunk[1:5], 2)  # Get column using middle 4 bits
        s_box_value = S_BOXES[idx][row][col]  # Look up value in the selected S-Box
        output_bits[f'S{s_box_num + 1}'] = format(s_box_value, '04b')  # Convert to 4-bit binary

    return output_bits

# Get 48-bit binary input from user
input_bits = input("Enter 48-bit binary input: ")

# Ensure input length is valid
if len(input_bits) != 48 or not set(input_bits).issubset({'0', '1'}):
    print("Invalid input! Enter exactly 48 bits.")
    exit()

# Perform S-Box substitution
output_bits = s_box_substitution(input_bits)

# Display results
for key, value in output_bits.items():
    print(f"{key} Output: {value}")
