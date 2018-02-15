class Item():
    def __init__(self, id_, value):
        self.id_ = id_
        self.value = value
        self.next = None
        self.before = None


class DoubleLinkedList():
    def __init__(self):
        self.size = 0
        self.root = None

    def insert(self, item):
        if self.root is None:
            self.root = item
        else:
            root = self.root
            while root.next is not None:
                root = root.next
            item.before = root
            root.next = item
        self.size += 1

    def search(self, id_):
        founded = None
        root = self.root
        while founded is None and root is not None:
            if id_ == root.id_:
                founded = root
            else:
                root = root.next
        return founded
