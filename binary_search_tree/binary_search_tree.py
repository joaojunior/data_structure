class Node():
    def __init__(self, id_, value):
        self.id_ = id_
        self.value = value
        self.left = None
        self.right = None

    def __eq__(self, other):
        return self.id_ == other.id_ and self.value == other.value


class BinarySearchTree():
    def __init__(self):
        self.number_of_nodes = 0
        self.root = None

    def insert(self, node):
        node = Node(node.id_, node.value)
        if self.root is None:
            self.root = node
        else:
            root = self.root
            inserted = False
            while inserted is False:
                if node.value >= root.value:
                    if root.right is None:
                        root.right = node
                        inserted = True
                    else:
                        root = root.right
                else:
                    if root.left is None:
                        root.left = node
                        inserted = True
                    else:
                        root = root.left
        self.number_of_nodes += 1

    def search(self, value):
        return self.__search__(value, self.root)

    def __search__(self, value, root):
        if root is None:
            return None
        elif root.value == value:
            return root
        elif value < root.value:
            return self.__search__(value, root.left)
        else:
            return self.__search__(value, root.right)
