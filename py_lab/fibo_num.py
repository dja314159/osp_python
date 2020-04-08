#!/usr/bin/python3

num=int(input("fibonacci number?"))

a=[]

fib1=1
fib2=1
i=0
a.append(1)
a.append(1)

for i in range (2,num,1):
	a.append(a[i-1]+a[i-2])


for i in range (0,num):
	if i!=(num-1):
		print(a[i], end=',')
	else:
		print(a[i], end='\n')

print("F%d = %d"%(num,a[num-1]))
