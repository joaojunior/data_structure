import unittest


from double_linked_list import DoubleLinkedList, Item


def create_item(id_, value):
    return Item(id_, value)


class TestDoubleLinkedList(unittest.TestCase):
    def setUp(self):
        self.double_list = DoubleLinkedList()

    def test_insert_one_item(self):
        self.assertEqual(0, self.double_list.size)
        self.assertEqual(None, self.double_list.root)

        item1 = create_item(1, 1)

        self.double_list.insert(item1)
        self.assertEqual(1, self.double_list.size)
        self.assertEqual(item1, self.double_list.root)
        self.assertEqual(None, self.double_list.root.next)
        self.assertEqual(None, self.double_list.root.before)

    def test_insert_two_items(self):
        self.assertEqual(0, self.double_list.size)
        self.assertEqual(None, self.double_list.root)

        item1 = create_item(1, 1)
        item2 = create_item(2, 2)

        self.double_list.insert(item1)
        self.double_list.insert(item2)
        self.assertEqual(2, self.double_list.size)
        self.assertEqual(item1, self.double_list.root)
        self.assertEqual(item2, self.double_list.root.next)
        self.assertEqual(None, self.double_list.root.next.next)
        self.assertEqual(item1, self.double_list.root.next.before)

    def test_insert_three_items(self):
        self.assertEqual(0, self.double_list.size)
        self.assertEqual(None, self.double_list.root)

        item1 = create_item(1, 1)
        item2 = create_item(2, 2)
        item3 = create_item(3, 3)

        self.double_list.insert(item1)
        self.double_list.insert(item2)
        self.double_list.insert(item3)
        self.assertEqual(3, self.double_list.size)
        self.assertEqual(item1, self.double_list.root)
        self.assertEqual(item2, self.double_list.root.next)
        self.assertEqual(item1, self.double_list.root.next.before)
        self.assertEqual(item3, self.double_list.root.next.next)
        self.assertEqual(item2, self.double_list.root.next.next.before)
        self.assertEqual(item1, self.double_list.root.next.next.before.before)


if __name__ == '__main__':
    unittest.main()
