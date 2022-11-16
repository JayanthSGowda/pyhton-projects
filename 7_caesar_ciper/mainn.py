# there two methods in this file
#jump to line 67
from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)

#encript
def encode(message,shift_number):
    encrypted_message = ""

    for letter in message:
        if letter in alphabet:
            index = alphabet.index(letter)
            if index + shift_number > 25:
                index -= 26 + shift_number
                encrypted_message += alphabet[index]
            encrypted_message += alphabet[index + shift_number]
        else:
            encrypted_message += letter

    print(f"Here's the encoded result: {encrypted_message}")

# decript

def decode(message,shift_number):
    decrypted_message = ""

    for letter in message:
        if letter in alphabet:
            index = alphabet.index(letter)
            
            decrypted_message += alphabet[index - shift_number]
        else:
            decrypted_message += letter

    print(f"Here's the decoded result: {decrypted_message}")


check = True
while check:
    x = False
    while not x:
        to_do = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        if to_do == "encode":
            x = True
        elif to_do == "decode":
            x = True
        else:
            print("enter a valid input")
    message = input("Type your message:\n")
    shift_number = int(input("Type the shift number:\n"))

    if to_do == "encode":
        encode(message,shift_number)
    elif to_do == "decode":
        decode(message,shift_number)
    else:
        print("enter a valid input")
    
    replay = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if replay != "yes":
        check = False


# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# def caesar(start_text, shift_amount, cipher_direction):
#   end_text = ""
#   if cipher_direction == "decode":
#     shift_amount *= -1
#   for char in start_text:

#     if char in alphabet:
#         position = alphabet.index(char)
#         new_position = position + shift_amount
#         end_text += alphabet[new_position]
#     else:
#         end_text += char
    
#   print(f"Here's the {cipher_direction}d result: {end_text}")

# from art import logo
# print(logo)

# check = True
# while check:
#     direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
#     text = input("Type your message:\n").lower()
#     shift = int(input("Type the shift number:\n"))%26
#     caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
#     repeat = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
#     if repeat== "no":
#         check = False
#         print("Goodbye")