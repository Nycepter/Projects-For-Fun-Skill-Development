alphabet = [',', 'y', "'", 'g', '-', '1', '~', 'e', '=', 'x', '8', 'u', 'r', '$', 'd', 'a', 'z', 'n', 'f', 't', '^', '#', 'w', '?', '+', '_', 'c', '4', ')', '<','!', 'm', '9', ' ', '3', '%', '.', 'h', 'k', '`', 'i', ':', ';', '@', 'q', '(', '*', '&', 'v', 'b', '6', '7', 'o', 'l', '/', '0', 's', '2', 'j', 'p', '5', '>', '"']


def encrypt(message, shifter):
    list_message = list(message)
    encrypted_message = []
    shifted_letters = 1
    for letter_to_be_shifted in list_message:
        if letter_to_be_shifted in alphabet:
            index_of_letter = alphabet.index(letter_to_be_shifted)
            if shifted_letters % 2 == 0:
                shifted_index = (index_of_letter +
                                 (shifter - shifted_letters)) % 63
                shifted_letter = alphabet[shifted_index]
                encrypted_message.append(shifted_letter)
                shifted_letters += 1
            else:
                shifted_index = (index_of_letter -
                                 (shifter + shifted_letters)) % 63
                shifted_letter = alphabet[shifted_index]
                encrypted_message.append(shifted_letter)
                shifted_letters += 1

        else:
            encrypted_message.append(letter_to_be_shifted)
    encrypted_message_finished = "".join(encrypted_message)
    print("\nYour encrypted message is:")
    print(f"{encrypted_message_finished} \n")


def decrypt(message, shifter):
    list_message = list(message)
    encrypted_message = []
    shifted_letters = 1
    for letter_to_be_shifted in list_message:
        if letter_to_be_shifted in alphabet:
            index_of_letter = alphabet.index(letter_to_be_shifted)

            if shifted_letters % 2 == 0:
                shifted_index = (index_of_letter -
                                 (shifter - shifted_letters)) % 63
                shifted_letter = alphabet[shifted_index]
                encrypted_message.append(shifted_letter)
                shifted_letters += 1
            else:
                shifted_index = (index_of_letter +
                                 (shifter + shifted_letters)) % 63
                shifted_letter = alphabet[shifted_index]
                encrypted_message.append(shifted_letter)
                shifted_letters += 1
        else:
            encrypted_message.append(letter_to_be_shifted)
    encrypted_message_finished = "".join(encrypted_message)
    print("\nYour decrypted message is:")
    print(f"{encrypted_message_finished} \n")


while True:
    choice = input("Would you like to encrypt or decrypt a message?\n").lower()
    if choice == "encrypt":
        encrypt(input("\nEnter the message you would like to encrypt: \n"),
                int(input("\nEnter the number key: \n")))
        continue
    elif choice == "decrypt":
        decrypt(input("\nEnter the message you would like to decrypt: \n"),
                int(input("\nEnter the number key: \n")))
        continue
    else:
        print("\nError, please choose encrypt or decrypt. \n")
        continue
