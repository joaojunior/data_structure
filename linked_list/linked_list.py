class Item():
    def __init__(self, id_, value):
        self.id_ = id_
        self.value = value
        self.next = None


class LinkedList():
    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self, item):
        self.size += 1
        if self.root is None:
            self.root = item
        else:
            root = self.root
            while root is not None:
                if root.next is None:
                    root.next = item
                    root = item
                root = root.next

    def search(self, item):
        root = self.root
        item_found = None
        while item_found is None and root is not None:
            if item.id_ == root.id_:
                item_found = item
            else:
                root = root.next
        return item_found
