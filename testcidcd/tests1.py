import unittest

from prime import is_prime

class Tests(unittest.TestCase):
  def test_1(self):
    self.assertFalse(is_prime(1))

if __name__ == "__main__":
  unittest.main()