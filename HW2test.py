import unittest
import sys
from io import StringIO
from HW2code import main

class TestLongestPath(unittest.TestCase):
    def setUp(self):
        self.input_file1 = "inSample1.txt"
        self.input_file2 = "inSample2.txt"
        self.input_file3 = "inLarge1.txt"
        self.input_file4 = "inLarge2.txt"

    def test_find_longest_path_1(self):
        # Capture the output of the main function
        sys.stdout = StringIO()
        main(self.input_file1)
        output = sys.stdout.getvalue().strip()

        # Check the output
        self.assertEqual(output, "longest path: 20\nnumber of longest paths: 3")

    def test_find_longest_path_2(self):
        # Capture the output of the main function
        sys.stdout = StringIO()
        main(self.input_file2)
        output = sys.stdout.getvalue().strip()

        # Check the output
        self.assertEqual(output, "longest path: 6\nnumber of longest paths: 8")

    def test_find_longest_path_3(self):
        # Capture the output of the main function
        sys.stdout = StringIO()
        main(self.input_file3)
        output = sys.stdout.getvalue().strip()

        # Check the output
        self.assertEqual(output, "longest path: 29\nnumber of longest paths: 268435456")

    def test_find_longest_path_4(self):
        # Capture the output of the main function
        sys.stdout = StringIO()
        main(self.input_file4)
        output = sys.stdout.getvalue().strip()

        # Check the output
        self.assertEqual(output, "longest path: 19\nnumber of longest paths: 262144")

if __name__ == "__main__":
    unittest.main()
