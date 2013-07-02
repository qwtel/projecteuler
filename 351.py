from math import *

n = 5
A = [0 for i in range(0,n+1)]

def create_matrix(n):
	for i in range(1,n+1):
		c = 0
		B = []
		x = sqrt(i)
		for j in range(1,i/2+1):
			if i%j is 0:
				c += j - A[j]
				B.append(j-A[j])
			else:
				B.append(0)
		#print str(i)+':'
		#print B
		#print sum(B)
		A[i] = c

def create_slice(n):
	for i in range(1,n+1):
		c = 0
		r = int(sqrt(i))
		if i%100000 == 0:
			print i
	   	#for j in range(1,r+1):
	   	#	if i%j == 0:
	   	#		c += j-A[j]
       	#
       	#
	   	#		if j != 1:
	   	#			x = i/j
	   	#			c += x-A[x]
	   	#			#print str(i)+'%'+str(j)+' ~:'+str(x)
	   	#		else:
	   	#			pass
	   	#			#print str(i)+'%'+str(j)
       	#
	   	#A[i] = c

def sum_up():
	s = 0
	for r in A:
		s += r
	
	return s*6

def e351():
	create_slice(n)
	print sum_up()

   	#create_matrix(n)
   	#print sum_up()

e351()
