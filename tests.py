import unittest

from format_price import format_price


class PriceFormatterTestCase(unittest.TestCase):
    def test_positive_integer_price(self):
        self.assertEqual(format_price(1), "1")
        self.assertEqual(format_price(123), "123")
        self.assertEqual(format_price(2018), "2 018")
        self.assertEqual(format_price(30000), "30 000")
        self.assertEqual(format_price(1000000), "1 000 000")
        self.assertEqual(format_price("100"), "100")
        self.assertEqual(format_price("1000"), "1 000")

    def test_negative_integer_price(self):
        self.assertEqual(format_price(-1000), "-1 000")
        self.assertEqual(format_price("-1230000"), "-1 230 000")

    def test_zero_price(self):
        self.assertEqual(format_price(0), "0")
        self.assertEqual(format_price(0.0), "0")
        self.assertEqual(format_price("-0"), "0")
        self.assertEqual(format_price("-0.0"), "0")

    def test_positive_float_price(self):
        self.assertEqual(format_price(1000.0000), "1 000")
        self.assertEqual(format_price(100000.325235), "100 000.33")
        self.assertEqual(format_price(5.1700000), "5.17")
        self.assertEqual(format_price("1000.124500"), "1 000.12")

    def test_negative_float_price(self):
        self.assertEqual(format_price(-77.234), "-77.23")
        self.assertEqual(format_price(-1000.333), "-1 000.33")
        self.assertEqual(format_price(-10000.000), "-10 000")

    def test_incorect_price_value(self):
        self.assertIsNone(format_price("a12444"))
        self.assertIsNone(format_price("324.444a"))
        self.assertIsNone(format_price("123.6ggg7"))
        self.assertIsNone(format_price("ABC"))
        self.assertIsNone(format_price("123.000.555"))
        self.assertIsNone(format_price(None))
        self.assertIsNone(format_price(object()))
        self.assertIsNone(format_price(list()))
        self.assertIsNone(format_price(dict()))
        self.assertIsNone(format_price(tuple()))
        self.assertIsNone(format_price(set()))
        self.assertIsNone(format_price(lambda a: a))


if __name__ == "__main__":
    unittest.main()
