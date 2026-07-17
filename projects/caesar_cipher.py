"""
Caesar Cipher Encryption and Decryption
Author: Sarim Khan
Description:
A simple Python program that encrypts and decrypts text using the Caesar Cipher.
"""

def caesar(text, shift, encrypt=True):

    if not isinstance(shift, int):
        return 'Shift must be an integer value.'

    if shift < 1 or shift > 25:
        return 'Shift must be an integer between 1 and 25.'

    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    if not encrypt:
        shift = -shift

    shifted_alphabet = alphabet[shift:] + alphabet[:shift]

    translation_table = str.maketrans(
        alphabet + alphabet.upper(),
        shifted_alphabet + shifted_alphabet.upper()
    )

    return text.translate(translation_table)


def encrypt(text, shift):
    return caesar(text, shift)


def decrypt(text, shift):
    return caesar(text, shift, False)


# Examples
print("Encryption Example")
encrypted = encrypt("Cristiano Ronaldo", 5)
print("Encrypted:", encrypted)

print("\nDecryption Example")
decrypted = decrypt(encrypted, 5)
print("Decrypted:", decrypted)

print("\nROT13 Example")
rot13 = encrypt("Greatest of all time", 13)
print("Encrypted:", rot13)
print("Decrypted:", decrypt(rot13, 13))
