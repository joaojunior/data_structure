class Item():
    def __init__(self, id_, value):
        self.id_ = id_
        self.value = value
        self.left = None
        self.right = None


class BinaryTree():
    def __init__(self):
        self.size = 0
        self.root = None

    def insert(self, item):
        if self.root is None:
            self.root = item
        else:
            root = self.root
            inserted = False
            while inserted is False:
                if root.left is None:
                    root.left = item
                    inserted = True
                elif root.right is None:
                    root.right = item
                    inserted = True
                root = root.left
        self.size += 1

    def search(self, id_):
        if self.root is not None:
            if self.root.id_ == id_:
                return self.root
            else:
                return (self._search(id_, self.root.left) or
                        self._search(id_, self.root.right))
        else:
            return None

    def _search(self, id_, root):
        if root is not None:
            if root.id_ == id_:
                return root
            else:
                return (self._search(id_, root.left) or
                        self._search(id_, root.right))
        else:
            return None

    def remove(self, id_):
        item = self.search(id_)
        if item is not None:
            if self.node_is_leaf(item):
                item = self.__remove__(id_)
            else:
                leaf = self.find_leaf()
                if leaf is not None:
                    leaf.id_, item.id_ = item.id_, leaf.id_
                    leaf.value, item.value = item.value, leaf.value
                    item = self.__remove__(id_)
        if item is not None:
            self.size -= 1
        return item

    def node_is_leaf(self, node):
        return node is not None and node.left is None and node.right is None

    def find_leaf(self):
        leaf = None
        root = None
        if self.root is not None:
            if self.root.right is not None:
                root = self.root.right
            elif self.root.left is not None:
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
