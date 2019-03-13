###
# Problem
###

# Test if a binary tree is symmetric. That is, if the left subtree
# is a mirror of the right subtree. (with regard to structure and
# keys

###
# Work
###
# Questions:
# Size of tree, output type, etc etc

def symmetric(node):
  return mirror(node.left, node.right)

def mirror(ln, rn):
  if not ln and not rn: return True   # Both None
  if not (ln and rn): return False    # Only one None
  if ln.value != rn.value: return False
  return mirror(ln.right, rn.left) and mirror(ln.left, rn.right)

# Tests:
from binary_tree import BinaryTree
a = BinaryTree(314)
b = BinaryTree(6)
c = BinaryTree(2)
d = BinaryTree(3)
e = BinaryTree(6)
f = BinaryTree(2)
g = BinaryTree(3)
a.left = b
b.right = c
c.right = d
a.right = e
e.left = f
f.left = g
print "True", symmetric(a)

a = BinaryTree(314)
b = BinaryTree(6)
c = BinaryTree(2)
d = BinaryTree(3)
e = BinaryTree(6)
f = BinaryTree(3)
g = BinaryTree(3)
a.left = b
b.right = c
c.right = d
a.right = e
e.left = f
f.left = g
print "False", symmetric(a)


a = BinaryTree(314)
b = BinaryTree(6)
c = BinaryTree(2)
d = BinaryTree(3)
e = BinaryTree(6)
f = BinaryTree(2)
a.left = b
b.right = c
c.right = d
a.right = e
e.left = f
print "False", symmetric(a)

# Time: 10 minutes

###
# Mistakes / Bugs / Misses
###
