#!/usr/bin/env python3

import sys
import unittest

import general as G

class TestStructures(unittest.TestCase):
    def test_dedupe(self):
        self.assertEqual(G.dedupe([]), [])
        self.assertEqual(G.dedupe([0]), [0])
        self.assertEqual(G.dedupe([0, 0]), [0])
        self.assertEqual(G.dedupe([0, 1, 2, 1]), [0, 1, 2])

if __name__ == '__main__':
    unittest.main()

