"""Unit tests for arithmetic helpers in operators.py."""

import unittest

from operators import add, divide, multiply, subtract


class TestOperators(unittest.TestCase):
    """Validate each arithmetic operator against expected math behavior."""

    def test_add_returns_sum(self):
        """Addition should return the sum of both operands."""
        # Baseline sanity check: this operation should pass.
        self.assertEqual(add(2, 3), 5)

    def test_subtract_returns_difference(self):
        """Subtraction should compute a - b."""
        self.assertEqual(subtract(5, 2), 3)

    def test_multiply_returns_product(self):
        """Multiplication should compute a * b."""
        self.assertEqual(multiply(3, 4), 12)

    def test_divide_returns_float_quotient(self):
        """Division should preserve fractional quotients."""
        self.assertEqual(divide(7, 2), 3.5)


if __name__ == "__main__":
    unittest.main()