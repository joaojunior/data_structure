import unittest


from binary_search_tree import BinarySearchTree, Node


def create_node(id_, value):
    return Node(id_, value)


class TestBinarySearchTree(unittest.TestCase):
    def setUp(self):
        self.bst = BinarySearchTree()

    def test_empty_binary_search_tree(self):
        self.assertEqual(0, self.bst.number_of_nodes)
        self.assertEqual(None, self.bst.root)

    def test_insert_one_node(self):
        pass

    def test_insert_two_nodes_in_ascendent_order(self):
        pass

    def test_insert_two_nodes_in_descendent_order(self):
        pass

    def test_insert_tree_nodes_in_ascendent_order(self):
        pass

    def test_insert_tree_nodes_in_descendent_order(self):
        pass

    def test_insert_tree_nodes(self):
        pass

    def test_search_root_node(self):
        pass

    def test_right_leaf(Self):
        pass

    def test_left_leaf(self):
        pass

    def test_remove_root_with_no_children(self):
        pass

    def test_remove_root_with_one_child(self):
        pass

    def test_remove_root_with_two_children(self):
        pass

    def test_remove_leaf(self):
        pass

    def test_remove_node_with_one_child(self):
        pass

    def test_remove_node_with_two_children(self):
        pass


if __name__ == '__main__':
    unittest.main()
