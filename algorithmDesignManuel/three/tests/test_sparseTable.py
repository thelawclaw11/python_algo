import unittest

from algorithmDesignManuel.three.SparseTable import SparseTable
from algorithmDesignManuel.three.partial_sum import PartialSum


class TestPartialSum(unittest.TestCase):

    def test_1(self):
        array = [4, 2, 3, 7, 1, 5, 3, 3, 9, 6, 7, -1, 4]
        st = SparseTable(array)

