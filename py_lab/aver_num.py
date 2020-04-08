#!/usr/bin/python3

N = int(input('count? : '))

num=0
temp=0 
i=0
ave=0

for i in range(0,N):
	temp=int(input())
	num=num+temp
	
ave=num/N

print("average is : %lf "%(ave))

