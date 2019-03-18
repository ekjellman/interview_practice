###
# Problem
###

# Write API functions for a binary tree to set them to be locked
# or unlocked.

# A node cannot be set to lock if any of its descendants or ancestors are set
# to lock
# Change a node's lock state does not change the state of any other nodes

# Write the following functions:
# -- A function to test if a node is locked
# -- A function to lock the node. If it cannot be locked, return
#    False, otherwise lock it and return True
# -- A function to unlock the node.

###
# Work
###
# Questions:
# Is there any reason a node can't become unlocked? (I don't see it)
# Does the first function just return node.locked, or whether it can be locked?
# (I think just the first?
# Size of tree, etc.
# What to do if we try to unlock a node that's unlocked? (Do nothing)

# I'm going to implement these as not a part of the BinaryTree object because
# of the way I have things set up, but in an interview, I'd implement them
# as part of the class.

def is_locked(node):
  return node.locked

def unlock(node):
  node.locked = False

def lock(node):
  current = node
  while current:
    if current.locked:
      return False
    current = current.parent
  if child_locked(node):
    return False
  node.locked = True
  return True

def child_locked(node):
  if node.locked: return True
  if node.left and child_locked(node.left): return True
  if node.right and child_locked(node.right): return True
  return False

# Tests
from binary_tree import BinaryTree
a = BinaryTree("a")
b = BinaryTree("b")
c = BinaryTree("c")
d = BinaryTree("d")
e = BinaryTree("e")
f = BinaryTree("f")
g = BinaryTree("g")
a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
c.right = g
a.make_parents()
print lock(c), "True"
print lock(c), "False"
print lock(g), "False"
print is_locked(g), "False"
print is_locked(c), "True"
unlock(c)
print lock(a), "True"
for node in (b, c, d, e, f, g):
  print lock(node), "False"
for node in (b, c, d, e, f, g):
  print is_locked(node), "False"
unlock(a)
print lock(g), "True"
print lock(c), "False"
print lock(a), "False"
print lock(e), "True"
print lock(b), "False"
print lock(d), "True"

# Time: 13 minutes (FAILED) (My solution is correct but suboptimal)

###
# Mistakes / Bugs / Misses
###
# Missed close paren at 52
# Their solution is better. TODO: Make card
