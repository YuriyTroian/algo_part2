import unittest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from wchain import longest_word_chain

class TestWordChain(unittest.TestCase):

    def test_example_case(self):
        with open(os.path.join(os.path.dirname(__file__), '..', 'src', 'wchain.in'), 'r') as fin:
            n = int(fin.readline())
            words = [fin.readline().strip() for _ in range(n)]

        result = longest_word_chain(words)

        with open(os.path.join(os.path.dirname(__file__), '..', 'src', 'wchain.out'), 'w') as fout:
            fout.write(str(result) + '\n')


        self.assertEqual(result, 6)





if __name__ == '__main__':
    unittest.main()
