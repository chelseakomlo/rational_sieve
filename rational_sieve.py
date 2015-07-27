n = 187
bound = 11
factor_base = [2, 3, 5, 7, 11]



class Sieve():

  def pfactor(self, given):
    pfactors = []
    for factor in factor_base:
      while given % factor == 0:
        pfactors.append(factor)
        given //= factor
    if given > 0: pfactors.append(given)

    return pfactors

