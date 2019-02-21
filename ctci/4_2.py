###
# Problem
###

# Given a sorted array with unique integer elements, create a BST with
# minimal height

###
# Work
###

# Questions:
# Size of array

class BST(object):
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def print_tree(self, indent=0):
    print "-"  * indent, self.value
    if self.left: self.left.print_tree(indent + 1)
    if self.right: self.right.print_tree(indent + 1)
  # TODO: Other methods

def make_minimal_tree(array):
  if not array:
    return None
  if len(array) == 1:
    return BST(array[0])
  root_index = len(array) / 2
  return_tree = BST(array[root_index])
  return_tree.left = make_minimal_tree(array[:root_index])  # ?
  return_tree.right = make_minimal_tree(array[root_index + 1:])  # ?
  return return_tree

tree = make_minimal_tree(range(20))
tree.print_tree()
print tree.value
print tree.left.value
print tree.right.value

# Time: 18 minutes

###
# Mistakes / Bugs / Misses
###
# Line 32 had array / 2 instead of len(array) / 2
# BST __init__ didn't take a value
# Line 17: Set value to None instead of value
# print_tree called print self.left instead of .print_tree()
# print_tree also did not check if the node existed
# print_tree also did not actually indent.
# Line 33 had BST(root_index) instead of BST(array[root_index])
