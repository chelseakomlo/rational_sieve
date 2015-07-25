
n = 187
bound = 7 # chosen aribitrarily
factor_base = [2, 3, 5, 7] # primes less than chosen bound

def p_factors(given):
  factors = []
  for i in xrange(2, given):
    while given % i == 0:
      factors.append(i)
      given //= i
  if given > 1: factors.append(given)
  return factors

def b_smooth(given):
  factors = p_factors(given)
  not_smooth = [factor for factor in factors if factor not in factor_base]
  return len(not_smooth) == 0

def build_relations(z):
  #multiply together these various relations in such a way that the exponents of the primes are all even
  # first check to see if any of the vectors are in the state that we want (where all of the exponents are even)
  pass

def gcd(primes):
  pass

z = []
for i in range(2, n):
  given = i
  if b_smooth(i) and b_smooth(i+n):
    z.append({"z": {i: p_factors(i)}, "zn": {i+n: p_factors(i+n) } })

relations = build_relations(z)

print "z %s" % z


