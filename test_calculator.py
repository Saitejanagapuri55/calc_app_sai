import unittest
from calculator import Calculator
from faker import Faker

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()
        self.fake = Faker()

    def test_add(self):
        a = self.fake.random_number(digits=2)
        b = self.fake.random_number(digits=2)
        result = self.calc.add(a, b)
        self.assertEqual(result, a + b)

    def test_subtract(self):
        a = self.fake.random_number(digits=2)
        b = self.fake.random_number(digits=2)
        result = self.calc.subtract(a, b)
        self.assertEqual(result, a - b)

    def test_multiply(self):
        a = self.fake.random_number(digits=2)
        b = self.fake.random_number(digits=2)
        result = self.calc.multiply(a, b)
        self.assertEqual(result, a * b)

    def test_divide(self):
        a = self.fake.random_number(digits=2)
        b = self.fake.random_number(digits=2, fix_len=True) + 1  # Ensure no divide by 0
        result = self.calc.divide(a, b)
        self.assertEqual(result, a / b)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)

if __name__ == '__main__':
    unittest.main()
