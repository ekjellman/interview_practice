###
# Problem
###

# Find the first common ancestor of two nodes in a binary tree. Don't use any
# additional data structures to hold nodes

###
# Work
###
# Questions:
# Does the tree have parent nodes? (assume no)
# Do we have the root of the tree? (assume yes)

# If we could use another data structure, or we had parent nodes, we could use
# a similar trick to the merged linked list problem: Find the path to each node
# (through search or parent traversal) and treat those as two merged linked
# lists and find the point of merging.

# Since we don't, we'll do it a more brute force way.

def find_common_ancestor(root, a, b):
  # TODO: Error checking: are a and b both in the tree?
  if node_in_tree(a, root.left) and node_in_tree(b, root.left):
    return find_common_ancestor(root.left, a, b)
  if node_in_tree(a, root.right) and node_in_tree(b, root.right):
    return find_common_ancestor(root.right, a, b)
  return root  # a and b are in different subtrees, so this is the FCA

def node_in_tree(node, tree):
  if node == tree: return True
  if tree.left and node_in_tree(node, tree.left): return True
  if tree.right and node_in_tree(node, tree.right): return True
  return False

class BinaryTree(object):
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

tree = BinaryTree(0)
tree.left = BinaryTree(0)
tree.right = BinaryTree(0)
tree.left.left = BinaryTree(0)
tree.left.right = BinaryTree(0)
tree.right.left = BinaryTree(0)
tree.right.right = BinaryTree(0)
tree.left.left.left = BinaryTree(0)
tree.left.left.right = BinaryTree(0)

result = find_common_ancestor(tree, tree.left.left.left, tree.left.right)
print tree.left, result
result = find_common_ancestor(tree, tree.left.left.left, tree.right)
print tree, result
result = find_common_ancestor(tree, tree.left.left.left, tree.right.right)
print tree, result
result = find_common_ancestor(tree, tree.left.left.left, tree.left.left.right)
print tree.left.left, result

# Time: 14 minutes

###
# Mistakes / Bugs / Misses
###
# Forgot to pass root in test cases
# Did not find slightly more optimized version.
# Did not ask what return type should be (assumed node)
# There is a slightly more optimal version where instead of researching each
#   subtree, we recurse and return whether p, q, fca, or null are in the
#   subtree. Base case: when we're at a leaf return the obvious, and combine
#   by returning the combination of the children. When we find a node with both,
#   that's the FCA, so start returning that.
# Could REDO, or could just make a card.
