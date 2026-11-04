import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    # Add the following test methods to the TestCalculator class:
    # add: 2 test
    def test_add_negative_numbers(self):
        self.assertEqual(self.calc.add(-3, -4), -7)

    def test_add_with_zero(self):
        self.assertEqual(self.calc.add(0, 5), 5)

    # subtract: 2 test
    def test_subtract_positive_result(self):
        self.assertEqual(self.calc.subtract(5, 2), 3)

    def test_subtract_negative_result(self):
        self.assertEqual(self.calc.subtract(2, 5), -3)

    # multiply: 2 test
    def test_multiply_positive_numbers(self):
        self.assertEqual(self.calc.multiply(3, 7), 21)

    def test_multiply_negative_multiplier(self):
        self.assertEqual(self.calc.multiply(3, -2), -6)

    # divide: 2 test
    def test_divide_positive_numbers(self):
        self.assertEqual(self.calc.divide(5, 2), 2)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(5, 0)

    # modulo: 2 test
    def test_modulo_positive_numbers(self):
        
        self.assertEqual(self.calc.modulo(5, 2), 1)

    def test_modulo_negative_dividend(self):
        self.assertEqual(self.calc.modulo(-5, 3), 1)

if __name__ == '__main__':
    unittest.main()