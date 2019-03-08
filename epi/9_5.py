###
# Problem
###

# Compute the BST in-order traversal of a BST node. Don't use recursion

###
# Work
###
# Questions:
# Size of tree
# Output type (assume list of nodes)
# Use cases / space limitations
# Nodes unique? (Assume yes)

def in_order(node):
  stack = [(node, False)]
  traversal = []
  while stack:
    current, left_done = stack.pop()
    if not left_done:
      stack.append((current, True))
      if current.left:
        stack.append((current.left, False))
    else:
      traversal.append(current.value)
      if current.right:
        stack.append((current.right, False))
  return traversal

class BST(object):
  def __init__(self, value):
    self.value = value
    self.right = None
    self.left = None

root = BST(40)
root.left = BST(20)
root.left.left = BST(10)
root.left.right = BST(30)
root.right = BST(60)
root.right.left = BST(50)
root.right.right = BST(70)
root.right.right.right = BST(80)
root.right.right.right.left = BST(75)

print in_order(root)

# Time: 15 minutes

###
# Mistakes / Bugs / Misses
###
# Can do this without the left_done field (TODO: make card of their implementation)
