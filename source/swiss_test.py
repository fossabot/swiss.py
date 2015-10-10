#!/usr/bin/env python3

import swiss.structures as SS
import unittest

class TestStructures(unittest.TestCase):
    def test_dedupe(self):
        self.assertEqual(SS.dedupe([]), [])
        self.assertEqual(SS.dedupe([0]), [0])
        self.assertEqual(SS.dedupe([0, 0]), [0])
        self.assertEqual(SS.dedupe([0, 1, 2, 1]), [0, 1, 2])

if __name__ == '__main__':
    unittest.main()

