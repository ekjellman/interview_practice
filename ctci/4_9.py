###
# Problem
###

# A BST was created by traversing an array from left to right and inserting
# each element. Given a BST, print all possible arrays that could have led
# to this tree.

###
# Work
###
# Questions:
# Output type? (Just print the arrays)
# Input type? (Root of a BST)

def print_bst_arrays(root, frontier=None, current_array=None):
  # Sub-optimal version with lots of list copies
  if frontier is None:
    frontier = [root]
  if current_array is None:
    current_array = []
  if not frontier:
    print current_array
  for node in frontier:
    new_array = current_array[:]  # Could avoid with wind/unwind
    new_frontier = frontier[:]
    new_frontier.remove(node)
    new_array.append(node.value)
    if node.left: new_frontier.append(node.left)
    if node.right: new_frontier.append(node.right)
    print_bst_arrays(root, new_frontier, new_array)

def print_bst_arrays_2(root, frontier=None, current_array=None):
  if frontier is None:
    frontier = [root]
  if current_array is None:
    current_array = []
  if not frontier:
    print current_array
  for i in xrange(len(frontier)):
    node = frontier.pop(i)
    current_array.append(node.value)
    frontier_count = 0
    if node.left:
      frontier.append(node.left)
      frontier_count += 1
    if node.right:
      frontier.append(node.right)
      frontier_count += 1
    print_bst_arrays_2(root, frontier, current_array)
    while frontier_count > 0:
      frontier_count -= 1
      frontier.pop()
    current_array.pop()
    frontier.insert(i, node)

class BinaryTree(object):
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

bst = BinaryTree(10)
bst.left = BinaryTree(5)
bst.right = BinaryTree(15)
bst.right.left = BinaryTree(12)
print_bst_arrays(bst)
print_bst_arrays_2(bst)

# Time: 20 minutes (11 minutes for first version)

###
# Mistakes / Bugs / Misses
###
# in BinaryTree did self.left = left and self.right = right
# print_bst_arrays printed lists of nodes, not lists of values
# --- print_bst_arrays_2 errors
# Line 40: was len(frontier) instead of xrange(len(frontier))
# used both node and next_node for node
# Line 51: was >= 0 instead of > 0
# Forgot the recursive call

# I am pretty sure the algorithm she describes in the book is doing the same
# thing mine is, from a different viewpoint. Unfortunately, she doesn't give
# an example answer except for a trivial tree.
# Also, her solution returns a list of lists, where the problem statement says
# print. If we wanted to do this, we could pass along a results list.
