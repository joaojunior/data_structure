import unittest


from binary_search_tree import BinarySearchTree, Node


def create_node(id_, value):
    return Node(id_, value)


class TestInsertInBinarySearchTree(unittest.TestCase):
    def setUp(self):
        self.bst = BinarySearchTree()

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


class TestRemoveInBinarySearchTree(unittest.TestCase):
    def setUp(self):
        self.bst = BinarySearchTree()

    def test_remove_root_with_no_children(self):
        node1 = create_node(1, 1)
        self.bst.insert(node1)

        result = self.bst.remove(1)
        self.assertEqual(0, self.bst.number_of_nodes)
        self.assertEqual(node1, result)
        self.assertEqual(None, self.bst.root)

    def test_remove_root_with_one_child_left(self):
        node1 = create_node(1, 1)
        node0 = create_node(0, 0)
        self.bst.insert(node1)
        self.bst.insert(node0)

        result = self.bst.remove(node1.value)
        self.assertEqual(1, self.bst.number_of_nodes)
        self.assertEqual(node1, result)
        self.assertEqual(node0, self.bst.root)

    def test_remove_root_with_one_child_right(self):
        node1 = create_node(1, 1)
        node2 = create_node(2, 2)
        self.bst.insert(node1)
        self.bst.insert(node2)

        result = self.bst.remove(node1.value)
        self.assertEqual(1, self.bst.number_of_nodes)
        self.assertEqual(node1, result)
        self.assertEqual(node2, self.bst.root)

    def test_remove_root_with_two_children(self):
        node1 = create_node(1, 1)
        node2 = create_node(2, 2)
        node3 = create_node(3, 3)

        self.bst.insert(node2)
        self.bst.insert(node1)
        self.bst.insert(node3)

        result = self.bst.remove(node2.value)
        self.assertEqual(2, self.bst.number_of_nodes)
        self.assertEqual(node2, result)
        self.assertEqual(node3, self.bst.root)
        self.assertEqual(node1, self.bst.root.left)
        self.assertEqual(None, self.bst.root.right)

    def test_remove_left_leaf(self):
        node1 = create_node(1, 1)
        node2 = create_node(2, 2)
        node3 = create_node(3, 3)

        self.bst.insert(node2)
        self.bst.insert(node1)
        self.bst.insert(node3)

        result = self.bst.remove(node1.value)
        self.assertEqual(2, self.bst.number_of_nodes)
        self.assertEqual(node1, result)
        self.assertEqual(node2, self.bst.root)
        self.assertEqual(None, self.bst.root.left)
        self.assertEqual(node3, self.bst.root.right)

    def test_remove_right_leaf(self):
        node1 = create_node(1, 1)
        node2 = create_node(2, 2)
        node3 = create_node(3, 3)

        self.bst.insert(node2)
        self.bst.insert(node1)
        self.bst.insert(node3)

        result = self.bst.remove(node3.value)
        self.assertEqual(2, self.bst.number_of_nodes)
        self.assertEqual(node3, result)
        self.assertEqual(node2, self.bst.root)
        self.assertEqual(node1, self.bst.root.left)
        self.assertEqual(None, self.bst.root.right)

    def test_remove_node_with_one_right_child(self):
        node1 = create_node(1, 1)
        node2 = create_node(2, 2)
        node3 = create_node(3, 3)
        node4 = create_node(4, 4)

        self.bst.insert(node2)
        self.bst.insert(node1)
        self.bst.insert(node3)
        self.bst.insert(node4)

        result = self.bst.remove(node3.value)
        self.assertEqual(3, self.bst.number_of_nodes)
        self.assertEqual(node3, result)
        self.assertEqual(node2, self.bst.root)
        self.assertEqual(node1, self.bst.root.left)
        self.assertEqual(node4, self.bst.root.right)

    def test_remove_node_with_one_left_child(self):
        node1 = create_node(1, 1)
        node2 = create_node(2, 2)
        node3 = create_node(3, 3)
        node0 = create_node(0, 0)

        self.bst.insert(node2)
        self.bst.insert(node1)
        self.bst.insert(node3)
        self.bst.insert(node0)

        result = self.bst.remove(node1.value)
        self.assertEqual(3, self.bst.number_of_nodes)
        self.assertEqual(node1, result)
        self.assertEqual(node2, self.bst.root)
        self.assertEqual(node0, self.bst.root.left)
        self.assertEqual(node3, self.bst.root.right)

    def test_remove_node_with_two_children(self):
        node1 = create_node(1, 1)
        node2 = create_node(2, 2)
        node3 = create_node(3, 3)
        node4 = create_node(4, 4)
        node5 = create_node(5, 3.5)

        self.bst.insert(node2)
        self.bst.insert(node1)
        self.bst.insert(node3)
        self.bst.insert(node4)
        self.bst.insert(node5)

        result = self.bst.remove(node3.value)
        self.assertEqual(4, self.bst.number_of_nodes)
        self.assertEqual(node3, result)
        self.assertEqual(node2, self.bst.root)
        self.assertEqual(node1, self.bst.root.left)
        self.assertEqual(node5, self.bst.root.right)
        self.assertEqual(node4, self.bst.root.right.right)


class TestSearchInBinarySearchTree(unittest.TestCase):
    def setUp(self):
        self.bst = BinarySearchTree()
        self.node1 = create_node(1, 1)
        self.node2 = create_node(2, 2)
        self.node3 = create_node(3, 3)

        self.bst.insert(self.node2)
        self.bst.insert(self.node3)
        self.bst.insert(self.node1)

    def test_search_root_node(self):
        result = self.bst.search(self.node2.value)
        self.assertEqual(self.node2, result)

    def test_search_right_leaf(self):
        result = self.bst.search(self.node1.value)
        self.assertEqual(self.node1, result)

    def test_search_left_leaf(self):
        result = self.bst.search(self.node3.value)
        self.assertEqual(self.node3, result)

    def test_search_node_not_exist(self):
        result = self.bst.search(4)
        self.assertEqual(None, result)


class TestEmptyInBinarySearchTree(unittest.TestCase):
    def setUp(self):
        self.bst = BinarySearchTree()

    def test_empty_binary_search_tree(self):
        self.assertEqual(0, self.bst.number_of_nodes)
        self.assertEqual(None, self.bst.root)

    def test_insert_node(self):
        node1 = create_node(1, 1)

        self.bst.insert(node1)
        self.assertEqual(1, self.bst.number_of_nodes)
        self.assertEqual(node1, self.bst.root)

    def test_search_node(self):
        result = self.bst.search(1)
        self.assertEqual(None, result)

    def test_remove_node(self):
        result = self.bst.remove(1)
        self.assertEqual(None, result)


if __name__ == '__main__':
    unittest.main()
