def shift_alphabet_string(text, shift=5):
    alphabet_lower = ['abcdefghijklmnopqrstuvwxyz']
    alphabet_upper = ['ABCDEFGHIJKLMNOPQRSTUVWXY']
    shifted_text = ""

#Loop thru each character in the input string
    for char in text:
        if char in alphabet_lower:
        #Find the index of the character in the lowercase alphabet and apply shift
            index = alphabet_lower.index(char)
        shifted_text +=alphabet_lower [index + shift]
        if char in alphabet_upper:
        #Find the index of the character in the uppercase alphabet and apply shift
            index = alphabet_upper.index(char)
        shifted_text += alphabet_upper[(index + shift)]
    else:
        #spaces and special characterws remain
        shifted_text += char

    return shifted_text

input_string = input("Please enter the message you would like to encrypt.")
shift = 5 #shift value is set to 5
shifted_string = shift_alphabet_string(input_string, shift)
print("Encrypted Code:", shifted_string)
