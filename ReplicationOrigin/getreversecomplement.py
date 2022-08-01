
#Isavannah Reyes
#Scripts for Bioinformatics Specialization by UCSD on Coursera 
#Reverse Complement Problem: Find the reverse complement of a DNA string.

#Input: A DNA string Pattern.
#Output: Patternrc , the reverse complement of Pattern.
#Code Challenge: Solve the Reverse Complement Problem.

def getReverseComplement(sequence):
	#DNA base pair complements dictionary
	complements = { 'A':'T', 
					'G':'C', 
					'T':'A', 
					'C':'G'}
	#Initialize
	complementarySequence = ''

	#Read through the sequence backwards so that we get the complement in a 5->3 direction
	#The sequence we are given is in a 5' -> 3' direction. So in order to have a result in the same readable diirection 
	#we need to read it backwards to get the complement due to the biderectional nature of DNA.
	for i in range(len(sequence), 0, -1):
		#i-1 to support 0 based indexing
		#print(i-1)
		complementarySequence += complements[sequence[i-1]]
	return complementarySequence

#Test
#Input: AAAACCCGGT
#Expected output: ACCGGGTTTT
print('The reverse complement of AAAACCCGGT is ', getReverseComplement('AAAACCCGGT'))


#Data File
text_file = open("dataset_3_2.txt", "r")

#Get the sequence of the data file
sequence = text_file.readline().strip()

#close file
text_file.close()

print('The reverse complement of the given sequence is ', getReverseComplement(sequence))

