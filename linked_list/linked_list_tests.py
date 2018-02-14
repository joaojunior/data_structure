import unittest


from linked_list import Item, LinkedList


def create_item(id_, value):
    item = Item(id_, value)
    return item


class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.linked_list = LinkedList()

    def _assert_item(self, item, node):
        self.assertEqual(item.id_, node.id_)
        self.assertEqual(item.value, node.value)

    def test_insert_one_item(self):
        item1 = create_item(1, 1)
        self.assertEqual(0, self.linked_list.size)

        self.linked_list.insert(item1)
        self.assertEqual(1, self.linked_list.size)
        self._assert_item(item1, self.linked_list.root)
        self.assertEqual(None, self.linked_list.root.next)

    def test_insert_two_items(self):
        item1 = create_item(1, 1)
        item2 = create_item(2, 2)
        self.assertEqual(0, self.linked_list.size)

        self.linked_list.insert(item1)
        self.linked_list.insert(item2)
        self.assertEqual(2, self.linked_list.size)
        self._assert_item(item1, self.linked_list.root)
        self._assert_item(item2, self.linked_list.root.next)
        self.assertEqual(None, self.linked_list.root.next.next)

    def test_insert_three_items(self):
        item1 = create_item(1, 1)
        item2 = create_item(2, 2)
        item3 = create_item(3, 3)
        self.assertEqual(0, self.linked_list.size)

        self.linked_list.insert(item1)
        self.linked_list.insert(item2)
        self.linked_list.insert(item3)
        self.assertEqual(3, self.linked_list.size)
        self._assert_item(item1, self.linked_list.root)
        self._assert_item(item2, self.linked_list.root.next)
        self._assert_item(item3, self.linked_list.root.next.next)
        self.assertEqual(None, self.linked_list.root.next.next.next)

    def test_search_item_exist(self):
        item1 = create_item(1, 1)
        item2 = create_item(2, 2)
        item3 = create_item(3, 3)
        self.linked_list.insert(item1)
        self.linked_list.insert(item2)
        self.linked_list.insert(item3)

        expected = self.linked_list.search(item3)
        self.assertEqual(expected, item3)

    def test_search_item_not_exist(self):
        item1 = create_item(1, 1)
        item2 = create_item(2, 2)
        item3 = create_item(3, 3)
        item4 = create_item(4, 4)
        self.linked_list.insert(item1)
        self.linked_list.insert(item2)
        self.linked_list.insert(item3)

        self.assertEqual(None, self.linked_list.search(item4))

    def test_search_in_list_empty(self):
        item1 = create_item(1, 1)
        self.assertEqual(None, self.linked_list.search(item1))

    def test_delete_last_item(self):
        item1 = create_item(1, 1)
        item2 = create_item(2, 2)
        item3 = create_item(3, 3)
        self.linked_list.insert(item1)
        self.linked_list.insert(item2)
        self.linked_list.insert(item3)

        self.assertEqual(True, self.linked_list.delete(item3))
        self.assertEqual(2, self.linked_list.size)
        self.assertEqual(None, self.linked_list.root.next.next)

    def test_delete_first_item(self):
        item1 = create_item(1, 1)
        item2 = create_item(2, 2)
        item3 = create_item(3, 3)
        self.linked_list.insert(item1)
        self.linked_list.insert(item2)
        self.linked_list.insert(item3)

        self.assertEqual(True, self.linked_list.delete(item1))
        self.assertEqual(2, self.linked_list.size)
        self.assertEqual(None, self.linked_list.root.next.next)

    def test_delete_middle_item(self):
        item1 = create_item(1, 1)
        item2 = create_item(2, 2)
        item3 = create_item(3, 3)
        self.linked_list.insert(item1)
        self.linked_list.insert(item2)
        self.linked_list.insert(item3)

        self.assertEqual(True, self.linked_list.delete(item2))
        self.assertEqual(2, self.linked_list.size)
        self.assertEqual(None, self.linked_list.root.next.next)

    def test_delete_list_empty(self):
        item1 = create_item(1, 1)

        self.assertEqual(False, self.linked_list.delete(item1))
        self.assertEqual(0, self.linked_list.size)
        self.assertEqual(None, self.linked_list.root)


if __name__ == '__main__':
    unittest.main()
