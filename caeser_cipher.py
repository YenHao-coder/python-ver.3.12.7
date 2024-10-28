 # Todo-1 : Create a function called encrypt() that takes original_text and shift_amount as 2 inputs.
 # Todo-2 : Inside the 'encypt' function, shift each letter of the original_text forwards in the alphabet by the shift_amount and print the encrypted text.
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

import art
print(art.logo)



def encrypt(original_text, shift_amount):
    encrypted = ""

    for characters in original_text:
        shift_position = alphabet.index(characters) + shift_amount
        shift_position %= len(alphabet) #偏移位置為除列表長度之餘數. 避免超出列表範圍的情形
        encrypted += alphabet[shift_position]
    print(f"Here is the encoded result: {encrypted}")

# Todo-3 : Create a function called decrypt() that takes original_text and shift_amount as 2 inputs
 # Todo-4 : Inside the decrypt() function, shift each letter of the original_text forwards in the alphabet backwards by the shift_amount and print the decrypted test.

def decrypt(original_text, shift_amount):
    decrypted = ""
    for characters in original_text:
        shift_position = alphabet.index(characters) - shift_amount
        shift_position %= len(alphabet)
        decrypted += alphabet[shift_position]
    print(f"Here is the decoded result: {decrypted}")


# Todo-5 : Combine the encrypt() and decrypt() functions into a single function called caesar(). Use the value of the user chosen direction variable to determine which functionality to use.call the caesar function instead of encrypt/decrypt and pass in all three variables direction/text/shift.
def caeser(direction_choice):
    if direction == "encode":
        encrypt(original_text = text, shift_amount = shift)
    elif direction == "decode":
        decrypt(original_text = text, shift_amount = shift)
    else:
        print("You enter wrong direction, goodbye!!")

def caesar_0(original_text, shift_amount, encode_or_decode):
    output_text = ""

    if encode_or_decode == "decode":
        shift_amount *= -1

    for characters in original_text:
        if characters not in alphabet:
            output_text += characters
        else:      
            shift_position = alphabet.index(characters) + shift_amount
            shift_position %= len(alphabet) 
            output_text += alphabet[shift_position]
    print(f"Here is the {encode_or_decode}d result: {output_text}")



# Todo-7 : Import and print the logo from art.py when the program starts.
 # Todo-8 : What happens if the user enters a number/symbol/ space when the text is encoded/decoded.
  #Todo-9 : Canyou figure out a way to restart the cipher program?
should_continue = True

while should_continue:
    direction = input("type 'encode' to encrypt, type 'decode' to decrypt:\n")

    text = input("Type the message:\n").lower()

    shift = int(input("Type the shift number:\n"))

    caesar_0(text, shift, direction)

    restart = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()
    if restart == 'no':
        should_continue = False
        print("goodbye")