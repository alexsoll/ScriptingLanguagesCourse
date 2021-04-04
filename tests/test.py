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

    def test_polynomial_to_str(self):
        params = [
            [1, -1, 1],
            [-1, 2, 0],
            [5],
            [1, 0, 1],
            [1, 0, 1, 1],
            [1, 0, -1, 1],
            [0, 1]
        ]

        results = [
            "x^2-x+1", "-x^2+2x", "5", "x^2+1", "x^3+x+1", "x^3-x+1", "1"
        ]
        for i, param in enumerate(params):
            self.assertEqual(Polynomial(param).__str__(), results[i], f"Incorrect comparison for {Polynomial(param).__repr__()}")

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

    def test_compare(self):
        # Initialization
        p1 = Polynomial([1, 2, 3])
        p2 = Polynomial([1, 2])

        # Test 1
        self.assertNotEqual(p1, p2)

        p2.coeffs.append(3)

        # Test 2
        self.assertEqual(p1, p2)

        p2.coeffs = [0, 1, 2, 3]

        # Test 3
        self.assertEqual(p1, p2)

        p2.coeffs = [1, 2, 3, 0]

        # Test 4
        self.assertNotEqual(p1, p2)

    def test_addition_two_polynomials(self):
        # Initialization
        p1 = Polynomial([1, 2, 3])
        p2 = Polynomial([1, 2])

        # Addition
        res1 = p1 + p2
        res2 = p2 + p1

        self.assertEqual(res1.coeffs, [1, 3, 5])
        self.assertEqual(res2.coeffs, [1, 3, 5])

    def test_addition_polynomial_with_int(self):
        # Initialization
        p = Polynomial([1, 2, 3])
        i = 5

        # Addition
        res1 = p + i
        res2 = i + p

        self.assertEqual(res1.coeffs, [1, 2, 8])
        self.assertEqual(res2.coeffs, [1, 2, 8])

    def test_sub_two_polynomial(self):
        # Initialization
        p1 = Polynomial([1, 2, 3])
        p2 = Polynomial([2, 2])
        p3 = Polynomial([1, 2, 1])

        # Subtraction
        res1 = p1 - p2
        res2 = p2 - p1

        # Test 1
        self.assertEqual(res1.coeffs, [1, 0, 1])
        self.assertEqual(res2.coeffs, [-1, 0, -1])

        # Subtraction
        res1 = p1 - p3
        res2 = p3 - p1

        # Test 2
        self.assertEqual(res1.coeffs, [2])
        self.assertEqual(res2.coeffs, [-2])

    def test_sub_polynomial_with_int(self):
        # Initialization
        p1 = Polynomial([1, 2, 3])
        i = 3

        # Subtraction
        res1 = p1 - i
        res2 = i - p1

        self.assertEqual(res1.coeffs, [1, 2, 0])
        self.assertEqual(res2.coeffs, [-1, -2, 0])

    def test_mul_two_polynomialt(self):
        # Initialization
        p1 = Polynomial([1, 1, 3])
        p2 = Polynomial([2, 2])
        p3 = Polynomial([1, -1, 1])

        # Multiplication
        res1 = p1 * p2
        res2 = p2 * p1

        # Test 1
        self.assertEqual(res1.coeffs, [2, 4, 8, 6])
        self.assertEqual(res2.coeffs, [2, 4, 8, 6])

        # Multiplication
        res1 = p1 * p3
        res2 = p3 * p1

        # Test 2
        self.assertEqual(res1.coeffs, [1, 0, 3, -2, 3])
        self.assertEqual(res2.coeffs, [1, 0, 3, -2, 3])

    def test_mul_polynomial_with_int(self):
        # Initialization
        p1 = Polynomial([1, 1, 3])
        i = 2

        # Multiplication
        res1 = p1 * i
        res2 = i * p1

        self.assertEqual(res1.coeffs, [2, 2, 6])
        self.assertEqual(res2.coeffs, [2, 2, 6])

    def test_raise_add_with_incorrect_arg(self):
        # Initialization
        p = Polynomial([1, 1, 3])
        fs = [2.0, "2.0", [2.0], (2.0)]
        
        for f in fs:
            with self.assertRaises(TypeError):
                p + f
        for f in fs:
            with self.assertRaises(TypeError):
                f + p

    def test_raise_sub_with_incorrect_arg(self):
        # Initialization
        p = Polynomial([1, 1, 3])
        fs = [2.0, "2.0", [2.0], (2.0)]
        
        for f in fs:
            with self.assertRaises(TypeError):
                p - f
        for f in fs:
            with self.assertRaises(TypeError):
                f - p

    def test_raise_mul_with_incorrect_arg(self):
        # Initialization
        p = Polynomial([1, 1, 3])
        fs = [2.0, "2.0", [2.0], (2.0)]
        
        for f in fs:
            with self.assertRaises(TypeError):
                p * f
        for f in fs:
            with self.assertRaises(TypeError):
                f * p


if __name__ == '__main__':
    unittest.main()
