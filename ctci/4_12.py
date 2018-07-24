import collections

###
# Problem
###

# Given a binary tree with integer values, count the number of paths in the
# tree that sum up to a particular value.

###
# Work
###
# Input? (Assume a root node and a target)
# Output? (The number of paths)
# Size of the tree? Other use cases?
# Does the path of one node count?

class BinaryTree(object):
  def __init__(self, value):
    self.value = value
    self.right = None
    self.left = None

def paths_with_sum(tree, target, path_sum=0, prefix_sums=None):
  if prefix_sums is None:
    prefix_sums = collections.defaultdict(int)
  count = 1 if tree.value == target else 0
  new_path_sum = path_sum + tree.value
  if target - new_path_sum in prefix_sums:
    count += prefix_sums[new_path_sum - target]
  prefix_sums[new_path_sum] += 1
  if tree.left:
    count += paths_with_sum(tree.left, target, new_path_sum, prefix_sums)
  if tree.right:
    count += paths_with_sum(tree.right, target, new_path_sum, prefix_sums)
  prefix_sums[new_path_sum] -= 1
  return count

a = BinaryTree(3)
a.left = BinaryTree(-3)
a.right = BinaryTree(-2)
a.left.left = BinaryTree(2)
a.left.right = BinaryTree(3)
a.left.left.left = BinaryTree(1)
a.left.left.right = BinaryTree(1)
a.right = BinaryTree(-2)
a.right.left = BinaryTree(4)
a.right.right = BinaryTree(1)
a.right.left.left = BinaryTree(-2)
a.right.right.right = BinaryTree(1)

print paths_with_sum(a, 3), "9"
print paths_with_sum(a.left, 0), "9"
print paths_with_sum(a.right, 0), "9"

# Time: 25 minutes (failed)

###
# Mistakes / Bugs / Misses
###
# REDO
# It seems like I had the approach right, but there was a bug I couldn't find in
# time.
