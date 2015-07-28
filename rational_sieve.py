from fractions import gcd
from functools import reduce

class Sieve():

  def __init__(self, n, bound, factor_base):
    self.n = n
    self.bound = bound
    self.factor_base = factor_base
    self.cache = {}

  def get_factors(self):
    relations = self.build_b_smooth()
    possible_relations = [relation for relation in relations if self.even(relation["z"])]
    for relation in possible_relations:
      gcd = self.get_gcd(relation)
      if self._is_factorization(gcd):
        print("Potential factorization of %s is %s, %s" % (self.n, gcd[0], gcd[1]))

  def build_b_smooth(self): 
    relations = []
    for i in range(2, self.n): 
      if self._b_smooth(i): 
        relation = {"z": self.pfactors(i), "zn": self.pfactors(i+self.n)}
        relations.append(relation)
    return relations

  def even(self, factors):
    for unique in set(factors):
      if (factors.count(unique) % 2) != 0: return False
    return True

  def pfactors(self, given):
    if self.cache.get(given): return self.cache[given]
    return self._build_pfactors(given)

  def get_gcd(self, relation):
    z_pfactrs = reduce(lambda x, y: x*y, set(relation["z"])) 
    zn_pfactrs = reduce(lambda x, y: x*y, set(relation["zn"])) 
    return (gcd((zn_pfactrs - z_pfactrs), self.n), gcd((zn_pfactrs + z_pfactrs), self.n))

  def _build_pfactors(self, given):
    pfactors = []
    for i in range(2, given):
      while given % i == 0:
        pfactors.append(i)
        given //= i
    if given > 1: pfactors.append(given)
    self.cache[given] = pfactors
    return pfactors

  def _b_smooth(self, given):
   factors = self.pfactors(given) + self.pfactors(given + self.n) 
   return max(factors) in self.factor_base

  def _is_factorization(self, gcd):
    return gcd[0] * gcd[1] == self.n

if __name__ == "__main__":
      sieve = Sieve(187, 11, [2, 3, 5, 7, 11])
      sieve.get_factors()
