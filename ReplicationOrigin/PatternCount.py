#Isavannah Reyes
#Scripts for Bioinformatics Specialization by UCSD on Coursera 

#Psuedocode
#PatternCount(Text, Pattern)
#  count = 0
#  for i = 0 to len of text - len of Pattern
#    if Text(i, len of Pattern) = Pattern
#      count = count + 1
#  return count



#Count patterns in a text
def PatternCount(Text, Pattern):

	#Variables
	count = 0 
	patternlength = len(Pattern)

	#Traverse through inputed Text 
	#If text is GCGCG and the pattern is 'GCG' then we go for the length of text (5) - the pattern length (3) = 2
	#Traverse 0, 1, 2
	for i in range((len(Text) - patternlength) + 1):
		#For our example 
		#GCGCG
		# Text from 0 -> 3 is GCG
		# Text from 1 -> 4 is CGC
		# Text from 2 -> 5 is GCG
		#print(Text[i: (i+patternlength)])

		#If pattern is found, add to count
		if Text[i: (i+patternlength)] == Pattern:
			count = count + 1
			#print(Text[i: (i+patternlength)])

	return count

#Inputs
#Expected Output is 2 
print("The count for GCG in the pattern GCGCG is ", PatternCount('GCGCG', 'GCG'))

text_file = open("dataset_2_6.txt", "r")
#
#first line is the dataset text
data = text_file.readline().strip()
#second line is the patttern to find
Pattern = text_file.readline().strip()

#close file
text_file.close()
#print(pattern)

print("The count for ", Pattern, " in your data set is ", PatternCount(data, Pattern))
