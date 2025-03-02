import unittest
from lab1 import search_k
array = [15, 7, 22, 9, 36, 2, 42, 18]
class TestLab(unittest.TestCase):
    def test_search_k(self):
        self.assertEqual(search_k(3, array), "element = 22, index = 2")

if __name__ == '__main__':
    unittest.main()
