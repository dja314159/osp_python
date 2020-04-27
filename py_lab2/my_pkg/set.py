def setCal():
	import sys
	import re	

	temp1 = input("1st list: ")
	temp2 = input("2nd list: ")

	

	set1 = []
	set2 = []
	intersection = []	
	
	set1 = re.findall("\d+",temp1)
	set2 = re.findall("\d+",temp2)



	for i in set1:
		for j in set2:
			if (i==j):
				intersection.append(i)
	intersection.sort()

	for i in set2:
		check = 0	
		for j in set1:
			if (j==i):
				check+=1
		if(check==0):
			set1.append(i)
	
	set1.sort()

	print("=> union [",end='')
	for i in range(len(set1)):
		print(set1[i],end='')
		if(i==len(set1)-1):
			print("]")
		else:
			print(",",end='')
		
	print("=> intersection [",end='')
	for i in range(len(intersection)):
		print(intersection[i],end='')
		if(i==len(intersection)-1):
			print("]")
		else:
			print(",",end='')
				
