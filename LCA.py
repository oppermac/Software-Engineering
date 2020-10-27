# Code from https://www.geeksforgeeks.org/lowest-common-ancestor-binary-tree-set-1/ but 
# I have made a few modifications to make it easier for me to understand.
# Python is the second language and one with which I was unfamiliar until recently.
# It is interesteing to see how this different imlepmentation flows compared to java.
class LCA: 

	def __init__(self, key): 
		self.key = key 
		self.left = None
		self.right = None


def findPath( root, path, k): 


	if root is None: 
		return False

	path.append(root.key) 


	if root.key == k : 
		return True


	if ((root.left != None and findPath(root.left, path, k)) or
			(root.right!= None and findPath(root.right, path, k))): 
		return True

	
	path.pop() 
	return False


def findLCA(root, n1, n2): 

	path1 = [] 
	path2 = [] 


	if (not findPath(root, path1, n1) or not findPath(root, path2, n2)): 
		return -1

	
	i = 0
	while(i < len(path1) and i < len(path2)): 
		if path1[i] != path2[i]: 
			break
		i += 1
	return path1[i-1] 
