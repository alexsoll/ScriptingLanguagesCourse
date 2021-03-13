import unittest
from Polynomial.polynomial import Polynomial


class TestPolynomialMethods(unittest.TestCase):
    def test_emtpy_args_constructor(self):
        self.assertRaises(TypeError, Polynomial)

    def test_emtpy_list_constructor(self):
        self.assertRaises(ValueError, Polynomial, [])

    def test_emtpy_tuple_constructor(self):
        self.assertRaises(ValueError, Polynomial, ())

    def test_incorrect_types_constructor(self):
        self.assertRaises(TypeError, Polynomial, 1.0)

    def test_incorrect_lists_elements_constructor(self):
        self.assertRaises(TypeError, Polynomial, ["1", "2"])


if __name__ == '__main__':
    unittest.main()
