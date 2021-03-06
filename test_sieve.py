from nose.tools import * 

from rational_sieve import Sieve

class TestRationalSieve():

  def setUp(self):
    self.n = 187
    self.bound = 11
    self.factor_base = [2, 3, 5, 7, 11]
    self.sieve = Sieve(self.n, self.bound, self.factor_base)

  def test_finds_prime_factors_for_non_primes(self):
    prime_factors = self.sieve.pfactors(9)
    assert_equals(2, prime_factors.count(3))

  def test_finds_prime_factors_for_primes(self):
    prime_factors = self.sieve.pfactors(17)
    assert_equals(1, prime_factors.count(17))

  def test_builds_a_list_of_b_smooth_numbers(self):
    relations = self.sieve.build_relations()
    first = relations[0]
    max_pfactor = max(first["z"] + first["zn"])
    assert_true(max_pfactor in self.factor_base)

  def test_returns_false_for_non_even_exponents(self):
    pfactors = [2, 3, 3, 5]
    assert_false(self.sieve.even(pfactors))

  def test_returns_true_for_even_exponents(self):
    pfactors = [2, 2, 3, 3]
    assert_true(self.sieve.even(pfactors))

  def test_builds_greatest_common_divisor_with_n(self):
    relation = {"z": [3, 3], "zn": [2, 2, 7, 7]}
    gcd = self.sieve.get_gcd(relation)
    assert_equals(self.n, (gcd[0] * gcd[1]))
