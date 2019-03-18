###
# Problem
###

# Given a binary tree that has parent nodes, find the inorder
# successor to a node in a binary tree.

###
# Work
###
# Questions:
# Size of tree?
# What to return if no inorder successor? (Assume None)

def inorder_successor(node):
  if node.right:
    current = node.right
    while current.left:
      current = current.left
    return current
  else:
    current = node.parent
    child = node
    while current and child == current.right:
      child = current
      current = current.parent
    return current

# Test:
from binary_tree import BinaryTree
a = BinaryTree(10)
b = BinaryTree(5)
c = BinaryTree(15)
d = BinaryTree(3)
e = BinaryTree(7)
f = BinaryTree(12)
g = BinaryTree(17)
a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
c.right = g
a.make_parents()

current = d
while current:
  print current.value
  current = inorder_successor(current)

# Time: 8 minutes

###
# Mistakes / Bugs / Misses
###
