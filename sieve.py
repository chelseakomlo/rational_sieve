
# lazy, you could use the sieve of Eratosthenes to find primes
PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 
          127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181]
n = 187
bound = 7 # chosen aribitrarily
factor_base = [2, 3, 5, 7] # primes less than chosen bound

# first step is to test for divisibility by each number in the factor base. 
# if n is evenly divided by one of these, then we are finished.

# find positive integers z, where z is a number whose prime factors are in the factor_base

def b_smooth(given):
  factors = []
  for prime in PRIMES:
    if given % prime == 0:
      factors.append(prime)
      given //= prime

  not_in_factor_base = [factor for factor in factors if factor not in factor_base]
  return len(not_in_factor_base) == 0

z = []

for i in range(2, n):
  given = i
  if b_smooth(i):
    if b_smooth(i+n):
      z.append(i)

print "z %s" % z


