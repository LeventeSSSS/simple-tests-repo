import unittest
from calculator import Calculator

class TestCalculatorIntegration(unittest.TestCase):
    
    def setUp(self):
        """This method will run before each test"""
        self.calculator = Calculator()

    def test_add_and_subtract(self):
        """Test a sequence of add and subtract operations"""
        result = self.calculator.add(5, 3)  # 5 + 3 = 8
        result = self.calculator.subtract(result, 2)  # 8 - 2 = 6
        self.assertEqual(result, 6)

    def test_subtract_and_add(self):
        """Test a sequence of subtract and add operations"""
        result = self.calculator.subtract(10, 5)  # 10 - 5 = 5
        result = self.calculator.add(result, 7)  # 5 + 7 = 12
        self.assertEqual(result, 12)

    def test_chained_operations(self):
        """Test multiple chained operations"""
        result = self.calculator.add(2, 3)  # 2 + 3 = 5
        result = self.calculator.subtract(result, 1)  # 5 - 1 = 4
        result = self.calculator.add(result, 10)  # 4 + 10 = 14
        self.assertEqual(result, 14)

if __name__ == '__main__':
    unittest.main()
