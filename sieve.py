from fractions import gcd
import operator
import functools

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

def even(given):
  factors = given.values()[0]
  for number in factors: 
    if (factors.count(number) % 2 != 0): return False
  return True 

def build_relations(z):
  # first check to see if any of the vectors are already in the desired state
  return [vector for vector in z if (even(vector["z"]) and even(vector["zn"]))]

def get_gcd(primes_v, primes_vn):
  v = reduce(lambda x,y:x*y, list(set(primes_v)))
  vn = reduce(lambda x,y:x*y, list(set(primes_vn)))
  return [gcd((vn-v), n), gcd((vn+v), n)] 

z = []
for i in range(2, n):
  given = i
  if b_smooth(i) and b_smooth(i+n):
    z.append({"z": {i: p_factors(i)}, "zn": {i+n: p_factors(i+n) } })

relations = build_relations(z)

print "factorization of %s is %s" % (n, get_gcd(relations[0]["z"].values()[0], relations[0]["zn"].values()[0]))



