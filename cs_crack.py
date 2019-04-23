import string

import re



ALPHABET = string.ascii_uppercase





alphabets = [ALPHABET[-i:].lower() + ALPHABET[:-i].lower() for i in range(len(ALPHABET))]



# print(alphabets)



ciphertext = raw_input("Type encrypted message here in all capitals: ")



for alphabet in alphabets:

	decrypt = ciphertext

	for LETTER in ALPHABET:

		#print(LETTER)

		#print(ALPHABET)

		#print(alphabet)

		#index = re.match(LETTER, ALPHABET)

		index = ALPHABET.find(LETTER)

		#print(index)

		decrypt = decrypt.replace(LETTER, alphabet[index])

	print(decrypt)






