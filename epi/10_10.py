###
# Problem
###

# Given a preorder traversal and an in-order traversal, reconstruct
# a binary tree with those traversals.

###
# Work
###
# Questions:
# Size of the tree
# Unique elements? (Assume yes)

from binary_tree import BinaryTree

def reconstruct(inorder, preorder):
  if not inorder: return None
  assert len(inorder) == len(preorder)
  root_value = preorder[0]
  left_length = inorder.index(root_value)
  left_inorder = inorder[:left_length]
  right_inorder = inorder[left_length+1:]
  left_preorder = preorder[1:left_length+1]
  right_preorder = preorder[left_length+1:]
  tree = BinaryTree(root_value)
  tree.left = reconstruct(left_inorder, left_preorder)
  tree.right = reconstruct(right_inorder, right_preorder)
  return tree

# Test:
inorder = ["F", "B", "A", "E", "H", "C", "D", "I", "G"]
preorder = ["H", "B", "F", "E", "A", "C", "D", "G", "I"]
tree = reconstruct(inorder, preorder)
returned_inorder = [node.value for node in tree.in_order()]
returned_preorder = [node.value for node in tree.pre_order()]
print inorder
print returned_inorder
print preorder
print returned_preorder

# Time: 14 minutes

###
# Mistakes / Bugs / Misses
###
# Forgot colon on 17
# Used find() instead of index() on 21 (TODO: Make card)
# Forgot to return the tree at 29
# Did not make a hashtable from value to position in lists.
# TODO: Make an implementation card
