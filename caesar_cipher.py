#!/usr/bin/python3
import sys
import string

# Constants
MAX_KEY_SIZE = 26
ALPHABET = (string.ascii_uppercase)
LetterList = (string.ascii_lowercase)
PUNCTUATION = string.punctuation

Input = sys.argv

"""
User input functions
"""

def get_cipher_mode():
    """
    Gets user input for the cipher mode. Must be either encrypt, e, decrypt or d.
    
    Returns cipher_mode as a string.
    """
    while True:
        cipher_mode = str(Input[1])
        if cipher_mode in "encrypt e decrypt d".split():
            return cipher_mode
        else:
            print("wrong input")
        
            

def get_shift_value():
    """
    Gets user input for the shift value. Must be a positive integer.
    
    Returns shift_value as an int.
    """
    while True:
        shift_value = str(Input[2])
        if not shift_value.isdigit():
            print("wrong input")
        elif int(shift_value) < 0:
            print("wrong input")
        else:
            return int(shift_value)


def get_msg():
    global msg
    """
    Gets user input for the text. It continues reading in input until the user
    inputs an empty line (i.e. double enter).
    """
    line = str(Input[3:])
    msg = ""

    while line != "":
        msg += line
        line = input()
        
    return msg
    
"""
File usage functions
"""

def ret_file_msg(file_name):
    pass
        
def write_msg_to_file(file_name, msg):
    pass
    
"""
Cipher functions
"""

def translate_msg(shift_value, msg):
    """
    Performs the Caesar cipher on a string converted to upper case with the given shift.
    
    shift_value : int
        shift amount/rotation value for the cipher. Positive encrypts and negative decrypts.
    msg : str
        message to be translated
    
    Returns the translated message as a string.
    """
    translated_msg = ''

    for symbol in msg:
        # Need to check Symbol is a letter
        if symbol.isalpha():
            if symbol in ALPHABET:
                position = ALPHABET.index(symbol)
                new_symbol = ALPHABET[(position + shift_value) % MAX_KEY_SIZE]
            else:
                position = LetterList.index(symbol)
                new_symbol = LetterList[(position + shift_value) % MAX_KEY_SIZE]
            translated_msg += new_symbol
        else:
            # Leave Symbol unchanged if it's not a letter
            translated_msg += symbol

    return translated_msg
    

def caesar_encrypt(shift_value, msg):
    """
    Wrapper function for translate_msg
    
    N.B. shift value kept positive for encryption.
    """
    return translate_msg(shift_value, msg)
    

def caesar_decrypt(shift_value, msg):
    """
    Wrapper function for translate_msg
    
    N.B. shift value becomes negative for decryption.
    """
    return translate_msg(-shift_value, msg)

"""
Main function
"""
def main():
    mode = get_cipher_mode()
    shift = get_shift_value()    
    text = get_msg()
    
    if mode[0] == "e":
        translated_msg = caesar_encrypt(shift, msg)
    else:
        translated_msg = caesar_decrypt(shift, msg)
        
    print(translated_msg)


if __name__ == '__main__':
    main()
    sys.exit(1)
