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

    def remove(self, id_):
        item = self.search(id_)
        if item is not None:
            if self.node_is_leaf(item):
                item = self.__remove__(id_)
            else:
                leaf = self.find_leaf(item)
                if leaf is not None:
                    leaf.id_, item.id_ = item.id_, leaf.id_
                    leaf.value, item.value = item.value, leaf.value
                    item = self.__remove__(id_)
        if item is not None:
            self.number_of_nodes -= 1
        return item

    def node_is_leaf(self, node):
        return node is not None and node.left is None and node.right is None

    def find_leaf(self, root):
        leaf = None
        if root is not None:
            if root.right is not None:
                root = root.right
            elif root.left is not None:
                root = self.root.left
            if root is not None:
                while root.left is not None:
                    root = root.left
                leaf = root
        return leaf

    def __remove__(self, id_):
        item = None
        if self.root.id_ == id_:
            item = self.root
            self.root = None
        else:
            parent = self._parent(id_, self.root)
            item = None
            if parent is not None:
                if parent.left is not None and parent.left.id_ == id_:
                    item = parent.left
                    parent.left = None
                elif parent.right is not None and parent.right.id_ == id_:
                    item = parent.right
                    parent.right = None
        return item

    def _parent(self, id_, root):
        if root is not None:
            if root.left is not None and root.right is not None:
                if root.left.id_ == id_ or root.right.id_ == id_:
                    return root
                else:
                    return (self._parent(id_, root.left) or
                            self._parent(id_, root.right))
            elif root.left is not None:
                if root.left.id_ == id_:
                    return root
                else:
                    return self._parent(id_, root.left)
            elif root.right is not None:
                if root.right.id_ == id_:
                    return root
                else:
                    return self._parent(id_, root.right)

    def min_value_node(self, node):
        current = node
        while(current.left is not None):
            current = current.left
        return current
