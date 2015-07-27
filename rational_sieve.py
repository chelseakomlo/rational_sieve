
class Sieve():

  def __init__(self, n, bound, factor_base):
    self.n = n
    self.bound = bound
    self.factor_base = factor_base
    self.cache = {}

  def build_b_smooth(self): 
    self.relations = []
    for i in range(2, self.n): 
      if self._b_smooth(i): 
        relation = {"z": self.pfactors(i), "zn": self.pfactors(i+self.n)}
        self.relations.append(relation)

  def even(self, factors):
    for unique in set(factors):
      if (factors.count(unique) % 2) != 0: return False
    return True

  def pfactors(self, given):
    if self.cache.get(given): return self.cache[given]
    return self._build_pfactors(given)

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

