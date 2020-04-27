def binToOther():
	n = int(input("input binary number:"))


	oct = 0
	dec = 0
	hex = []


	temp = n
	sqr = 0
	while(temp!=0):
		c = int(temp%10)
		temp/=10	
		b = int(temp%10)
		temp/=10	
		a = int(temp%10)
		temp = int(temp/10)
		oct += (10**(sqr))*(4*a+2*b+1*c)
		sqr+=1


	temp = n
	sqr = 0	
	while(temp!=0):
		dec+= int(temp%10)*(2**(sqr))
		temp = int(temp/10)
		sqr +=1	

	temp = n
	sqr = 0
	while(temp!=0):
		d = int(temp%10)
		temp/=10	
		c = int(temp%10)
		temp/=10	
		b = int(temp%10)
		temp/=10	
		a = int(temp%10)
		temp = int(temp/10)
		value = 8*a+4*b+2*c+1*d
		if value<10:
			hex.append(value)
		elif value==10:
			hex.append('A')
		elif value==11:
			hex.append('B')
		elif value==12:
			hex.append('C')
		elif value==13:
			hex.append('D')
		elif value==14:
			hex.append('E')
		else:
			hex.append('F')


	hex.reverse()
	print("=> OCT> %d "%(oct))
	print("=> DEC> %d "%(dec))
	print("=> HEX> ",end ='')
	for i in hex:
		print(i,end='')
	print("")

		
	

