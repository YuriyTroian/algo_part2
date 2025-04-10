import unittest
from red_black_priority_queue import PriorityRBTree

class TestPriorityRBTree(unittest.TestCase):
    def setUp(self):
        self.tree = PriorityRBTree()
        self.tree.insert("Task A", 3)
        self.tree.insert("Task B", 1)
        self.tree.insert("Task C", 4)
        self.tree.insert("Task D", 2)

    def test_view_queue_before_delete(self):
        queue_before = self.tree.view_queue()
        test_before = [('root.left', 'Task B', 1, 'BLACK'), ('root.left.right', 'Task D', 2, 'RED'),
                       ('root', 'Task A', 3, 'BLACK'), ('root.right', 'Task C', 4, 'BLACK')]
        self.assertEqual(queue_before, test_before)

    def test_max_priority_oper(self):
        max_task = self.tree.max_priority_oper()
        self.assertEqual(max_task, "Task B")


if __name__ == "__main__":
    unittest.main()
