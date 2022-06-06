import unittest

from algorithmDesignManuel.three.partial_sum import PartialSum


class TestPartialSum(unittest.TestCase):

    def test_1(self):
        array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        ps = PartialSum(array)

        self.assertEqual(ps.get_partial_sum(0), 1)
        self.assertEqual(ps.get_partial_sum(4), 15)
        self.assertEqual(ps.get_partial_sum(9), 55)

        ps.add(0, 1)

        self.assertEqual(ps.get_partial_sum(0), 2)
        self.assertEqual(ps.get_partial_sum(1), 4)




