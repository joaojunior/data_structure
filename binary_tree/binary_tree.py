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
