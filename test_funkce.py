from unittest import TestCase
from funkce import losuj_sportku


class TestFunkce(TestCase):

    def test_losuj_sportku(self):
        pocet_cisel = 6
        cisla = losuj_sportku(pocet_cisel=pocet_cisel)
        cisla_unique = set(cisla)
        actual_len = [len(cisla), len(cisla_unique)]
        expected = [pocet_cisel, pocet_cisel]
        self.assertEqual(actual_len, expected)
