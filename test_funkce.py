from unittest import TestCase
from funkce import losuj_sportku


class TestLosovani(TestCase):

    def test_losovani_result_length(self):
        actual = losuj_sportku()
        expected = 6
        self.assertEqual(len(actual), expected)

    def test_losovani_result_unique(self):
        actual = losuj_sportku()
        #retype to set -> remove duplicates
        actual = set(actual)
        expected = 6
        self.assertEqual(len(actual), expected)
