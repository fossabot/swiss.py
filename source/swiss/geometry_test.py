#!/usr/bin/env python3

import geometry as G
import unittest

class TestStructures(unittest.TestCase):
    def test_calculate_change(self):
        self.assertEqual(G.calculate_change((1, 1), (1, 1)), (0, 0))

    def test_calculate_distance(self):
        self.fail()

    def test_calculate_slope(self):
        self.fail()

    def test_is_in_circle(self):
        self.fail()

    def test_is_in_range(self):
        self.fail()

    def test_rotate_point(self):
        self.fail()

    def test_sort_clockwis(self):
        self.fail()

    def test_translate_point(self):
        self.fail()

if __name__ == '__main__':
    unittest.main()

