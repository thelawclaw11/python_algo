import unittest
from contains_triangle import contains_triangle


class TestContainsTriangle(unittest.TestCase):
    def test_alpha(self):
        graph = [
            [1, 2],
            [0, 2],
            [0, 1]
        ]
        self.assertTrue(contains_triangle(graph))

    def test_beta(self):
        graph = [
            [1,2],
            [0,3],
            [0,3],
            [1,2]
        ]
        self.assertFalse(contains_triangle(graph))

    def test_gamma(self):
        graph = [
            [1,2],
            [0,3,4],
            [0,5,6],
            [1],
            [1],
            [2],
            [2]
        ]
        self.assertFalse(contains_triangle(graph))

    def test_delta(self):
        graph = [
            [1,2],
            [0,3],
            [0,3,4,5],
            [1,2],
            [2,5],
            [2,4]
        ]

        self.assertTrue(contains_triangle(graph))
