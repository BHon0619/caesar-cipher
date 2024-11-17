def caesar_cipher(message, shift=5):
    alphabet_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphabet_lower = "abcdefghijklmnopqrstuvwxyz"
    encoded_message = ""

# Loop through each character in the input text
    for char in message:
        if isinstance(char, str):  
            if char.islower():
                new_pos = (alphabet_lower.index(char) + shift) % 26
                encoded_message += alphabet_lower[new_pos]
            elif char.isupper():
                new_pos = (alphabet_upper.index(char) + shift) % 26
                encoded_message += alphabet_upper[new_pos]
            else:
                encoded_message += char
        else:
            encoded_message += char
    return encoded_message

message = input("Please enter the message you would like to encode.")
shifted_message = caesar_cipher(message, shift=5)
print("Here is your encoded message:", shifted_message) 