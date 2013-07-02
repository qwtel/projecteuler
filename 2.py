n = 1
m = 1
s = 0
r = 0

while m < 4000000:
	s += n+m
	n=m
	m=s

	if s%2 == 0:
		r += s
	s=0

print r
