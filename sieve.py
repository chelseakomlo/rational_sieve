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

def build_squares(prime, z_vector, zn_vector):
  is_odd = z_vector.count(prime) % 2 != 0
  if is_odd:
    z_vector.append(prime)
    zn_vector.append(prime)
  return {"z": {1: z_vector}, "zn": {1: zn_vector}}

def build_even(z):
  evens = []
  for vector in z:
    z_vector_prime_factors = vector["z"].values()[0]
    zn_vector_prime_factors = vector["zn"].values()[0]
    uniques = list(set(z_vector_prime_factors))
    for prime in uniques:
      evens.append(build_squares(prime, z_vector_prime_factors, zn_vector_prime_factors))
  return evens

def build_relations(z):
  evens = []
  [evens.append(vector) for vector in z if (even(vector["z"]) and even(vector["zn"]))]
  vectors_to_manipulate = [ vector for vector in z if not even(vector["z"]) ] 
  [evens.append(vector) for vector in build_even(vectors_to_manipulate) ]
  return evens

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

for relation in relations: 
  print "factorization of %s is %s" % (n, get_gcd(relation["z"].values()[0], relation["zn"].values()[0]))



