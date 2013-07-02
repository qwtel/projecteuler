# ZU LANGSAM
import time
import primefacmodule as pfm

start=time.time()

c=[]

def b(n):
	s=0
	for x in xrange(1,n+1):
		t=pfm.totient(x)
		s+=t
	return n*(n-1)/2 + 1 - s
	
def anzahl(n):
	return 6*(n-1)+6*b(n)


print anzahl(100000000)
print time.time()-start

# n*(n-1)/2 + 1 - sum( phi(i), i=1..n)
#100k 11762395476
#1m 1176221685648

#11762187201804552
#4362.30590796

