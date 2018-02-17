class Item():
    def __init__(self, id_, value):
        self.id_ = id_
        self.value = value


class Queue():
    def __init__(self):
        self.size = 0
        self._items = []

    def enqueue(self, item):
        self.size += 1
        self._items.append(item)

    def dequeue(self):
        item = None
        if self.size > 0:
            self.size -= 1
            item = self._items.pop(0)
        return item
