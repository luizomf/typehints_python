"""Offline behavioral checks for the isolated arithmetic exercise."""

import unittest

from mean import arithmetic_mean


class MeanTests(unittest.TestCase):
    def test_multiple_values(self) -> None:
        self.assertEqual(arithmetic_mean((2.0, 4.0, 6.0)), 4.0)

    def test_single_value(self) -> None:
        self.assertEqual(arithmetic_mean((7.0,)), 7.0)

    def test_empty_values(self) -> None:
        with self.assertRaises(ValueError):
            arithmetic_mean(())


if __name__ == "__main__":
    unittest.main()
