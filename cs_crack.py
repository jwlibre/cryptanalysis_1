import string
import re

# This script takes in a Caesar-shifted string from the user,
# and outputs each of the 26 possible plaintexts.

ALPHABET = string.ascii_uppercase
alphabets = [ALPHABET[-i:].lower() + ALPHABET[:-i].lower() for i in range(len(ALPHABET))]

ciphertext = raw_input("Type encrypted message here: ")
ciphertext = ciphertext.upper()

for alphabet in alphabets:
	decrypt = ciphertext

	for LETTER in ALPHABET:

		index = ALPHABET.find(LETTER)
		decrypt = decrypt.replace(LETTER, alphabet[index])

	print(decrypt)






