from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

print(logo)


def caesar(new_text, shift):
    if direction == "decode":
        shift *= -1
    for nr in range(len(text)):
        if text[nr] not in alphabet:
            new_text += text[nr]
        else:
            position = alphabet.index(text[nr])
            if position + shift > len(alphabet) - 1 and direction == "encode":
                new_shift = shift - (position + shift % len(alphabet) - 1) - 1
                print(new_shift)
                new_text += alphabet[new_shift]
            else:
                new_text += alphabet[position + shift]
            print(new_text)


restart = "yes"
while restart == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar("", shift=shift)
    restart = input("Do you want to restart the program? Type yes or no.")
