import unittest
from math import pi

from format_price import format_price


class TestPriceFormatter(unittest.TestCase):
    def test_format_int_price(self):
        self.assertEqual(format_price(0), "0")
        self.assertEqual(format_price(1), "1")
        self.assertEqual(format_price(123), "123")
        self.assertEqual(format_price(2018), "2 018")
        self.assertEqual(format_price(30000), "30 000")
        self.assertEqual(format_price(1000000), "1 000 000")
        self.assertEqual(format_price(-1000), "-1 000")

    def test_format_float_price(self):
        self.assertEqual(format_price(0.0), "0")
        self.assertEqual(format_price(1000.0000), "1 000")
        self.assertEqual(format_price(100000.325235), "100 000.325235")
        self.assertEqual(format_price(-77.234), "-77.234")
        self.assertEqual(format_price(5.1700000), "5.17")
        self.assertEqual(format_price(pi), str(pi))

    def test_format_str_price(self):
        self.assertEqual(format_price("123"), "123")
        self.assertEqual(format_price("1000.124500"), "1 000.1245")
        self.assertEqual(format_price("-1230000"), "-1 230 000")
        self.assertIsNone(format_price("a12444"))
        self.assertIsNone(format_price("324.444a"))
        self.assertIsNone(format_price("123.6ggg7"))
        self.assertIsNone(format_price("ABC"))
        self.assertIsNone(format_price("123.000.555"))

    def test_format_price_other(self):
        self.assertIsNone(format_price(None))
        self.assertIsNone(format_price(object()))


if __name__ == "__main__":
    unittest.main()
