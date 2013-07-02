m = 0
for i in range(999,100,-1):
	for j in range(999,100,-1):
		t = i*j
		s = str(t)
		if s[3:] == s[:3][::-1]:
			if t > m:
				m = t

print m
