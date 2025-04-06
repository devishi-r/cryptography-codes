import struct

# Convert message to binary
def message_to_binary(message):
    binary_message = ''.join(format(ord(c), '08b') for c in message)
    return binary_message

# Pad the binary message
def pad_message(binary_message):
    original_length = len(binary_message)
    
    # Append '1' bit
    binary_message += '1'
    
    # Calculate padding length (until 448 mod 512)
    padding_length = (448 - (original_length + 1) % 512) % 512
    
    # Append '0' bits
    binary_message += '0' * padding_length
    
    # Append original message length as 64-bit binary
    original_length_bits = format(original_length, '064b')
    binary_message += original_length_bits
    
    return binary_message, padding_length + 1  # Include the '1' bit in count

# Get user input
message = input("Enter the original message: ")

# Process the message
binary_message = message_to_binary(message)
padded_message, total_padding_bits = pad_message(binary_message)

# Display results
print("\nOriginal Message in Binary:")
print(binary_message)

print("\nTotal Number of Padding Bits:")
print(total_padding_bits)

print("\nPadding Bits in Binary:")
print(padded_message[len(binary_message):-64])  # Excluding message + length

print("\nLength of Original Message:")
print(len(binary_message))

print("\nLength of Original Message in Binary:")
print(format(len(binary_message), '064b'))
