alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.
def encrypt(original_text, shift_amount):

# TODO-2: Inside the 'encrypt()' function, shift each letter of the 'original_text' forwards in the alphabet
#  by the shift amount and print the encrypted text.
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

# TODO-4: What happens if you try to shift z forwards by 9? Can you fix the code?

# TODO-3: Call the 'encrypt()' function and pass in the user inputs. You should be able to test the code and encrypt a
#  message.
encrypt(text, shift)

