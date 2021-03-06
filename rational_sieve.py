from fractions import gcd
from functools import reduce

class Sieve():

  def __init__(self, n, bound, factor_base):
    self.n = n
    self.bound = bound
    self.factor_base = factor_base

  def get_factors(self):
    relations = self.build_relations()
    possible_r = [r for r in relations if self.even(r["z"])] # next step is to convert non-even relations
    for relation in possible_r:
      gcd = self.get_gcd(relation)
      if self.__factors(gcd): print("Potential factors of %s is %s, %s" % (self.n, gcd[0], gcd[1]))

# should return relations that have primes only within the factor base
# everything else should be thrown away
  def build_relations(self): 
    relations = []
    for i in range(2, self.n): 
      z_factors = self.pfactors(i)
      if self.__b_smooth(z_factors): 
        zn_factors = self.pfactors(i+self.n)
        relations.append({"z": z_factors, "zn": zn_factors})
    return relations

  def even(self, factors):
    for unique in set(factors):
      if (factors.count(unique) % 2) != 0: return False
    return True

  def get_gcd(self, relation):
    z_pfactrs = reduce(lambda x, y: x*y, set(relation["z"])) 
    zn_pfactrs = reduce(lambda x, y: x*y, set(relation["zn"])) 
    return (gcd((zn_pfactrs - z_pfactrs), self.n), gcd((zn_pfactrs + z_pfactrs), self.n))

  def pfactors(self, given):
    pfactors = []
    for i in range(2, given):
      while given % i == 0:
        pfactors.append(i)
        given //= i
    if given > 1: pfactors.append(given)
    return pfactors

  def __b_smooth(self, pfactr):
   return max(pfactr) in self.factor_base

  def __factors(self, gcd):
    return gcd[0] * gcd[1] == self.n

if __name__ == "__main__":
      sieve = Sieve(63, 11, [2, 3, 5, 7])
      sieve.get_factors()
