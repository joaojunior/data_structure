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
        pass

    def test_search_middle(self):
        pass

    def test_search_leaf(self):
        pass

    def test_search_element_not_exist(self):
        pass

    def test_remove_head_with_no_children(self):
        pass

    def test_remove_head_with_one_child(self):
        pass

    def test_remove_head_with_two_children(self):
        pass

    def test_remove_leaf(self):
        pass

    def test_remove_middle_with_one_child(self):
        pass

    def test_remove_middle_with_two_children(self):
        pass


if __name__ == '__main__':
    unittest.main()
