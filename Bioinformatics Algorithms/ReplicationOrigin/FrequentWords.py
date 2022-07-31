#Isavannah Reyes
#Scripts for Bioinformatics Specialization by UCSD on Coursera 

#Psuedocode
#FrequentWords(Text, k)
#    FrequentPatterns =van array of strings of length 0
#    freqMap = FrequencyTable(Text, k)
#    max = MaxMap(freqMap)
#    for all strings Pattern in freqMap
#        if freqMap[pattern] ==max
#            append Pattern to frequentPatterns
#    return frequentPatterns

#Find the most frequent words of length k in a given text
def FrequentWords(Text, K):
	#Frquency Table
	FrequentMap= {}
	#Initalize
	mostFrequent = []
	maxcount = 1
	

	#Traverse through text
	for i in range((len(Text) - K) + 1):
		#Get  word of length k 
		kmer = Text[i: (i+K)] 
		#print(kmer)
		#Check if the pattern is already in the FrequentMap dictionary
		#Existing in dictionary already, so at LEAST a count of 1 
		if kmer in FrequentMap:
			#Alreaedy in dictionary, so add to the count
			FrequentMap[kmer] += 1
			
			#Getting most frequent
			#Add to the mostFrequent list if count is equal to the current max count
			if FrequentMap[kmer] == maxcount:
				mostFrequent.append(kmer)
			#If the kmers count is higher than max count, then add to max count  
			#clear the list to include the current most Frequent kmer		
			if FrequentMap[kmer] > maxcount:
				maxcount += 1
				mostFrequent.clear()
				mostFrequent.append(kmer)

		#kmer is not in the dictionary
		else:
			#Add to dictionary
			FrequentMap[kmer] = 1 
			#Corner case - first entry, so we need an entry into most Frequent list 
			#Check if list is empty
			if not mostFrequent:
				#list is empty 
				mostFrequent.append(kmer)

	#print("AATTT", FrequentMap["AATTT"], "ATTTC", FrequentMap['ATTTC'], "TTTCC", FrequentMap['TTTCC'])
	#print (FrequentMap)

	
	return mostFrequent

#Inputs
#Expected Output is AATTT
words = FrequentWords('ACAAATTTGCATAATTTCGGGAAATTTCC', 5)
print("The most frequent word in ACAAATTTGCATAATTTCGGGAAATTTCC is ", words[0])

#ACGTTGCATGTCGCATGATGCATGAGAGCT
#4
#Expected Output is CATG GCAT
words = (FrequentWords('ACGTTGCATGTCGCATGATGCATGAGAGCT',4))
print("The most frequent words in ACGTTGCATGTCGCATGATGCATGAGAGCT are", words[0], ' and ', words[1])

#Data File
text_file = open("dataset_2_13.txt", "r")
#
#first line is the dataset text
data = text_file.readline().strip()
k = text_file.readline().strip()

#close file
text_file.close()
#print(pattern)
words = (FrequentWords(data, int(k)))
print("The most frequent words in the data set is ", words[0])
#Output:ACTAGGATTCA

