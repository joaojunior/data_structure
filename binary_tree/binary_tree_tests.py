import unittest

from binary_tree import BinaryTree, Item


def create_item(id_, value):
    return Item(id_, value)


class TestBinaryTree(unittest.TestCase):
    def setUp(self):
        self.binary_tree = BinaryTree()

    def test_empty_binary_tree(self):
        self.assertEqual(0, self.binary_tree.size)
        self.assertEqual(None, self.binary_tree.root)

    def test_insert_one_item_in_empty_binary_tree(self):
        item1 = create_item(1, 1)

        self.binary_tree.insert(item1)
        self.assertEqual(1, self.binary_tree.size)
        self.assertEqual(item1, self.binary_tree.root)
        self.assertEqual(None, self.binary_tree.root.left)
        self.assertEqual(None, self.binary_tree.root.right)

    def test_insert_two_items(self):
        item1 = create_item(1, 1)
        item2 = create_item(2, 2)

        self.binary_tree.insert(item1)
        self.binary_tree.insert(item2)
        self.assertEqual(2, self.binary_tree.size)
        self.assertEqual(item1, self.binary_tree.root)
        self.assertEqual(item2, self.binary_tree.root.left)
        self.assertEqual(None, self.binary_tree.root.right)

    def test_insert_three_items(self):
        item1 = create_item(1, 1)
        item2 = create_item(2, 2)
        item3 = create_item(3, 3)

        self.binary_tree.insert(item1)
        self.binary_tree.insert(item2)
        self.binary_tree.insert(item3)
        self.assertEqual(3, self.binary_tree.size)
        self.assertEqual(item1, self.binary_tree.root)
        self.assertEqual(item2, self.binary_tree.root.left)
        self.assertEqual(item3, self.binary_tree.root.right)

    def test_search_head(self):
        item1 = create_item(1, 1)

        self.binary_tree.insert(item1)
        result = self.binary_tree.search(item1.id_)
        self.assertEqual(item1, result)

    def test_search_left_child(self):
        item1 = create_item(1, 1)
        item2 = create_item(2, 2)

        self.binary_tree.insert(item1)
        self.binary_tree.insert(item2)

        result = self.binary_tree.search(item2.id_)
        self.assertEqual(item2, result)

    def test_search_right_child(self):
        item1 = create_item(1, 1)
        item2 = create_item(2, 2)
        item3 = create_item(3, 3)

        self.binary_tree.insert(item1)
        self.binary_tree.insert(item2)
        self.binary_tree.insert(item3)

        result = self.binary_tree.search(item3.id_)
        self.assertEqual(item3, result)

    def test_search_in_empty_binary_tree(self):
        result = self.binary_tree.search(1)
        self.assertEqual(None, result)

    def test_search_item_not_exist(self):
        item1 = create_item(1, 1)
        item2 = create_item(2, 2)
        item3 = create_item(3, 3)

        self.binary_tree.insert(item1)
        self.binary_tree.insert(item2)
        self.binary_tree.insert(item3)

        result = self.binary_tree.search(4)
        self.assertEqual(None, result)

    def test_remove_head_with_no_children(self):
        item1 = create_item(1, 1)

        self.binary_tree.insert(item1)

        result = self.binary_tree.remove(item1.id_)
        self.assertEqual(1, result.id_)
        self.assertEqual(1, result.value)
        self.assertEqual(0, self.binary_tree.size)
        self.assertEqual(None, self.binary_tree.root)

    def test_remove_head_with_one_child(self):
        item1 = create_item(1, 1)
        item2 = create_item(2, 2)

        self.binary_tree.insert(item1)
        self.binary_tree.insert(item2)

        result = self.binary_tree.remove(item1.id_)
        self.assertEqual(1, result.id_)
        self.assertEqual(1, result.value)
        self.assertEqual(1, self.binary_tree.size)
        self.assertEqual(2, self.binary_tree.root.id_)
        self.assertEqual(2, self.binary_tree.root.value)
        self.assertEqual(None, self.binary_tree.root.left)
        self.assertEqual(None, self.binary_tree.root.right)

    def test_remove_head_with_two_children(self):
        item1 = create_item(1, 1)
        item2 = create_item(2, 2)
        item3 = create_item(3, 3)

        self.binary_tree.insert(item1)
        self.binary_tree.insert(item2)
        self.binary_tree.insert(item3)

        result = self.binary_tree.remove(item1.id_)
        self.assertEqual(1, result.id_)
        self.assertEqual(1, result.value)
        self.assertEqual(2, self.binary_tree.size)
        self.assertEqual(3, self.binary_tree.root.id_)
        self.assertEqual(3, self.binary_tree.root.value)
        self.assertEqual(2, self.binary_tree.root.left.id_)
        self.assertEqual(2, self.binary_tree.root.left.value)
        self.assertEqual(None, self.binary_tree.root.right)

    def test_remove_leaf(self):
        item1 = create_item(1, 1)
        item2 = create_item(2, 2)
        item3 = create_item(3, 3)
        item4 = create_item(4, 4)

        self.binary_tree.insert(item1)
        self.binary_tree.insert(item2)
        self.binary_tree.insert(item3)
        self.binary_tree.insert(item4)

        result = self.binary_tree.remove(item4.id_)
        self.assertEqual(item4, result)
        self.assertEqual(3, self.binary_tree.size)
        self.assertEqual(item1, self.binary_tree.root)
        self.assertEqual(item2, self.binary_tree.root.left)
        self.assertEqual(item3, self.binary_tree.root.right)

    def test_remove_middle_with_one_child(self):
        item1 = create_item(1, 1)
        item2 = create_item(2, 2)
        item3 = create_item(3, 3)
        item4 = create_item(4, 4)

        self.binary_tree.insert(item1)
        self.binary_tree.insert(item2)
        self.binary_tree.insert(item3)
        self.binary_tree.insert(item4)

        result = self.binary_tree.remove(item2.id_)
        self.assertEqual(2, result.id_)
        self.assertEqual(2, result.value)
        self.assertEqual(2, result.value)
        self.assertEqual(3, self.binary_tree.size)
        self.assertEqual(item1, self.binary_tree.root)
        self.assertEqual(3, self.binary_tree.root.left.id_)
        self.assertEqual(3, self.binary_tree.root.left.value)
        self.assertEqual(item4, self.binary_tree.root.left.left)

    def test_remove_middle_with_two_children(self):
        item1 = create_item(1, 1)
        item2 = create_item(2, 2)
        item3 = create_item(3, 3)
        item4 = create_item(4, 4)
        item5 = create_item(5, 5)

        self.binary_tree.insert(item1)
        self.binary_tree.insert(item2)
        self.binary_tree.insert(item3)
        self.binary_tree.insert(item4)
        self.binary_tree.insert(item5)

        result = self.binary_tree.remove(item2.id_)
        self.assertEqual(2, result.id_)
        self.assertEqual(2, result.value)
        self.assertEqual(4, self.binary_tree.size)
        self.assertEqual(item1, self.binary_tree.root)
        self.assertEqual(3, self.binary_tree.root.left.id_)
        self.assertEqual(3, self.binary_tree.root.left.value)
        self.assertEqual(item4, self.binary_tree.root.left.left)
        self.assertEqual(item5, self.binary_tree.root.left.right)

    def test_remove_item_not_exist(self):
        item1 = create_item(1, 1)
        item2 = create_item(2, 2)
        item3 = create_item(3, 3)
        item4 = create_item(4, 4)
        item5 = create_item(5, 5)

        self.binary_tree.insert(item1)
        self.binary_tree.insert(item2)
        self.binary_tree.insert(item3)
        self.binary_tree.insert(item4)
        self.binary_tree.insert(item5)

        result = self.binary_tree.remove(6)
        self.assertEqual(None, result)
        self.assertEqual(5, self.binary_tree.size)
        self.assertEqual(item1, self.binary_tree.root)
        self.assertEqual(item2, self.binary_tree.root.left)
        self.assertEqual(item3, self.binary_tree.root.right)
        self.assertEqual(item4, self.binary_tree.root.left.left)
        self.assertEqual(item5, self.binary_tree.root.left.right)


if __name__ == '__main__':
    unittest.main()
