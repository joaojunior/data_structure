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

    def test_search_item_exist(self):
        item1 = create_item(1, 1)
        item2 = create_item(2, 2)
        item3 = create_item(3, 3)

        self.double_list.insert(item1)
        self.double_list.insert(item2)
        self.double_list.insert(item3)

        self.assertEqual(item3, self.double_list.search(item3.id_))

    def test_search_item_not_exist(self):
        item1 = create_item(1, 1)
        item2 = create_item(2, 2)
        item3 = create_item(3, 3)

        self.double_list.insert(item1)
        self.double_list.insert(item2)
        self.double_list.insert(item3)

        self.assertEqual(None, self.double_list.search(4))

    def test_search_in_list_empty(self):
        self.assertEqual(None, self.double_list.search(1))

    def test_remove_last_item(self):
        item1 = create_item(1, 1)
        item2 = create_item(2, 2)
        item3 = create_item(3, 3)

        self.double_list.insert(item1)
        self.double_list.insert(item2)
        self.double_list.insert(item3)

        item_removed = self.double_list.delete(item3.id_)
        self.assertEqual(item3, item_removed)
        self.assertEqual(2, self.double_list.size)
        self.assertEqual(item1, self.double_list.root)
        self.assertEqual(item2, self.double_list.root.next)

    def test_remove_first_item(self):
        item1 = create_item(1, 1)
        item2 = create_item(2, 2)
        item3 = create_item(3, 3)

        self.double_list.insert(item1)
        self.double_list.insert(item2)
        self.double_list.insert(item3)

        item_removed = self.double_list.delete(item1.id_)
        self.assertEqual(item1, item_removed)
        self.assertEqual(2, self.double_list.size)
        self.assertEqual(item2, self.double_list.root)
        self.assertEqual(item3, self.double_list.root.next)

    def test_remove_middle_item(self):
        item1 = create_item(1, 1)
        item2 = create_item(2, 2)
        item3 = create_item(3, 3)

        self.double_list.insert(item1)
        self.double_list.insert(item2)
        self.double_list.insert(item3)

        item_removed = self.double_list.delete(item2.id_)
        self.assertEqual(item2, item_removed)
        self.assertEqual(2, self.double_list.size)
        self.assertEqual(item1, self.double_list.root)
        self.assertEqual(item3, self.double_list.root.next)


if __name__ == '__main__':
    unittest.main()
