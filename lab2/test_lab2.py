import unittest
from lab2 import banana_and_jackie

class TestBananaAndJackie(unittest.TestCase):
    def test_banana_and_jackie(self):
        self.assertEqual(banana_and_jackie([3,6,7,11], 8), 4)
        self.assertEqual(banana_and_jackie([30,11,23,4,20], 5), 30)
        self.assertEqual(banana_and_jackie([30,11,23,4,20], 6), 23)



