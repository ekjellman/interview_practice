###
# Problem
###

# Given a pre-order traversal that marks empty children with null,
# reconstruct the tree

###
# Work
###
# Questions:
# Size of the tree
# Use cases
from binary_tree import BinaryTree

def reconstruct(traversal):
  # TODO: Error checking (invalid traversal)
  root_value = traversal[0]
  root = BinaryTree(root_value)
  stack = [(root, "R"), (root, "L")]  # Indicates we could recurse
  for i in xrange(1, len(traversal)):
    value = traversal[i]
    node, branch = stack.pop()
    if value is None: continue
    new_node = BinaryTree(value)
    if branch == "L":
      node.left = new_node
    elif branch == "R":
      node.right = new_node
    else:
      raise ValueError("shouldn't get here")
    stack.append((new_node, "R"))
    stack.append((new_node, "L"))
  return root

# Test:
traversal = ["H", "B", "F", None, None, "E", "A", None, None, None,
             "C", None, "D", None, "G", "I", None, None, None]
tree = reconstruct(traversal)
print traversal
print [node.value for node in tree.pre_order()]

# Time: 15 minutes

###
# Mistakes / Bugs / Misses
###
# The recursive solution in the book is clever and I want to
# remember it. (TODO: make card)
