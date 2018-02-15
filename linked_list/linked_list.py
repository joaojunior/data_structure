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

    def search(self, id_):
        root = self.root
        item_found = None
        while item_found is None and root is not None:
            if id_ == root.id_:
                item_found = root
            else:
                root = root.next
        return item_found

    def delete(self, id_):
        root = self.root
        deleted = None
        if root is not None:
            if id_ == root.id_:
                deleted = root
                self.root = root.next
            while deleted is None and root.next is not None:
                if id_ == root.next.id_:
                    deleted = root.next
                    root.next = root.next.next
                else:
                    root = root.next
        if deleted is not None:
            self.size -= 1
        return deleted
