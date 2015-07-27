from nose.tools import * 

from rational_sieve import Sieve

class TestRationalSieve():

  def setUp(self):
    self.sieve = Sieve()

  def test_rational_sieve_finds_prime_factors_for_non_prime(self):
    prime_factors = self.sieve.pfactor(9)
    assert_equals(2, prime_factors.count(3))

  def test_rational_sieve_finds_prime_factors_for_prime(self):
    prime_factors = self.sieve.pfactor(17)
    assert_equals(1, prime_factors.count(17))
