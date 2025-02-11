import unittest
from add_numbers import add_two_numbers

class TestAddNumbers(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertAlmostEqual(add_two_numbers(2, 3), 5.0)
        
    def test_negative_numbers(self):
        self.assertAlmostEqual(add_two_numbers(-1, 1), 0.0)
        
    def test_decimal_numbers(self):
        self.assertAlmostEqual(add_two_numbers(2.5, 3.7), 6.2)

if __name__ == '__main__':
    unittest.main()