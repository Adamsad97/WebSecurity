import unittest

from calculator.calculator import add, divide, multiply, subtract, power, root, percent


class TestCalculator(unittest.TestCase):
    def test_power(self):
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(9, 0.5), 3)
        self.assertEqual(power(-2, 2), 4)

    def test_root(self):
        self.assertEqual(root(9, 2), 3)
        self.assertEqual(root(27, 3), 3)
        self.assertAlmostEqual(root(16, 4), 2)
        with self.assertRaises(ValueError):
            root(8, 0)

    def test_percent(self):
        self.assertEqual(percent(200, 10), 20)
        self.assertEqual(percent(50, 50), 25)
        self.assertEqual(percent(100, 0), 0)

    def test_add(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(subtract(1, 2), -1)
        self.assertEqual(subtract(-1, 1), -2)
        self.assertEqual(subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(multiply(1, 2), 2)
        self.assertEqual(multiply(-1, 1), -1)
        self.assertEqual(multiply(-1, -1), 1)

    def test_divide(self):
        self.assertEqual(divide(1, 2), 0.5)
        self.assertEqual(divide(-1, 1), -1)
        self.assertEqual(divide(-1, -1), 1)
        self.assertEqual(divide(0, 5), 0)
        with self.assertRaises(ValueError):
            divide(1, 0)

if __name__ == '__main__':
    unittest.main()
