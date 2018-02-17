import unittest

from queue import Item, Queue


def create_item(id_, value):
    return Item(id_, value)


class TestQueue(unittest.TestCase):
    def setUp(self):
        self.queue = Queue()

    def test_enqueue_one_item(self):
        item1 = create_item(1, 1)
        self.assertEqual(0, self.queue.size)

        self.queue.enqueue(item1)
        self.assertEqual(1, self.queue.size)
        self.assertEqual(item1, self.queue._items[0])

    def test_enqueue_two_items(self):
        item1 = create_item(1, 1)
        item2 = create_item(2, 2)
        self.assertEqual(0, self.queue.size)

        self.queue.enqueue(item1)
        self.queue.enqueue(item2)
        self.assertEqual(2, self.queue.size)
        self.assertEqual(item1, self.queue._items[0])
        self.assertEqual(item2, self.queue._items[1])

    def test_dequeue_one_item_when_queue_has_one_item(self):
        item1 = create_item(1, 1)
        self.queue.enqueue(item1)

        result = self.queue.dequeue()
        self.assertEqual(0, self.queue.size)
        self.assertEqual(item1, result)

    def test_dequeue_one_item_when_queue_has_two_items(self):
        item1 = create_item(1, 1)
        item2 = create_item(2, 2)
        self.queue.enqueue(item1)
        self.queue.enqueue(item2)

        result = self.queue.dequeue()
        self.assertEqual(1, self.queue.size)
        self.assertEqual(item1, result)
        self.assertEqual(item2, self.queue._items[0])

    def test_try_dequeue_when_queue_is_empty(self):
        result = self.queue.dequeue()

        self.assertEqual(None, result)
        self.assertEqual(0, self.queue.size)


if __name__ == '__main__':
    unittest.main()
