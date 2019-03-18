###
# Problem
###

# Given a binary tree that stores the number of nodes in the subtree
# rooted at that node, find the kth node in an inorder traversal.

###
# Work
###
# Questions:
# 0 or 1 indexed? (Assume 0)
# Size of tree, use cases, etc
# Output type? (Assume node)

def kth_inorder(node, k):
  # TODO: Error checking (valid node, valid k)
  left_size = node.left.subtree_nodes if node.left else 0
  if k == left_size:
    return node
  elif k < left_size:
    return kth_inorder(node.left, k)
  else:
    return kth_inorder(node.right, k - left_size - 1)

# Tests
from binary_tree import BinaryTree
a = BinaryTree(10)
b = BinaryTree(5)
c = BinaryTree(15)
d = BinaryTree(3)
e = BinaryTree(7)
f = BinaryTree(12)
g = BinaryTree(17)
h = BinaryTree(13)

a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
c.right = g
f.right = h
a.populate()

for i in xrange(a.subtree_nodes):
  print kth_inorder(a, i).value

# Time: 11 minutes

###
# Mistakes / Bugs / Misses
###
