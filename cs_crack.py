import string
import re

# This script takes in a Caesar-shifted string from the user,
# and outputs each of the 26 possible plaintexts.

def cs_crack(ciphertext):

	plaintexts = []
	ciphertext = ciphertext.upper()

	ALPHABET = string.ascii_uppercase
	alphabets = [ALPHABET[-i:].lower() + ALPHABET[:-i].lower() for i in range(len(ALPHABET))]

	for alphabet in alphabets:
		decrypt = ciphertext

		for LETTER in ALPHABET:

			index = ALPHABET.find(LETTER)
			decrypt = decrypt.replace(LETTER, alphabet[index])

		plaintexts.append(decrypt)

	return plaintexts
