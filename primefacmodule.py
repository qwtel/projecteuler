import random
import collections

def primesbelow(N):
	# http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
	#""" Input N>=6, Returns a list of primes, 2 <= p < N """
	correction = N % 6 > 1
	N = (N, N-1, N+4, N+3, N+2, N+1)[N%6]
	sieve = [True] * (N // 3)
	sieve[0] = False
	for i in range(int(N ** .5) // 3 + 1):
		if sieve[i]:
			k = (3 * i + 1) | 1
			sieve[k*k // 3::2*k] = [False] * ((N//6 - (k*k)//6 - 1)//k + 1)
			sieve[(k*k + 4*k - 2*k*(i%2)) // 3::2*k] = [False] * ((N // 6 - (k*k + 4*k - 2*k*(i%2))//6 - 1) // k + 1)
	return [2, 3] + [(3 * i + 1) | 1 for i in range(1, N//3 - correction) if sieve[i]]

# http://en.wikipedia.org/wiki/Miller-Rabin_primality_test#Algorithm_and_running_time
def miller_rabin_witness(a, d, n, s): # True is witness, False is not
	x = pow(a, d, n)
	
	if x == 1 or x == n - 1: return False
	
	for r in range(s - 1):
		x = pow(x, 2, n)
		if x == 1: return True
		if x == n - 1: break
	else: return True
	
	return False

tests = ((2, 3), (31, 73), (2, 7, 61), (2, 3, 5, 7, 11), (2, 3, 5, 7, 11, 13), (2, 3, 5, 7, 11, 13, 17))
testlimits = (1373653, 9080191, 4759123141, 2152302898747, 3474749660383, 341550071728321)
_tests = len(tests)

smallprimeset = set(primesbelow(100000))
_smallprimeset = 100000
def isprime(n, precision=7):
	if n < 1:
		raise ValueError("Out of bounds, first argument must be > 0")
	elif n == 2:
		return True
	elif n == 1 or n % 2 == 0:
		return False
	elif n < _smallprimeset:
		return n in smallprimeset

	d = n - 1
	s = 0
	while d % 2 == 0:
		d //= 2
		s += 1

	for test in range(_tests):
		if n < testlimits[test]: break
	else: # use default algorithm
		for repeat in range(precision):
			a = random.randrange(2, n - 2)
			if miller_rabin_witness(a, d, n, s):
				return False

		return True

	for a in tests[test]: # use the small n tests
		if miller_rabin_witness(a, d, n, s):
			return False

	return True

# https://comeoncodeon.wordpress.com/2010/09/18/pollard-rho-brent-integer-factorization/
def pollard_brent(n):
	if n % 2 == 0: return 2
	if n % 3 == 0: return 3

	y, c, m = random.randint(1, n-1), random.randint(1, n-1), random.randint(1, n-1)
	g, r, q = 1, 1, 1
	while g == 1:
		x = y
		for i in range(r):
			y = (pow(y, 2, n) + c) % n

		k = 0
		while k < r and g == 1:
			ys = y
			for i in range(min(m, r-k)):
				y = (pow(y, 2, n) + c) % n
				q = q * abs(x-y) % n
			g = gcd(q, n)
			k += m
		r *= 2
	if g == n:
		while True:
			ys = (pow(ys, 2, n) + c) % n
			g = gcd(abs(x - ys), n)
			if g > 1:
				break

	return g

smallprimes = tuple(primesbelow(1000)) # might seem low, but 1000*1000 = 1000000, so this will fully factor every composite < 1000000
def primefactors(n, sort=False):
	factors = []

	limit = int(n ** .5) + 1
	for checker in smallprimes:
		if checker > limit: break
		while n % checker == 0:
			factors.append(checker)
			n //= checker
			if checker > limit: break

	if n < 2: return factors
	
	return factors + bigfactors(n, sort) # trial division did not fully factor, switch to pollard-brent

def bigfactors(n, sort=False):
	factors = []
	while n > 1:
		if isprime(n):
			factors.append(n)
			break

		factor = pollard_brent(n)
		factors.extend(bigfactors(factor, sort)) # recurse to factor the not necessarily prime factor returned by pollard-brent
		n //= factor

	if sort: factors.sort()	
	return factors

def factorization(n):
	factors = collections.defaultdict(int)
	for p1 in primefactors(n): factors[p1] += 1

	return factors

totients = {}
def totient(n):
	if n == 0: return 1

	if n in totients:
		return totients[n]
	
	tot = 1
	for p, exp in factorization(n).items():
		tot *= (p - 1)  *  p ** (exp - 1)
	
	totients[n] = tot
	return tot

def gcd(a, b):
	if a == b: return a
	while b > 0: a, b = b, a % b
	return a

def lcm(a, b):
	return abs(a * b) // gcd(a, b)

def isperm(a, b):
	if a == b: return False
	if type(a) == int:
		c = [0] * 10

		while a:
			c[a % 10] += 1
			a //= 10
	
		while b:
			c[b % 10] -= 1
			b //= 10
	
		for count in c:
			if count != 0: return False
		return True

	for char in set(a):
		if b.count(char) != a.count(char):
			return False
		return True

# decorators
def profile(func):
	import time
	import os
	
	def wrapper(*arg):
		if os.name == "nt":
			timer = time.clock
		else:
			timer = time.time
		
		start = timer()
		res = func(*arg)
		stop = timer()

		print("%s took %0.3f s" % (func.__name__, stop - start))
		return res
	return wrapper