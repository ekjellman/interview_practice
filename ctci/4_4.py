###
# Problem
###

# Determine if a BST is balanced

###
# Work
###

# Questions:
# Input/Output types? (assume input is BST node, output is boolean)
# Is an empty tree balanced? (Assume yes)
# Can I assume a bst node has a height value? (assume no)

class BST(object):
  def __init__(self, value):
    self.value = value
    self.right = None
    self.left = None

def get_tree_heights(bst, heights_hash):
  if bst is None:
    return
  get_tree_heights(bst.left, heights_hash)
  get_tree_heights(bst.right, heights_hash)
  if bst.left in heights_hash:
    left_height = heights_hash[bst.left]
  else:
    left_height = 0
  if bst.right in heights_hash:
    right_height = heights_hash[bst.right]
  else:
    right_height = 0
  heights_hash[bst] = 1 + max(left_height, right_height)

def is_balanced(bst):
  if not bst: return True
  heights_hash = {}
  get_tree_heights(bst, heights_hash)
  if bst.left in heights_hash:
    left_height = heights_hash[bst.left]
  else:
    left_height = 0
  if bst.right in heights_hash:
    right_height = heights_hash[bst.right]
  else:
    right_height = 0
  if abs(left_height - right_height) > 1: return False
  return is_balanced(bst.left) and is_balanced(bst.right)

# Is there a way to do this in O(n) time without O(n) space? I don't know.

# unbalanced
bst = BST(0)
bst.left = BST(1)
bst.left.left = BST(2)
bst.left.left.left = BST(5)
bst.right = BST(3)
bst.right.right = BST(4)
bst.right.right.right = BST(6)
print "False", is_balanced(bst)

bst = BST(0)
bst.left = BST(1)
bst.left.left = BST(2)
bst.left.right = BST(3)
bst.right = BST(4)
bst.right.left = BST(5)
bst.right.right = BST(6)
print "True", is_balanced(bst)

# Time: 25 minutes

###
# Mistakes / Bugs / Misses
###
# -- Did not ask about height value before coding
# put "best" instead of bst for first test tree
# forgot to make a empty hash in line 39
# Thought you could use None for a key in a hashtable.
# Had to redo heights_hash when I was trying to return heights
# Lots of other little details due to heights_hash
# REDO
# The answer in the book is better: have a recursive get_heights() function,
# but return -1 or a sentinel if the tree is unbalanced.
