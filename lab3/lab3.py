class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def binary_tree_diameter(tree: BinaryTree) -> int:
    max_diameter = [0]

    def depth(node: BinaryTree) -> int:
        if not node:
            return 0

        left_depth = depth(node.left)
        right_depth = depth(node.right)

        max_diameter[0] = max(max_diameter[0], left_depth + right_depth)

        return 1 + max(left_depth, right_depth)

    depth(tree)
    return max_diameter[0]



# root = BinaryTree(1)
# root.left = BinaryTree(3)
# root.right = BinaryTree(2)
# root.left.left = BinaryTree(7)
# root.left.right = BinaryTree(4)
# root.left.left.left = BinaryTree(8)
# root.left.right.right = BinaryTree(5)
# root.left.left.left.left = BinaryTree(9)
# root.left.right.right.right = BinaryTree(6)
#
#
#
#
# print(binary_tree_diameter(root))

