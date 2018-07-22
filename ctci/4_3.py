import collections
###
# Problem
###

# Convert a binary tree into a set of linked lists, one linked list per level

###
# Work
###

# Questions:
# Return type? (Assume a list of LinkedList objects)
# Input? (Assume the root of the BST)
# What to do for empty input / None input? (assume return empty list)

class BST(object):
  def __init__(self, value):
    self.value = value
    self.right = None
    self.left = None

def make_level_lists(bst):
  if not bst: return []
  level_lists = []
  current = collections.deque()
  current.append(bst)
  while current:
    next_level = collections.deque()
    for bst_node in current:
      if bst_node.left: next_level.append(bst_node.left)
      if bst_node.right: next_level.append(bst_node.right)
    level_lists.append(current)
    current = next_level
  return level_lists

bst = BST(0)
bst.left = BST(1)
bst.right = BST(2)
bst.left.left = BST(3)
bst.left.right = BST(4)
bst.right.left = BST(5)
bst.left.left.left = BST(6)

lists = make_level_lists(bst)
for l in lists:
  print l

# Time: 11 minutes

###
# Mistakes / Bugs / Misses
###
# Did not think of empty case before coding
