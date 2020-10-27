import unittest
from LCA import Node
from LCA import lca
from LCA import treeToString


class TestLCA(unittest.TestCase):
    def test_lca_output(self):
        root = Node(20)
        root.left = Node(8)
        root.right = Node(22)
        root.left.left = Node(4)
        root.left.right = Node(12)
        root.left.right.left = Node(10)
        root.left.right.right = Node(14)

        n1 = 10
        n2 = 14
        assert lca(root, n1, n2).data == 12

    def test_lca_output_2(self):
        root = Node(15)
        root.left = Node(12)
        root.left.left = Node(11)
        root.left.right = Node(13)
        root.right = Node(18)
        root.right.left = Node(17)

        n1 = 17
        n2 = 13
        assert lca(root, n1, n2).data == 15

    def test_tree_to_string(self):
        root = Node(20)
        root.left = Node(8)
        root.right = Node(22)
        root.left.left = Node(4)
        root.left.right = Node(12)
        root.left.right.left = Node(10)
        root.left.right.right = Node(14)

        string = []
        treeToString(root, string)

        assert ''.join(string) == '20(8(4)(12(10)(14)))(22)'

    def test_LCA_none_node(self):
        n1 = 1
        n2 = 3

        assert lca(None, n1, n2) is None

    def test_LCA_single_node_tree(self):

        root = Node(1)
        n1 = 1
        n2 = 3

        assert lca(root, n1, n2).data == 1

    def test_arguments_not_in_tree(self):

        root = Node(2)
        root.left = Node(1)
        root.right = Node(3)

        n1 = 5
        n2 = 6

        assert lca(root, n1, n2) is None

    def test_empty_tree(self):

        root = None
        assert lca(root, 3, 4) is None

    def test_tree_out_of_order(self):
        root = Node(50)
        root.left = Node(30)
        root.right = Node(10)
        root.left.left = Node(40)
        root.left.right = Node(70)
        root.right.left = Node(20)
        root.right.right = Node(60)

        assert lca(root, 60, 40).data == 50
        assert lca(root, 30, 40).data == 30
        assert lca(root, 60, 20).data == 50
        assert lca(root, 70, 20).data == 50
