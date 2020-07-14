import unittest
from kata import sum_numbers_in


class StringCalculatorTests(unittest.TestCase):
    def test_none_and_empty_compute_as_zero(self):
        self.assertEqual(sum_numbers_in(""), 0)
        self.assertEqual(sum_numbers_in(None), 0)

    def test_numbers_in_expression_are_converted_to_integers(self):
        self.assertEqual(sum_numbers_in("8"), 8)

    def test_numbers_in_expression_are_separated_by_commas(self):
        self.assertEqual(sum_numbers_in("1,4"), 5)
        self.assertEqual(sum_numbers_in("1,4,1"), 6)

    def test_non_numeric_symbols_are_evaluated_as_zeros(self):
        self.assertEqual(sum_numbers_in("10,a"), 10)
        self.assertEqual(sum_numbers_in("a"), 0)
        self.assertEqual(sum_numbers_in("1a,2"), 2)

    def test_numbers_in_expression_are_separated_by_configured_separator(self):
        self.assertEqual(sum_numbers_in("//#/3#2"), 5)
        self.assertEqual(sum_numbers_in("//#/3,2"), 0)
        self.assertEqual(sum_numbers_in("//%/1%2%3"), 6)
        self.assertEqual(sum_numbers_in("//#@€/3#@€2#@€5"), 10)
        self.assertEqual(sum_numbers_in("//#@€/3#@€2#@€2,5"), 5)

