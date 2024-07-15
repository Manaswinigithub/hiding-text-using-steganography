def message_to_binary(message):
    # Convert each character to its binary representation
    return ''.join(format(ord(char), '08b') for char in message)

def encode_capitalization(text, message):
    binary_message = message_to_binary(message)
    encoded_text = ''
    binary_index = 0

    for char in text:
        if char.isalpha():
            if binary_index < len(binary_message):
                if binary_message[binary_index] == '1':
                    encoded_text += char.upper()
                else:
                    encoded_text += char.lower()
                binary_index += 1
            else:
                encoded_text += char
        else:
            encoded_text += char

    return encoded_text

# Example usage
cover_text = "This is a simple cover text."
hidden_message = "Hi"
encoded_text = encode_capitalization(cover_text, hidden_message)
print("Encoded Text:", encoded_text)
def binary_to_message(binary_message):
    message = ''
    for i in range(0, len(binary_message), 8):
        byte = binary_message[i:i+8]
        message += chr(int(byte, 2))
    return message

def decode_capitalization(encoded_text):
    binary_message = ''
    for char in encoded_text:
        if char.isalpha():
            if char.isupper():
                binary_message += '1'
            else:
                binary_message += '0'

    return binary_to_message(binary_message)

# Example usage
decoded_message = decode_capitalization(encoded_text)
print("Decoded Message:", decoded_message)
