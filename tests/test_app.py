"""Unit tests for expression parsing and Flask routes in app.py."""

import unittest

from app import app, calculate


class TestCalculate(unittest.TestCase):
    """Exercise the parser and dispatcher used by the web endpoint."""

    def test_calculate_addition_expression(self):
        """A simple addition expression should be evaluated correctly."""
        self.assertEqual(calculate("1+2"), 3.0)

    def test_calculate_subtraction_expression(self):
        """Subtraction expressions should preserve left-to-right operand order."""
        self.assertEqual(calculate("5-2"), 3.0)

    def test_calculate_multiplication_expression(self):
        """Multiplication expressions should compute a product, not a power."""
        self.assertEqual(calculate("3*4"), 12.0)

    def test_calculate_division_expression(self):
        """Division expressions should return a non-truncated float when needed."""
        self.assertEqual(calculate("7/2"), 3.5)

    def test_calculate_rejects_multiple_operators(self):
        """Parser should reject chained expressions beyond one binary operator."""
        with self.assertRaises(ValueError):
            calculate("1+2+3")

    def test_calculate_rejects_non_numeric_operands(self):
        """Parser should reject expressions that contain non-numeric operands."""
        with self.assertRaises(ValueError):
            calculate("abc+2")


class TestIndexRoute(unittest.TestCase):
    """Validate integration behavior of the Flask root endpoint."""

    def setUp(self):
        """Create a fresh Flask test client for each test."""
        app.testing = True
        self.client = app.test_client()

    def test_index_get_returns_200(self):
        """GET / should return a successful response."""
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_index_post_shows_computed_result(self):
        """POST / should render the computed result into the display input."""
        response = self.client.post("/", data={"display": "5-2"})

        self.assertEqual(response.status_code, 200)
        # The template stores the result in the input value attribute.
        self.assertIn('value="3.0"', response.get_data(as_text=True))


if __name__ == "__main__":
    unittest.main()