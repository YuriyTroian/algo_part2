class RBNode:
    def __init__(self, value, priority, color="RED"):
        self.value = value
        self.priority = priority
        self.color = color
        self.left = None
        self.right = None
        self.parent = None


class PriorityRBTree:
    def __init__(self):
        self.NIL = RBNode(None, None, color="BLACK")
        self.root = self.NIL

    def insert(self, value, priority):
        new_node = RBNode(value, priority)
        new_node.left = self.NIL
        new_node.right = self.NIL
        parent = None
        current = self.root

        while current != self.NIL:
            parent = current
            if priority < current.priority:
                current = current.left
            else:
                current = current.right

        new_node.parent = parent
        if parent is None:
            self.root = new_node
        elif priority < parent.priority:
            parent.left = new_node
        else:
            parent.right = new_node

        new_node.color = "RED"
        self._fix_insert(new_node)

    def _rotate_left(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def _rotate_right(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.NIL:
            y.right.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def _fix_insert(self, z):
        while z.parent and z.parent.color == "RED":
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right
                if y.color == "RED":
                    z.parent.color = "BLACK"
                    y.color = "BLACK"
                    z.parent.parent.color = "RED"
                    z = z.parent.parent
                else:
                    if z == z.parent.right:
                        z = z.parent
                        self._rotate_left(z)
                    z.parent.color = "BLACK"
                    z.parent.parent.color = "RED"
                    self._rotate_right(z.parent.parent)
            else:
                y = z.parent.parent.left
                if y.color == "RED":
                    z.parent.color = "BLACK"
                    y.color = "BLACK"
                    z.parent.parent.color = "RED"
                    z = z.parent.parent
                else:
                    if z == z.parent.left:
                        z = z.parent
                        self._rotate_right(z)
                    z.parent.color = "BLACK"
                    z.parent.parent.color = "RED"
                    self._rotate_left(z.parent.parent)
        self.root.color = "BLACK"

    def _minimum(self, node):
        while node.left != self.NIL:
            node = node.left
        return node

    def _transplant(self, u, v):
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def _fix_delete(self, x):
        while x != self.root and x.color == "BLACK":
            if x == x.parent.left:
                sibling = x.parent.right
                if sibling.color == "RED":
                    sibling.color = "BLACK"
                    x.parent.color = "RED"
                    self._rotate_left(x.parent)
                    sibling = x.parent.right
                if sibling.left.color == "BLACK" and sibling.right.color == "BLACK":
                    sibling.color = "RED"
                    x = x.parent
                else:
                    if sibling.right.color == "BLACK":
                        sibling.left.color = "BLACK"
                        sibling.color = "RED"
                        self._rotate_right(sibling)
                        sibling = x.parent.right
                    sibling.color = x.parent.color
                    x.parent.color = "BLACK"
                    sibling.right.color = "BLACK"
                    self._rotate_left(x.parent)
                    x = self.root
            else:
                sibling = x.parent.left
                if sibling.color == "RED":
                    sibling.color = "BLACK"
                    x.parent.color = "RED"
                    self._rotate_right(x.parent)
                    sibling = x.parent.left
                if sibling.left.color == "BLACK" and sibling.right.color == "BLACK":
                    sibling.color = "RED"
                    x = x.parent
                else:
                    if sibling.left.color == "BLACK":
                        sibling.right.color = "BLACK"
                        sibling.color = "RED"
                        self._rotate_left(sibling)
                        sibling = x.parent.left
                    sibling.color = x.parent.color
                    x.parent.color = "BLACK"
                    sibling.left.color = "BLACK"
                    self._rotate_right(x.parent)
                    x = self.root
        x.color = "BLACK"

    def _delete_node(self, z):
        y = z
        y_original_color = y.color
        if z.left == self.NIL:
            x = z.right
            self._transplant(z, z.right)
        elif z.right == self.NIL:
            x = z.left
            self._transplant(z, z.left)
        else:
            y = self._minimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self._transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self._transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        if y_original_color == "BLACK":
            self._fix_delete(x)

    def max_priority_oper(self):
        if self.root == self.NIL:
            return None
        min_node = self._minimum(self.root)
        value = min_node.value
        self._delete_node(min_node)
        return value

    def _collect(self, node, res, pos="root"):
        if node != self.NIL:
            self._collect(node.left, res, pos + ".left")
            res.append((pos, node.value, node.priority, node.color))
            self._collect(node.right, res, pos + ".right")

    def view_queue(self):
        result = []
        self._collect(self.root, result)
        return result






# pq = PriorityRBTree()
# pq.insert("Task A", 3)
# pq.insert("Task B", 1)
# pq.insert("Task Q", 1)
# pq.insert("Task C", 4)
# pq.insert("Task D", 2)
#
# print("Вся черга:")
# for elem in pq.view_queue():
#     print(elem)
#
# print("\nМаксимальний пріоритет:", pq.max_priority_oper())
#
# print("\nЧерга після видалення:")
# for elem in pq.view_queue():
#     print(elem)
