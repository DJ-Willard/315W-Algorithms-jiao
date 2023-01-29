import unittest
from unittest.mock import patch
import sys
from HW2code import find_longest_path

class TestFindLongestPath(unittest.TestCase):

    @patch('sys.stdin', open('inSample1.txt', 'r'))
    def test_Sample1(self):
        n, m = map(int, input().strip().split())
        edges = [tuple(map(int, line.strip().split())) for line in sys.stdin]
        longest_path, num_longest_paths = find_longest_path(n, m, edges)
        self.assertEqual(longest_path, 20)
        self.assertEqual(num_longest_paths, 3)

    @patch('sys.stdin', open('inSample2.txt', 'r'))
    def test_Sample2(self):
        n, m = map(int, input().strip().split())
        edges = [tuple(map(int, line.strip().split())) for line in sys.stdin]
        longest_path, num_longest_paths = find_longest_path(n, m, edges)
        self.assertEqual(longest_path, 6)
        self.assertEqual(num_longest_paths, 8)

    @patch('sys.stdin', open('inLarge1.txt', 'r'))
    def test_Large1(self):
        n, m = map(int, input().strip().split())
        edges = [tuple(map(int, line.strip().split())) for line in sys.stdin]
        longest_path, num_longest_paths = find_longest_path(n, m, edges)
        self.assertEqual(longest_path, 29)
        self.assertEqual(num_longest_paths, 268435456)

    @patch('sys.stdin', open('inLarge2.txt', 'r'))
    def test_Large2(self):
        n, m = map(int, input().strip().split())
        edges = [tuple(map(int, line.strip().split())) for line in sys.stdin]
        longest_path, num_longest_paths = find_longest_path(n, m, edges)
        self.assertEqual(longest_path, 19)
        self.assertEqual(num_longest_paths, 262144)

if __name__ == '__main__':
    unittest.main()
