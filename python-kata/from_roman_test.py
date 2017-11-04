from from_roman import parse
from nose_parameterized import parameterized
import unittest

class FromRomanTestCase(unittest.TestCase):
    @parameterized.expand([
        ("I",       1),     # 1 
        ("II",      2),     # 1 + 1
        ("IV",      4),     # -1 + 5
        ("V",       5),     # 5
        ("IX",      9),     # -1 + 10
        ("XLII",    42),    # -10 + 50 + 1 + 1
        ("XCIX",    99),    # -10 + 100 - 1 + 10
        ("MMXIII",  2013)   # 1000 + 10 + 1 + 1 + 1
    ])
    def test_sequence(self, roman, latin):
        self.assertEqual(parse(roman), latin)