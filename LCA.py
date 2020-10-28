# Code from https://www.geeksforgeeks.org/lowest-common-ancestor-binary-tree-set-1/ but 
# I have made a few modifications to make it easier for me to understand.
# Python is the second language and one with which I was unfamiliar until recently.
# It is interesteing to see how this different imlepmentation flows compared to java.



class Node:


    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None



def lca(root, n1, n2):

    if root is None:
        return None

    
    if root.data > n1 and root.data > n2:
        return lca(root.left, n1, n2)

       
    if root.data < n1 and root.data < n2:
        return lca(root.right, n1, n2)

    return root


def treeToString(root: Node, string: list):
 
    if root is None:
        return


    string.append(str(root.data))


    if not root.left and not root.right:
        return


    string.append('(')
    treeToString(root.left, string)
    string.append(')')

    if root.right:
        string.append('(')
        treeToString(root.right, string)
        string.append(')')
