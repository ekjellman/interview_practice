###
# Problem
###

# Find if there is a leaf whose path weight equals a given value.

###
# Work
###
# Questions:
# Return type? (Assume boolean? The leaf itself is also possible)
# Range of weights

def path_sum_exists(node, goal, partial_sum=0):
  if node is None: return False
  current_sum = partial_sum + node.value
  if node.left or node.right:
    return (path_sum_exists(node.left, goal, current_sum) or
            path_sum_exists(node.right, goal, current_sum))
  else:
    return current_sum == goal

# Test
from binary_tree import BinaryTree
a = BinaryTree(6)
b = BinaryTree(12)
c = BinaryTree(19)
d = BinaryTree(4)
e = BinaryTree(7)
f = BinaryTree(14)
g = BinaryTree(21)

a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
c.right = g

print "False", path_sum_exists(a, 0)
print "False", path_sum_exists(a, 100)
print "False", path_sum_exists(a, 18)
print "True", path_sum_exists(a, 25)
print "True", path_sum_exists(a, 39)
print "False", path_sum_exists(a, 38)

# Time: 10 minutes

###
# Mistakes / Bugs / Misses
###
