from decimal import *
getcontext().prec = 1999

res = tmp = ii = 0

def check(n):
	s = str(Decimal(1)/Decimal(n))[2:]
	for c in xrange(2,len(s)):
		for os in xrange(0,2):
			if s[os+c:os+c+c] == s[os:os+c]:

				return c

for i in xrange(2,1000):
	tmp = check(i)
	if tmp:
		if tmp > res:
			res = tmp
			ii = i
		print str(i) + ': ' + str(tmp)
				
print ii
