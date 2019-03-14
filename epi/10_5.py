###
# Problem
###

# Given a binary tree whose values are bits, compute the sum of the
# binary numbers represented by root to leaf paths

###
# Work
###
# Questions:
# Height of tree (might matter in some languages)
# Define leaf (assume node with no children)

def tree_sum(node, current_path=0):
  if node is None: return 0
  new_path = (current_path << 1) + node.value
  if node.left or node.right:
    return tree_sum(node.left, new_path) + tree_sum(node.right, new_path)
  else:
    return new_path

# Tests
from binary_tree import BinaryTree
a = BinaryTree(0)
b = BinaryTree(0)
c = BinaryTree(1)
d = BinaryTree(0)
e = BinaryTree(1)
f = BinaryTree(0)
g = BinaryTree(1)
a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
c.right = g
print tree_sum(a), 6

a = BinaryTree(1)
b = BinaryTree(0)
c = BinaryTree(0)
d = BinaryTree(0)
e = BinaryTree(1)
f = BinaryTree(1)
g = BinaryTree(1)
h = BinaryTree(0)
i = BinaryTree(1)
j = BinaryTree(0)
k = BinaryTree(0)
l = BinaryTree(1)
m = BinaryTree(1)
n = BinaryTree(0)
o = BinaryTree(0)
p = BinaryTree(0)

a.left = b
a.right = i
b.left = c
b.right = f
c.left = d
c.right = e
f.right = g
g.left = h
i.left = j
i.right = o
j.right = k
k.left = l
k.right = n
l.right = m
o.right = p
print tree_sum(a), 8 + 9 + 22 + 51 + 24 + 12

# Time: 11 minutes (including that horrible book test)

###
# Mistakes / Bugs / Misses
###

