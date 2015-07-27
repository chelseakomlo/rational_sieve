
class Sieve():

  def __init__(self, n, bound, factor_base):
    self.n = n
    self.bound = bound
    self.factor_base = factor_base

  def pfactor(self, given):
    pfactors = []
    for i in range(2, given):
      while given % i == 0:
        pfactors.append(i)
        given //= i
    if given > 1: pfactors.append(given)
    return pfactors

  def build_b_smooth(self): 
    self.relations = []
    for i in range(2, self.n): 
      if self._b_smooth(i): 
        relation = {"z": self.pfactor(i), "zn": self.pfactor(i+self.n)}
        self.relations.append(relation)

  def _b_smooth(self, given):
   factors = self.pfactor(given) + self.pfactor(given + self.n) 
   return max(factors) in self.factor_base
