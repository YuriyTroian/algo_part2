import unittest
from red_black_priority_queue import PriorityTree

class TestPriorityTree(unittest.TestCase):
    def setUp(self):
        self.pq = PriorityTree()
        self.pq.insert("Task A", 3)
        self.pq.insert("Task B", 1)
        self.pq.insert("Task Q", 1)
        self.pq.insert("Task C", 4)
        self.pq.insert("Task D", 2)

    def test_view_queue_before_delete(self):
        queue_before = self.pq.view_queue()
        test_before = [('root.left.left', 'Task Q', 1), ('root.left', 'Task B', 1),
                       ('root.left.right', 'Task D', 2), ('root', 'Task A', 3), ('root.right', 'Task C', 4)]
        self.assertEqual(queue_before, test_before)

    def test_max_priority_oper(self):
        max_task = self.pq.max_priority_oper()
        self.assertEqual(max_task, "Task Q")


if __name__ == "__main__":
    unittest.main()
