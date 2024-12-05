import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    
    def setUp(self):
        """This method will run before each test"""
        self.calculator = Calculator()

    def test_add(self):
        """Test the add method"""
        self.assertEqual(self.calculator.add(2, 3), 5)
        self.assertEqual(self.calculator.add(-1, 1), 0)
        self.assertEqual(self.calculator.add(0, 0), 0)

    def test_subtract(self):
        """Test the subtract method"""
        self.assertEqual(self.calculator.subtract(5, 3), 2)
        self.assertEqual(self.calculator.subtract(0, 1), -1)
        self.assertEqual(self.calculator.subtract(-1, -1), 0)

if __name__ == '__main__':
    unittest.main()
