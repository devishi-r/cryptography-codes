# MD5 Initial Constants
A = int(input("Enter initial A (in hex, without 0x prefix): "), 16)
B = int(input("Enter initial B (in hex, without 0x prefix): "), 16)
C = int(input("Enter initial C (in hex, without 0x prefix): "), 16)
D = int(input("Enter initial D (in hex, without 0x prefix): "), 16)

M0 = int(input("Enter first 32-bit block (M0) in decimal: "))
K1 = int(input("Enter K1 constant in decimal: "))

M1 = int(input("Enter second 32-bit block (M1) in decimal: "))
K2 = int(input("Enter K2 constant in decimal: "))

# MD5 F function
def F(X, Y, Z):
    return (X & Y) | (~X & Z)

# Left rotate function
def left_rotate(x, s):
    return ((x << s) | (x >> (32 - s))) & 0xFFFFFFFF

# Step 1 processing
def step1_processing(A, B, C, D, M0, K1):
    A = (B + left_rotate((A + F(B, C, D) + M0 + K1), 7)) & 0xFFFFFFFF
    return A

# Step 2 processing
def step2_processing(A, B, C, D, M1, K2):
    D = (A + left_rotate((D + F(A, B, C) + M1 + K2), 12)) & 0xFFFFFFFF
    return D

# Display initial values
print("\nInitial MD5 Buffer Values:")
print(f"A = {hex(A)}")
print(f"B = {hex(B)}")
print(f"C = {hex(C)}")
print(f"D = {hex(D)}")

# Step 1 processing
A = step1_processing(A, B, C, D, M0, K1)

# Display Step 1 output
print("\nAfter Step 1 (Round 1):")
print(f"A = {hex(A)}")
print(f"B = {hex(B)}")
print(f"C = {hex(C)}")
print(f"D = {hex(D)}")

# Step 2 processing (using output of Step 1)
D = step2_processing(A, B, C, D, M1, K2)

# Display Step 2 output
print("\nAfter Step 2 (Round 1):")
print(f"A = {hex(A)}")
print(f"B = {hex(B)}")
print(f"C = {hex(C)}")
print(f"D = {hex(D)}")
