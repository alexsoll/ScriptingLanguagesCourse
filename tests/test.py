import unittest
import traceback
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

    def test_polynomial_to_str(self):
        # Test 1
        self.assertEqual(Polynomial([1, -1, 1]).__str__(), "x^2-x+1")
        
        # Test 2
        self.assertEqual(Polynomial([-1, 2, 0]).__str__(), "-x^2+2x")

        # Test 3
        self.assertEqual(Polynomial([5]).__str__(), "5")

    def test_repr(self):
        # Test 1
        self.assertEqual(Polynomial([1, 2, 3]).__repr__(), "Polynomial([1, 2, 3])")

        # Test 2 
        self.assertEqual(Polynomial((1, 2, 3)).__repr__(), "Polynomial([1, 2, 3])")

        # Test 3
        self.assertEqual(Polynomial(1).__repr__(), "Polynomial([1])")

    def test_modification_pow_field(self):
        # Initialization
        p = Polynomial([1, 2, 3])

        # Test 1
        self.assertEqual(2, p.max_degree)

        # Coeffs field modification
        p.coeffs.append(4)

        # Test 2
        self.assertEqual(3, p.max_degree)

        # Coeffs field modification
        p.coeffs = [1, 2]

        # Test 3
        self.assertEqual(1, p.max_degree)

    def test_ability_to_change_coeffs(self):
        # Initialization
        p = Polynomial([1, 2, 3])

        # Coeffs field modification
        p.coeffs = [1, 0]

        # Test 1
        self.assertEqual([1, 0], p.coeffs)

        # Coeffs field modification
        p.coeffs.pop(1)

        # Test 2
        self.assertEqual([1], p.coeffs)


if __name__ == '__main__':
    unittest.main()
