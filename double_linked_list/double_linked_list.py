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

    def delete(self, id_):
        item = None
        if self.root is not None and self.root.id_ == id_:
            item = self.root
            self.root = self.root.next
            self.root.next.before = self.root
        else:
            root = self.root
            while root.next is not None and item is None:
                if root.next.id_ == id_:
                    item = root.next
                    root.next = root.next.next
                    if root.next is not None:
                        root.next.before = root
                else:
                    root = root.next
        if item is not None:
            self.size -= 1
        return item
