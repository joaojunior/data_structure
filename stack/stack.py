class Item():
    def __init__(self, id_, value):
        self.id_ = id_
        self.value = value


class Stack():
    def __init__(self):
        self.size = 0
        self._items = []

    def push(self, item):
        self._items.append(item)
        self.size += 1

    def pop(self):
        item = None
        if self.size > 0:
            item = self._items.pop()
            self.size -= 1
        return item
