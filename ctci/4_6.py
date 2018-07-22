###
# Problem
###

# Given a BST node with parent links, find the in-order successor of the node.

###
# Work
###
# Questions:
# What if there is no successor? (Assume return None)
# Input/Output types (input is a BST node, output is also a node)

# Inorder traversal is L Root R
# If there is a right node, go right, then left as far as possible
#   This is saying we were at "Root"
# If not, go up until the child is the left child of a parent, and return the
#   parent
#   This is saying we were at "L"
# If this never happens, we were at the end of the traversal

class BST(object):
  def __init__(self, value, parent):
    self.value = value
    self.parent = parent
    self.left = None
    self.right = None

def find_next_node(bst):
  if bst.right:
    current = bst.right
    while current.left:
      current = current.left
    return current
  else:
    current = bst
    while current.parent and current != current.parent.left:
      current = current.parent
    return current.parent

bst = BST(20, None)
bst.left = BST(10, bst)
bst.right = BST(30, bst)
bst.left.left = BST(5, bst.left)
bst.left.right = BST(15, bst.left)
bst.right.left = BST(25, bst.right)
bst.right.right = BST(35, bst.right)
bst.left.left.right = BST(7, bst.left.left)
bst.right.right.left = BST(32, bst.right.right)

current = bst.left.left
while current:
  print current.value
  current = find_next_node(current)

# Time: 16 minutes

###
# Mistakes / Bugs / Misses
###
# Forgot colon on 37
# Used def instead of class on 22
