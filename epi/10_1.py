###
# Problem
###

# Determine if a binary tree is height-balanced

###
# Work
###
# Questions:
# Size of tree, output types, blah blah

from binary_tree import BinaryTree

def balanced(node):
  if not node: return True
  left_height = height(node.left) if node.left else 0
  right_height = height(node.left) if node.right else 0
  if abs(left_height - right_height) > 1: return False
  return balanced(node.left) and balanced(node.right)

def height(node):
  if not node: return 0
  return 1 + max(height(node.left), height(node.right))

# Tests
a = BinaryTree("A")
b = BinaryTree("A")
c = BinaryTree("A")
d = BinaryTree("A")

a.left = b
b.left = c
b.right = d
print "False", balanced(a)
print "True", balanced(b)

# Time: 13 minutes (including making BinaryTree)

###
# Mistakes / Bugs / Misses
###
# TODO: Make a card for definition of balanced binary tree. My
#       impression of it was wrong (i.e. Figure 10-2 in their book
#       is balanced, but I didn't think it was)
# Forgot colons on 15 and 22
# 18 had node.left instead of node.right
# Their solution is nice. We could implement in Python with a tuple
# of (balanced, height) as the return. TODO: Make card
