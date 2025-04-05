class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority
        self.left = None
        self.right = None


class PriorityTree:
    def __init__(self):
        self.root = None

    def _insert(self, root, value, priority):
        if root is None:
            return Node(value, priority)

        if priority <= root.priority:
            root.left = self._insert(root.left, value, priority)
        else:
            root.right = self._insert(root.right, value, priority)

        return root

    def insert(self, value, priority):
        self.root = self._insert(self.root, value, priority)

    def _find_max(self, root):
        if root is None or root.left is None:
            return root
        return self._find_max(root.left)

    def _delete_max(self, root):
        if root is None:
            return None
        if root.left is None:
            return root.right
        root.left = self._delete_max(root.left)
        return root

    def max_priority_oper(self):
        if self.root is None:
            return None
        max_node = self._find_max(self.root)
        self.root = self._delete_max(self.root)
        return max_node.value if max_node else None

    def view_queue(self):
        elements = []
        self._collect_elements(self.root, elements, "root")
        return elements

    def _collect_elements(self, root, elements, position):
        if root is not None:
            self._collect_elements(root.left, elements, position + ".left")
            elements.append((position, root.value, root.priority))
            self._collect_elements(root.right, elements, position + ".right")

# pq = PriorityTree()
# pq.insert("Task A", 3)
# pq.insert("Task B", 1)
# pq.insert("Task Q", 1)
# pq.insert("Task C", 4)
# pq.insert("Task D", 2)
#
#
# print("Вся черга:", pq.view_queue())
# print("-----------------------------------")
# print("Максимальний пріоритет:", pq.max_priority_oper())
# print("-----------------------------------")
# print("Вся черга:", pq.view_queue())










