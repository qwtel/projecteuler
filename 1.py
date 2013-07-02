import math

s = 0
for i in range(1000):
	if i*3 < 1000:
		s+=i*3
	if i*5 < 1000:
		s+=i*5
	if i*15 < 1000:
		s-=i*15

print s
