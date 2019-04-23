import string
import pdb
import matplotlib.pyplot as plt

# this script takes in a message in ciphertext, which we assume has been written using a polyalphabetic cipher
# to find the periodicity of the message, we can try different periodicities up to 26, and choose the value which returns the largest average index of coincidence

ALPHABET = string.ascii_uppercase

# function to calculate the index of coincidence of a text, given trial periodicity
def calc_ic(p, text, ALPHABET):

	length = len(text)
	
	# divide the text into bins, according to the periodicity p	
	
	bins = {}
	for k in range(0,p):
		bins[k] = ''

	for j in range(0, length):
		bin_index = j % p
		bins[bin_index] = bins[bin_index] + text[j]	


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
		for letter in frequency_analysis[i].keys():
			numerator = numerator + (frequency_analysis[i][letter] * (frequency_analysis[i][letter] - 1))
		denominator = float(len(bins[i]) * (len(bins[i]) - 1))
		denominator = denominator / 26
		try:
			ic = numerator / denominator
		except:
			pdb.set_trace()		
		indices_of_coincidence[i] = ic

	average = sum(indices_of_coincidence.values())/len(indices_of_coincidence.values())

	return (average, bins)











# read in the enciphered message as a text file
f = open('msg1.txt','r')

text = f.read()
# text = f.readlines()

f.close()


text = text.upper()
text = text.replace('\n', '')

#### DO ANY NECESSARY TEXT CLEANING HERE

# pdb.set_trace() # inspect the text to see what needs to be done

# i = 0
# for line in text:
#	adapted_line = line.replace(' ','')
#	adapted_line = adapted_line.replace("\'", "")
#	adapted_line = adapted_line.replace('\n','')
#	adapted_line = adapted_line.replace(";",'')
#	adapted_line = adapted_line.replace(".",'')
#	adapted_line = adapted_line.replace(",",'')
#	adapted_line = adapted_line.replace("-",'')
#	adapted_line = adapted_line.replace("\"",'')
#	if i == 0:
#		adapted_text = adapted_line
#	else:
#		adapted_text = adapted_text + adapted_line
#	i = i + 1


# find all the ic values for all the possible periodicity values
ic_dict = {}

for p in range(1,27):
	ic = calc_ic(p, text, ALPHABET)[0]
	ic_dict[p] = ic

# print the ic_dict to the console
# CURRENTLY UNSATISFACTORY AS A MEANS OF OUTPUT
# TO DO - use matplotlib to plot the data to see the periodicity, or export the data as a csv to plot in excel
print(ic_dict)

periodicity = ic_dict.keys()
ic_values = ic_dict.values()

plt.plot(periodicity, ic_values)
plt.xlabel('periodicity')
plt.ylabel('index of coincidence')
plt.show()


p = int(raw_input('To proceed, select the periodicity to test for frequency analysis: '))

bins = calc_ic(p, text, ALPHABET)[1]

pdb.set_trace()

