alphabet = [',', 'y', "'", 'g', '-', '1', '~', 'e', '=', 'x', '8', 'u', 'r', '$', 'd', 'a', 'z', 'n', 'f', 't', '^', '#', 'w', '?', '+', '_', 'c', '4', ')', '<',
            '!', 'm', '9', ' ', '3', '%', '.', 'h', 'k', '`', 'i', ':', ';', '@', 'q', '(', '*', '&', 'v', 'b', '6', '7', 'o', 'l', '/', '0', 's', '2', 'j', 'p', '5', '>', '"']


def encrypt(message, shifter):
    """_summary_

    Args:
        message (_Str_): The message that the user wants to encrypt.
        shifter (_Int_): The initial amount that the letters are to be shifted by. 

    Description:
        This code defines a function called "encrypt" that takes two parameters: "message" and "shifter". The code first converts the "message" into a list called "list_message". It then initializes an empty list called "encrypted_message" to store the encrypted letters.

        The variable "shifted_letters" is set to 1 to keep track of the number of letters that have been shifted. The code then iterates over each letter in "list_message".

        If the letter is in the "alphabet" (undefined in the code), it proceeds to encrypt it.

        If the "shifted_letters" is divisible by 2, it calculates the shifted index by adding the "shifter" minus the "shifted_letters" to the index of the letter. Then it calculates the modulo 63 of the shifted index to ensure it remains within the range of available letters. The shifted letter is then retrieved from the "alphabet" using the shifted index and appended to the "encrypted_message" list. The "shifted_letters" variable is incremented by 1.

        If the "shifted_letters" is not divisible by 2, the shifted index is calculated by subtracting the "shifter" plus the "shifted_letters" from the index of the letter. The rest of the process is the same as the previous case.

        If the letter is not in the "alphabet", it is appended as is to the "encrypted_message" list.

        After iterating over all the letters in "list_message", the "encrypted_message" is joined back into a string called "encrypted_message_finished". Finally, the encrypted message is printed to the console.



    """
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
    """
    _summary_

    Args:
    message (_Str_): The message that the user wants to decrypt.
    shifter (_Int_): The initial amount that the letters were shifted by.

    Description:
    This code defines a function called "decrypt" that takes two parameters: "message" and "shifter". 
    The code first converts the "message" into a list called "list_message". It then initializes an empty list called "encrypted_message" to store the decrypted letters. 
    The variable "shifted_letters" is set to 1 to keep track of the number of letters that have been shifted. 
    The code then iterates over each letter in "list_message". 
    If the letter is in the "alphabet" (undefined in the code), it proceeds to decrypt it. 
    If the "shifted_letters" is divisible by 2, it calculates the shifted index by subtracting the "shifter" minus the "shifted_letters" from the index of the letter. 
    Then it calculates the modulo 63 of the shifted index to ensure it remains within the range of available letters. 
    The decrypted letter is then retrieved from the "alphabet" using the shifted index and appended to the "encrypted_message" list. 
    The "shifted_letters" variable is incremented by 1. 
    If the "shifted_letters" is not divisible by 2, the shifted index is calculated by adding the "shifter" plus the "shifted_letters" to the index of the letter. 
    The rest of the process is the same as the previous case. 
    If the letter is not in the "alphabet", it is appended as is to the "encrypted_message" list. 
    After iterating over all the letters in "list_message", the "encrypted_message" is joined back into a string called "encrypted_message_finished". 
    Finally, the decrypted message is printed to the console.
    """
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
