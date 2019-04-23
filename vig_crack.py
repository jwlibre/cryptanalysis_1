import string
import re
import pdb
import pandas as pd
import math

# returns plaintext from a ciphertext enciphered using the Vigenere cipher,
# taking the ciphertext and keyword as direct input from the user.

alphabet = string.ascii_lowercase
ALPHABET_UPPER = string.ascii_uppercase

ALPHABETS = [alphabet[i:].upper() + alphabet[:i].upper() for i in range(len(alphabet))]

ciphertext = raw_input("Type encrypted message here: ")
ciphertext = ciphertext.upper()
keyword = raw_input("Type keyword here: ")
keyword = keyword.upper()

# repeat the keyword so that it forms a 26-letter string
num_reps = int(math.floor(26 / len(keyword)))
leftover_chars = 26 % len(keyword)

keyword_2 = ""
if num_reps < 1:
	keyword_2 = keyword[0:26]

else:
	for i in range(num_reps):
		keyword_2 = keyword_2 + keyword

	keyword_2 = keyword_2 + keyword[0:leftover_chars]
print(keyword_2)

keyword_2 = list(keyword_2)

# construct Vigenere square
ALPHABETS_keys = [letter for letter in ALPHABET_UPPER] + ['keyword']
ALPHABETS_vals = [list(ALPHABET) for ALPHABET in ALPHABETS] + [keyword_2]

ALPHABETS = dict(zip(ALPHABETS_keys, ALPHABETS_vals))

alphabet = list(alphabet)

vig_square = pd.DataFrame(columns = alphabet, index = ALPHABETS_keys)

for index in vig_square.index:
	vig_square.loc[index] = ALPHABETS[index]

# define a keychain, which will be the keyword repeated out over the length of the message

keychain_length = len(ciphertext)

keychain = []
for i in range(keychain_length):
	key = ciphertext[i]
	value = keyword[i % len(keyword)]
	keychain.append([key, value])
	print(key, value)

# decrypt message
decrypt = ''

for i in range(len(keychain)):
	cipherletter = keychain[i][0]
	keyletter = keychain[i][1]
	ALPHABET = vig_square.loc[keyletter,:]
	ALPHABET = ALPHABET.reset_index()
	ALPHABET = ALPHABET.rename(columns = {'index':'plaintext',keyletter:'ciphertext'})
	decrypt = decrypt + ALPHABET.loc[ALPHABET['ciphertext'] == cipherletter, 'plaintext'].values[0]

print("Decrypted message below:")
print(decrypt)
