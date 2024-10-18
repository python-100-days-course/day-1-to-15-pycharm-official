alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# TODO-1: Create a function called 'decrypt()' that takes 'original_text' and 'shift_amount' as inputs.
def decrypt(original_text, shift_amount):

# TODO-2: Inside the 'decrypt()' function, shift each letter of the 'original_text' *backwards* in the alphabet
#  by the shift amount and print the decrypted text.
# my code:
    decrypted_text = ""
    z_index = len(alphabet) - 1
    # print(z_index) # checking
    for char in original_text:
        new_char_index = alphabet.index(char) - shift_amount
        # if new_char_index = a to z
        if new_char_index >= 0:
            decrypted_text += alphabet[new_char_index]
        # if new_char_index is negative, start from end of the alphabet
        else:
            decrypted_text += alphabet[new_char_index + (z_index + 1)]
    print(f"Here is the decoded result: {decrypted_text}")
# 1 shift: ifmmp -> hello, 3 shift: crur -> zoro
# decrypt(text, shift)

# TODO-3: Combine the 'encrypt()' and 'decrypt()' functions into one function called 'caesar()'.
#  Use the value of the user chosen 'direction' variable to determine which functionality to use.
# my code:
def caesar(original_text, shift_amount):
    if direction == "encode":
        encrypted_text = ""
        z_index = len(alphabet) - 1
        # print(z_index) # checking
        for char in original_text:
            new_char_index = alphabet.index(char) + shift_amount
            # if new_char_index = a to z
            if new_char_index <= z_index:
                encrypted_text += alphabet[new_char_index]
            # if new_char_index goes beyond z, start from beginning of the alphabet
            else:
                encrypted_text += alphabet[new_char_index - (z_index + 1)]
        print(f"Here is the encoded result: {encrypted_text}")
    elif direction == "decode":
        decrypted_text = ""
        z_index = len(alphabet) - 1
        # print(z_index) # checking
        for char in original_text:
            new_char_index = alphabet.index(char) - shift_amount
            # if new_char_index = a to z
            if new_char_index >= 0:
                decrypted_text += alphabet[new_char_index]
            # if new_char_index is negative, start from end of the alphabet
            else:
                decrypted_text += alphabet[new_char_index + (z_index + 1)]
        print(f"Here is the decoded result: {decrypted_text}")
    else:
        print("You've entered something other than 'encode' or 'decode', please try again.")

caesar(text, shift)



