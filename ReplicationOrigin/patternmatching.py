#Isavannah Reyes
#Scripts for Bioinformatics Specialization by UCSD on Coursera 
#Code Challenge: Solve the Pattern Matching Problem.

#Input: Two strings, Pattern and Genome.
#Output: A collection of integers specifying all starting positions where Pattern appears as a substring of #Genome.

def patternMatching(pattern, genome): 
	
	#Variables
	patternlength = len(pattern)
	matchingStartLocations =[]


	#Traverse through inputed Text 
	#If text is GCGCG and the pattern is 'GCG' then we go for the length of text (5) - the pattern length (3) = 2
	#Traverse 0, 1, 2
	for i in range((len(genome) - patternlength) + 1):
		

		#If pattern is found, add to list
		if genome[i: (i+patternlength)] == pattern:
			matchingStartLocations.append(i)
			#print(Text[i: (i+patternlength)])

	return matchingStartLocations
#Input
#ATAT
#GATATATGCATATACTT
#Expected Output: 1 3 9
print('The locations for ATAT in GATATATGCATATACTT can be found at' ,patternMatching('ATAT', 'GATATATGCATATACTT'))


text_file = open("dataset_3_5.txt", "r")
#
#first line is the pattern 
pattern = text_file.readline().strip()
#second line is the genome to search
genome = text_file.readline().strip()

#close file
text_file.close()
#print(pattern)

print("The locations for ", pattern, " in your data set can be found at", ' '.join(map(str,patternMatching(pattern, genome))))


#Vibrio Cholera
text_file = open("Vibrio_cholerae.txt", "r")
#read genome
genome = text_file.readline().strip()

#close file
text_file.close()

#Looking for start locations of dnaAbox in Vibrio cholerae: CTTGATCAT

print("The locations for DNAa box: CTTGATCAT in the V. cholerae genome can be found at", ' '.join(map(str,patternMatching('CTTGATCAT', genome))))


#Looking for start locations of dnaAbox in Vibrio cholerae: ATGATCAAG This is the reverse complelemt of CTTGATCAT

print("The locations for DNAa box: ATGATCAAG in the V. cholerae genome can be found at", ' '.join(map(str,patternMatching('ATGATCAAG', genome))))

