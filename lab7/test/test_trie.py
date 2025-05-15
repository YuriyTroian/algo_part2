import unittest
from src.trie import Trie, build_trie


class TestTrie(unittest.TestCase):
    def setUp(self):
        self.patterns = ["apple", "app", "banana", "band"]
        self.trie = build_trie(self.patterns)

    def test_insert_and_search(self):
        for word in self.patterns:
            self.assertTrue(self.trie.search(word))

    def test_search_non_existing(self):
        self.assertFalse(self.trie.search("appl"))
        self.assertFalse(self.trie.search("bananas"))

    def test_starts_with(self):
        self.assertTrue(self.trie.starts_with("app"))
        self.assertTrue(self.trie.starts_with("ban"))
        self.assertFalse(self.trie.starts_with("can"))

    def test_insert_new_word(self):
        self.trie.insert("canary")
        self.assertTrue(self.trie.search("canary"))
        self.assertTrue(self.trie.starts_with("can"))


if __name__ == "__main__":
    unittest.main()
