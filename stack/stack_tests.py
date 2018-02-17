import unittest

from stack import Item, Stack


def create_item(id_, value):
    Item(id_, value)


class TestStack(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()

    def test_insert_one_item(self):
        item1 = create_item(1, 1)

        self.assertEqual(0, self.stack.size)

        self.stack.push(item1)
        self.assertEqual(1, self.stack.size)
        self.assertEqual(item1, self.stack._items[0])

    def test_insert_two_items(self):
        item1 = create_item(1, 1)
        item2 = create_item(2, 2)

        self.assertEqual(0, self.stack.size)

        self.stack.push(item1)
        self.stack.push(item2)
        self.assertEqual(2, self.stack.size)
        self.assertEqual(item1, self.stack._items[0])
        self.assertEqual(item2, self.stack._items[1])

    def test_pop_one_item_when_stack_start_with_one_item(self):
        item1 = create_item(1, 1)
        self.stack.push(item1)

        result = self.stack.pop()
        self.assertEqual(0, self.stack.size)
        self.assertEqual(item1, result)

    def test_pop_one_item_when_stack_start_with_two_items(self):
        item1 = create_item(1, 1)
        item2 = create_item(2, 2)
        self.stack.push(item1)
        self.stack.push(item2)

        result = self.stack.pop()
        self.assertEqual(1, self.stack.size)
        self.assertEqual(item1, result)
        self.assertEqual(item2, self.stack._items[0])

    def test_try_pop_when_stack_is_empty(self):
        self.assertEqual(0, self.stack.size)
        result = self.stack.pop()

        self.assertEqual(0, self.stack.size)
        self.assertEqual(None, result)


if __name__ == '__main__':
    unittest.main()
