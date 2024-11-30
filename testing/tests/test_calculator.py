import unittest
from testing.src.calculator import suma, substract, multiply, divide

class CalculatorTest(unittest.TestCase):
    def test_suma(self):
        assert suma(3, 3) == 6

    def test_substract(self):
        assert substract(7, 5) == 2

    def test_multiply(self):
        assert multiply(3, 5) == 15
    
    def test_divide(self):
        assert divide(25, 5) == 5

    def test_divide_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)