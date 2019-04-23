import string
import pdb

# the idea of periodicity is that ciphertext[1] is encoded with alphabet[1],
# ciphertext[2] with alphabet[2], etc, until the period length, p:
# ciphertext[p] with alphabet[p]
# ciphertext[p+1] with alphabet [1]
# hence, the frequency analysis needs to extract characters and put them into
# their relevant bins one at a time, rather than skimming off the first p
# cipher characters, the second p cipher characters, etc.

p = int(raw_input("Select periodicity 'p' of cipher: "))

f = open('msg1.txt','r')
text = f.read()
f.close()

text = text.upper()

q = open('msg1_capsonly.txt','w')
q.write(text)
q.close()

f = open('msg1.txt','r')
text = f.readlines()
f.close()


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

output1 = open('msg1_allcaps.txt','w')
output1.write(adapted_text)
output1.close()

length = len(adapted_text)

# extract 1st character, put it in the first bin
# extract 2nd character, put it in the second bin
# extract pth character, put it in the pth bin
# extract p+1th character, put it in the first bin

bins = {}
for k in range(0,p):
	bins[k] = ''

for j in range(0, length):
	bin_index = j % p
	bins[bin_index] = bins[bin_index] + adapted_text[j]	



# now do a frequency analysis on each bin and find the index of coincidence each time

# now do a line-by-line character frequency calculation
ALPHABET = string.ascii_uppercase

frequency_analysis = {}

for i in range(len(bins)):
	alphabet_temp = {}
	for letter in ALPHABET:
		alphabet_temp[letter] = 0
		for character in bins[i]:
			if character == letter:
				alphabet_temp[letter] = alphabet_temp[letter] + 1
	frequency_analysis[i] = alphabet_temp
	

# now calculate index of coincidence for each of the bins
indices_of_coincidence = {}

for i in range(len(frequency_analysis)):
	numerator = 0.0
	denominator = 0.0
	for letter in frequency_analysis[i].keys(): # bins[i].keys = letters in alphabet, bins[i].values = frequency of letter occuring in bin
		numerator = numerator + (frequency_analysis[i][letter] * (frequency_analysis[i][letter] - 1))
	denominator = len(bins[i]) * (len(bins[i]) - 1)
	denominator = denominator / 26

	ic = numerator / denominator
	indices_of_coincidence[i] = ic

print(indices_of_coincidence)

pdb.set_trace()
# now, we treat the separate bins as individual messages,
# which we decrypt using the frequency analysis done earlier



