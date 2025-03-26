import unittest
from lab3 import binary_tree_diameter
from lab3 import BinaryTree


class TestBinaryTreeDiameter(unittest.TestCase):
    def test_example_tree(self):
        root = BinaryTree(1)
        root.left = BinaryTree(3)
        root.right = BinaryTree(2)
        root.left.left = BinaryTree(7)
        root.left.right = BinaryTree(4)
        root.left.left.left = BinaryTree(8)
        root.left.right.right = BinaryTree(5)
        root.left.left.left.left = BinaryTree(9)
        root.left.right.right.right = BinaryTree(6)

        self.assertEqual(binary_tree_diameter(root), 6)


if __name__ == "__main__":
    unittest.main()
