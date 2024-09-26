import unittest
from main import add, sub, multiply, divide, check_even, modulo


class TestMath(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 5), 7)
        self.assertNotEqual(add(3, 7), 9)

    def test_subtract(self):
        self.assertEqual(sub(7, 4), 3)
        self.assertNotEqual(sub(4, 2), 1)

    def test_multiply(self):
        self.assertNotEqual(multiply(2, 5), 12)
        self.assertEqual(multiply(3, 6), 18)

    def test_divide(self):
        self.assertNotEqual(divide(4, 2), 3)
        self.assertEqual(divide(20, 5), 4)

    def test_divide_by_zero(self):
        self.assertRaises(ValueError, divide, 6, 0)


class TestEven(unittest.TestCase):
    def test_check_even(self):
        self.assertTrue(check_even(2))
        self.assertTrue(not check_even(7))
        self.assertFalse(check_even(23))


class TestModulo(unittest.TestCase):
    def test_modulo(self):
        self.assertEqual(modulo(5, 2), 1)
        self.assertEqual(modulo(234, 5), 4)
        self.assertNotEqual(modulo(10, 3), 2)

    def test_modulo_by_zero(self):
        self.assertRaises(ValueError, modulo, 5, 0)


if __name__ == '__main__':
    unittest.main()
