class RBNode:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.color = "RED"
        self.left = None
        self.right = None
        self.parent = None


class RedBlackTree:
    def __init__(self):
        self.NIL = RBNode(None, 0)
        self.NIL.color = "BLACK"
        self.NIL.left = self.NIL.right = self.NIL
        self.root = self.NIL

    def insert_order(self, name, price):
        new_node = RBNode(name, price)
        new_node.left = new_node.right = self.NIL
        parent = None
        current = self.root

        while current != self.NIL:
            parent = current
            if new_node.price >= current.price:
                current = current.left
            else:
                current = current.right

        new_node.parent = parent
        if parent is None:
            self.root = new_node
        elif new_node.price >= parent.price:
            parent.left = new_node
        else:
            parent.right = new_node

        new_node.color = "RED"
        self._fix_insert(new_node)

    def _fix_insert(self, node):
        while node != self.root and node.parent.color == "RED":
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle.color == "RED":
                    node.parent.color = "BLACK"
                    uncle.color = "BLACK"
                    node.parent.parent.color = "RED"
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self._rotate_left(node)
                    node.parent.color = "BLACK"
                    node.parent.parent.color = "RED"
                    self._rotate_right(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                if uncle.color == "RED":
                    node.parent.color = "BLACK"
                    uncle.color = "BLACK"
                    node.parent.parent.color = "RED"
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self._rotate_right(node)
                    node.parent.color = "BLACK"
                    node.parent.parent.color = "RED"
                    self._rotate_left(node.parent.parent)
        self.root.color = "BLACK"

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

    def _inorder_with_position(self, node, path, result):
        if node != self.NIL:
            self._inorder_with_position(node.left, path + ".left", result)
            result.append((path, node.name, node.price, node.color))
            self._inorder_with_position(node.right, path + ".right", result)

    def view_orders(self):
        result = []
        self._inorder_with_position(self.root, "root", result)
        return result

    def find_max(self):
        node = self.root
        if node == self.NIL:
            return None
        while node.left != self.NIL:
            node = node.left
        return node

    def find_min(self):
        node = self.root
        if node == self.NIL:
            return None
        while node.right != self.NIL:
            node = node.right
        return node

    def delete_node(self, z):
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

    def _transplant(self, u, v):
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def _minimum(self, node):
        while node.left != self.NIL:
            node = node.left
        return node

    def _fix_delete(self, x):
        while x != self.root and x.color == "BLACK":
            if x == x.parent.left:
                brother = x.parent.right
                if brother.color == "RED":
                    brother.color = "BLACK"
                    x.parent.color = "RED"
                    self._rotate_left(x.parent)
                    brother = x.parent.right
                if brother.left.color == "BLACK" and brother.right.color == "BLACK":
                    brother.color = "RED"
                    x = x.parent
                else:
                    if brother.right.color == "BLACK":
                        brother.left.color = "BLACK"
                        brother.color = "RED"
                        self._rotate_right(brother)
                        brother = x.parent.right
                    brother.color = x.parent.color
                    x.parent.color = "BLACK"
                    brother.right.color = "BLACK"
                    self._rotate_left(x.parent)
                    x = self.root
            else:
                brother = x.parent.left
                if brother.color == "RED":
                    brother.color = "BLACK"
                    x.parent.color = "RED"
                    self._rotate_right(x.parent)
                    brother = x.parent.left
                if brother.left.color == "BLACK" and brother.right.color == "BLACK":
                    brother.color = "RED"
                    x = x.parent
                else:
                    if brother.left.color == "BLACK":
                        brother.right.color = "BLACK"
                        brother.color = "RED"
                        self._rotate_left(brother)
                        brother = x.parent.left
                    brother.color = x.parent.color
                    x.parent.color = "BLACK"
                    brother.left.color = "BLACK"
                    self._rotate_right(x.parent)
                    x = self.root
        x.color = "BLACK"


def main():
    tree = RedBlackTree()

    while True:
        print("\n1. Додати заявку")
        print("2. Показати всі заявки")
        print("3. Знайти мінімальну ціну (та видалити)")
        print("4. Знайти максимальну ціну (та видалити)")
        print("5. Вихід")
        choice = input("Вибір: ")

        if choice == "1":
            name = input("Введіть назву акцій: ")
            price = float(input("Введіть ціну: "))
            tree.insert_order(name, price)
            print("Заявка додана!")

        elif choice == "2":
            print("Усі заявки:")
            orders = tree.view_orders()
            if orders:
                for order in orders:
                    print(f"{order[0]} — {order[1]} (Ціна: {order[2]}, Колір: {order[3]})")
            else:
                print("Немає заявок.")

        elif choice == "3":
            min_order = tree.find_min()
            if min_order:
                print(f"Мінімальна ціна: {min_order.price} — {min_order.name}")
                tree.delete_node(min_order)
                print("Заявку видалено.")
            else:
                print("Немає заявок.")

        elif choice == "4":
            max_order = tree.find_max()
            if max_order:
                print(f"Максимальна ціна: {max_order.price} — {max_order.name}")
                tree.delete_node(max_order)
                print("Заявку видалено.")
            else:
                print("Немає заявок.")

        elif choice == "5":
            print("Вихід.")
            break

        else:
            print("Невірний вибір. Спробуйте знову.")


if __name__ == "__main__":
    main()



