import time, math
start=time.time()
count=0
l=[]
d={}
count=0
n=0
#1155, 1755, 1920, 2079, 2304, 2688, 3003, 3135, 3315, 3360 first 10 correct ones
# (3*a+x)**2-4*x**2=3*n
#dict[key] = value


for a in xrange(1,5000):
	for x in xrange(1,3*a):
		n=((3*a+x)**2-4*x**2)/3
		if n % 1 == 0 and n>0 and n<10**6:
			l.append(n)
		
for z in l:
	if not d.has_key(z):
		d[z]=0
	d[z]+=1
#print l

for key in d:
	if d[key]==10:
		count+=1
		
print count
print time.time()-start

