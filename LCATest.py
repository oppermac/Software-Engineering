import unittest
from LCA import Node
from LCA import lca
from LCA import treeToString


class TestLCA(unittest.TestCase):
    def test__single_node_tree(self):

        root = Node(1)
        assert lca(root, 1, 6).data == 1
       
    def test_seven_node_tree(self):
		root = Node(1)
		root.left = Node(2)
	    root.right = Node(3)
		root.left.left = Node(4)
		root.left.right = Node(5)
		root.right.left = Node(6)
	    root.right.right = Node(7)
        
        assert lca(root, 4, 5).data == 2
        assert lca(root, 1, 2).data == 1

    def test_lca_output_teen_tree(self):
        root = Node(15)
        root.left = Node(19)
        root.left.left = Node(12)
        root.left.right = Node(13)
        root.right = Node(14)
        root.right.left = Node(17)

        assert lca(root, 17, 13).data == 15

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
       
        assert lca(None, 1, 3) is None

    def test_arguments_not_in_tree(self):

        root = Node(2)
        root.left = Node(1)
        root.right = Node(3)

        assert lca(root, 5, 6) is None

    def test_empty_tree(self):

        root = None
        assert lca(root, 8, 3) is None

    def test_tree_out_of_order(self):
        root = Node(50)
        root.left = Node(30)
        root.right = Node(10)
        root.left.left = Node(40)
        root.left.right = Node(70)
        root.right.left = Node(20)
        root.right.right = Node(60)

        assert lca(root, 60, 40).data == 50
        assert lca(root, 60, 20).data == 50
        assert lca(root, 70, 20).data == 50
        assert lca(root, 30, 40).data == 30
       
