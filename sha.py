def sha512_padding(message_length):
    """Calculates the padding for SHA-512."""
    length_in_bits = message_length
    k = (896 - (length_in_bits)) % 1024
    if k < 0:
        k += 1024
    total_padding_bits = k + 64
    padded_message_length = length_in_bits + total_padding_bits

    return total_padding_bits, padded_message_length

message_length = int(input("Enter the length of the original message in bits: "))
padding_bits, padded_length = sha512_padding(message_length)

print(f"\nOriginal Message Length: {message_length} bits")
print(f"Padding Bits (number of '0's added after the '1' bit): {padding_bits - 65}") # -65 to show only the zeroes
print(f"Total Padded Message Length: {padded_length} bits")
print(f"Total Blocks Required: {padded_length // 1024 +1}")