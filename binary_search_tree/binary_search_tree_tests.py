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
        node1 = create_node(1, 1)

        self.bst.insert(node1)
        self.assertEqual(1, self.bst.number_of_nodes)
        self.assertEqual(node1, self.bst.root)

    def test_insert_two_nodes_in_ascendent_order(self):
        node1 = create_node(1, 1)
        node2 = create_node(2, 2)

        self.bst.insert(node1)
        self.bst.insert(node2)
        self.assertEqual(2, self.bst.number_of_nodes)
        self.assertEqual(node1, self.bst.root)
        self.assertEqual(None, self.bst.root.left)
        self.assertEqual(node2, self.bst.root.right)

    def test_insert_two_nodes_in_descendent_order(self):
        node1 = create_node(1, 1)
        node2 = create_node(2, 2)

        self.bst.insert(node2)
        self.bst.insert(node1)
        self.assertEqual(2, self.bst.number_of_nodes)
        self.assertEqual(node2, self.bst.root)
        self.assertEqual(node1, self.bst.root.left)
        self.assertEqual(None, self.bst.root.right)

    def test_insert_tree_nodes_in_ascendent_order(self):
        node1 = create_node(1, 1)
        node2 = create_node(2, 2)
        node3 = create_node(3, 3)

        self.bst.insert(node1)
        self.bst.insert(node2)
        self.bst.insert(node3)
        self.assertEqual(3, self.bst.number_of_nodes)
        self.assertEqual(node1, self.bst.root)
        self.assertEqual(None, self.bst.root.left)
        self.assertEqual(node2, self.bst.root.right)
        self.assertEqual(node3, self.bst.root.right.right)

    def test_insert_tree_nodes_in_descendent_order(self):
        node1 = create_node(1, 1)
        node2 = create_node(2, 2)
        node3 = create_node(3, 3)

        self.bst.insert(node3)
        self.bst.insert(node2)
        self.bst.insert(node1)
        self.assertEqual(3, self.bst.number_of_nodes)
        self.assertEqual(node3, self.bst.root)
        self.assertEqual(None, self.bst.root.right)
        self.assertEqual(node2, self.bst.root.left)
        self.assertEqual(node1, self.bst.root.left.left)

    def test_insert_tree_nodes(self):
        node1 = create_node(1, 1)
        node2 = create_node(2, 2)
        node3 = create_node(3, 3)

        self.bst.insert(node2)
        self.bst.insert(node3)
        self.bst.insert(node1)
        self.assertEqual(3, self.bst.number_of_nodes)
        self.assertEqual(node2, self.bst.root)
        self.assertEqual(node3, self.bst.root.right)
        self.assertEqual(node1, self.bst.root.left)

    def test_insert_tree_equal_nodes(self):
        node1 = create_node(1, 1)

        self.bst.insert(node1)
        self.bst.insert(node1)
        self.bst.insert(node1)
        self.assertEqual(3, self.bst.number_of_nodes)
        self.assertEqual(node1, self.bst.root)
        self.assertEqual(node1, self.bst.root.right)
        self.assertEqual(node1, self.bst.root.right.right)

    def test_search_root_node(self):
        pass

    def test_search_right_leaf(Self):
        pass

    def test_search_left_leaf(self):
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
