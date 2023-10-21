alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]


def encrypt(message, shifter):
    list_message = list(message)
    encrypted_message = []
    shifted_letters = 0
    for letter_to_be_shifted in list_message:
        if letter_to_be_shifted in alphabet:
            index_of_letter = alphabet.index(letter_to_be_shifted)
            shifted_index = (index_of_letter -
                             (shifter - shifted_letters)) % 26
            shifted_letter = alphabet[shifted_index]
            encrypted_message.append(shifted_letter)
            shifted_letters += 1

        else:  # the spaces count as letter not in alphabet so the else statement is what includes them in the output
            encrypted_message.append(letter_to_be_shifted)
    encrypted_message_finished = "".join(encrypted_message)
    print("\nYour encrypted message is:")
    print(f"{encrypted_message_finished} \n")


def decrypt(message, shifter):
    list_message = list(message)
    encrypted_message = []
    shifted_letters = 0
    for letter_to_be_shifted in list_message:
        if letter_to_be_shifted in alphabet:
            index_of_letter = alphabet.index(letter_to_be_shifted)
            shifted_index = (index_of_letter +
                             (shifter - shifted_letters)) % 26
            shifted_letter = alphabet[shifted_index]
            encrypted_message.append(shifted_letter)
            shifted_letters += 1
        else:  # the spaces count as letter not in alphabet so the else statement is what includes them in the output
            encrypted_message.append(letter_to_be_shifted)
    encrypted_message_finished = "".join(encrypted_message)
    print("\nYour decrypted message is:")
    print(f"{encrypted_message_finished} \n")


while True:
    choice = input("Would you like to encrypt or decrypt a message?\n").lower()
    if choice == "encrypt":
        encrypt(input("\nEnter the message you would like to encrypt: \n"),
                int(input("\nEnter the number you want to shift by: \n")))
        continue
    elif choice == "decrypt":
        decrypt(input("\nEnter the message you would like to decrypt: \n"),
                int(input("\nEnter the number you want to shift by: \n")))
        continue
    else:
        print("\nError, please choose encrypt or decrypt. \n")
        continue
