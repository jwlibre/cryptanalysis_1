import string
import pdb

# NOTE - the frequency analysis part needs to be corrected.
# the idea of periodicity is that ciphertext[1] is encoded with alphabet[1],
# ciphertext[2] with alphabet[2], etc, until the period length, p:
# ciphertext[p] with alphabet[p]
# ciphertext[p+1] with alphabet [1]
# hence, the frequency analysis needs to extract characters and put them into
# their relevant bins one at a time, rather than skimming off the first p
# cipher characters, the second p cipher characters, etc.

f = open('msg1.txt','r')
text = f.readlines()
f.close()

i = 0
for line in text:
	adapted_line = line.upper()
	if i == 0:
		adapted_text = adapted_line
	else:
		adapted_text = adapted_text + adapted_line
	i = i+1

output1 = open('msg1_allcaps.txt','w')
output1.write(adapted_text)
output1.close()


i = 0
for line in text:
	adapted_line = line.replace(' ','')
	adapted_line = adapted_line.replace("\'", "")
	adapted_line = adapted_line.replace('\n','')
	adapted_line = adapted_line.replace(";",'')
	adapted_line = adapted_line.replace(".",'')
	adapted_line = adapted_line.replace(",",'')
	adapted_line = adapted_line.replace("-",'')
	adapted_line = adapted_line.replace("\"",'')
	if i == 0:
		adapted_text = adapted_line
	else:
		adapted_text = adapted_text + adapted_line
	i = i + 1


adapted_text = adapted_text.upper()

length = len(adapted_text)

# change 14 in the below to the trial periodicity of the text
for j in range(0, int(length / 14)):
	if j == 0:
		new_adapted_text = adapted_text[0:13:1] + '\n'
	else:
		new_adapted_text = new_adapted_text + adapted_text[(j*14)-1:((j+1)*14)-1:1] + '\n'





g = open('msg1_foranalysis.txt','w')
g.write(new_adapted_text)
g.close()

h = open('msg1_foranalysis.txt','r')


# now do a line-by-line character frequency calculation
ALPHABET = string.ascii_uppercase

frequency_analysis = {}

k = 1

for line in h.readlines():
	alphabet_temp = {}
	for letter in ALPHABET:
		alphabet_temp[letter] = 0
		for character in line:
			if character == letter:
				alphabet_temp[letter] = alphabet_temp[letter] + 1
	frequency_analysis[k] = alphabet_temp
	
	k = k+1



