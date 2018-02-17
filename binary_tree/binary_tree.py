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
