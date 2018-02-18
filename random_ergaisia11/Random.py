import Random_add
import random
words=[]
words_in_table=[]
while True:
	try:
		ans=raw_input("What file would you like to open(type 'exit' to exit) :")
		break
	except:
		print "file not found" 
if (ans!="exit"):
	file=open("example.txt")

	lines=100
	rows=100
	table=Random_add.rand_table(lines,rows)


	for line in file :

		temp=line.split(" ")
		temp= map(lambda s: s.strip(), temp)
		temp = filter(None, temp)
		

		for word in temp :
			if (word not in words): 
				words.append(word.upper())
				

	for i in range(100):
		words_in_table.append("")
		for j in range(100):
			words_in_table[i]+=table[i][j]
	for i in range(100):
		words_in_table.append("")
		for j in range(100):
			words_in_table[100+i]+=table[j][i]

	for word1 in words:
	
		for word2 in words_in_table:
			if(word1 in word2):
				
				print word1 +" in table as :"+word2
				break
				
