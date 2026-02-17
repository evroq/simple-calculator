import unittest
import sys
import os

# Добавляем путь к родительской папке для импорта calculator
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import calculator

class TestCalculator(unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(calculator.add(2, 3), 5)
        self.assertEqual(calculator.add(-1, 1), 0)
        self.assertEqual(calculator.add(0, 0), 0)
    
    def test_subtract(self):
        self.assertEqual(calculator.subtract(5, 3), 2)
        self.assertEqual(calculator.subtract(1, 5), -4)
        self.assertEqual(calculator.subtract(0, 0), 0)
    
    def test_multiply(self):
        self.assertEqual(calculator.multiply(2, 3), 6)
        self.assertEqual(calculator.multiply(-2, 3), -6)
        self.assertEqual(calculator.multiply(0, 5), 0)
    
    def test_divide(self):
        self.assertEqual(calculator.divide(6, 3), 2)
        self.assertEqual(calculator.divide(5, 2), 2.5)
        with self.assertRaises(ValueError):
            calculator.divide(10, 0)
    
    def test_square_root(self):
        self.assertEqual(calculator.square_root(9), 3)
        self.assertEqual(calculator.square_root(0), 0)
        self.assertEqual(calculator.square_root(2), 1.4142135623730951)
        self.assertEqual(calculator.square_root(-1), "Ошибка: нельзя извлечь корень из отрицательного числа")

if __name__ == '__main__':
    unittest.main()