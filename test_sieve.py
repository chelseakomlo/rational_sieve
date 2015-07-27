from nose.tools import * 

from rational_sieve import Sieve

class TestRationalSieve():

  def setUp(self):
    self.n = 55
    self.bound = 11
    self.factor_base = [2, 3, 5, 7, 11]
    self.sieve = Sieve(self.n, self.bound, self.factor_base)

  def test_rational_sieve_finds_prime_factors_for_non_prime(self):
    prime_factors = self.sieve.pfactor(9)
    assert_equals(2, prime_factors.count(3))

  def test_rational_sieve_finds_prime_factors_for_prime(self):
    prime_factors = self.sieve.pfactor(17)
    assert_equals(1, prime_factors.count(17))

  def test_rational_sieve_builds_a_list_of_b_smooth_numbers(self):
    self.sieve.build_b_smooth()
    first = self.sieve.relations[0]
    max_pfactor = max(first["z"] + first["zn"])
    assert_true(max_pfactor in self.factor_base)
    
