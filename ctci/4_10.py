###
# Problem
###

# T1 and T2 are large binary trees, T1 much larger than T2
# Determine if T2 is a subtree of T1. That is, is there a node in T1 where
# that node in T1 is identical to T2

###
# Work
###
# Questions:
# What do we mean by "identical"? Node object equality? value equality?
# What do the tree nodes look like? (assume just value, left, right)
# (Assume value equality. If object equality, we would just look for the
#  instance of T2's root in T1, because everything under would be the same)

# A minute's thought is not coming up with anything other than brute force, or
# some ridiculous scheme with hashing.
# If the nodes had some information about subtree size that would be helpful
# (because we could look for nodes with the same value and size instead of
# just the same value)

# I'll write the brute force algorithm.

def is_subtree(large, small):
  # Could make this one gigantic return statement, I think this reads better)
  if is_same(large, small): return True
  if large.left and is_subtree(large.left, small): return True
  if large.right and is_subtree(large.right, small): return True
  return False

def is_same(a, b):
  # This feels really ugly
  if a is None and b is None: return True
  if a is None or b is None: return False
  if a.value != b.value: return False
  return is_same(a.left, b.left) and is_same(a.right, b.right)

class BinaryTree(object):
  def __init__(self, value):
    self.value = value
    self.right = None
    self.left = None

a = BinaryTree(10)
a.left = BinaryTree(5)
a.right = BinaryTree(15)
a.left.left = BinaryTree(3)
a.left.right = BinaryTree(7)
a.right.right = BinaryTree(17)
a.right.left = BinaryTree(12)

b = BinaryTree(15)
b.right = BinaryTree(17)
b.left = BinaryTree(12)
print "True", is_subtree(a, b)

b = BinaryTree(15)
b.right = BinaryTree(17)
b.left = BinaryTree(13)
print "False", is_subtree(a, b)

b = BinaryTree(12)
print "True", is_subtree(a, b)

# Time: 18 minutes. A lot spent trying to improve is_same. Ugh.

###
# Mistakes / Bugs / Misses
###
# Lines 29-30: Used is_same() instead of is_subtree()
# Amusingly, my is_same() method is exactly her matchTree() method.
#   Maybe it's ok.
