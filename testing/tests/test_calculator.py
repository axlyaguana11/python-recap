import unittest
from testing.src.calculator import suma, substract

class CalculatorTest(unittest.TestCase):
    def test_suma(self):
        assert suma(3, 3) == 6

    def test_substract(self):
        assert substract(7, 5) == 2

