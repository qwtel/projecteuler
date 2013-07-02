import primefacmodule as pfm
import time
start=time.time()
a=pfm.primesbelow(1000)
r=0
for d in a: 
	for n in xrange(1,1000):
		if ((10**n)-1) % d ==0:
			if  n > r:
				r = d
			break
print r
print time.time()-start