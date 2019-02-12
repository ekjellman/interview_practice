###
# Problem
###

# You have a BiNode, which points to two other nodes. This could be used to
# represent a binary tree (where node1 is left and node2 is right), or a
# doubly linked list (where node1 is prev and node2 is next). Convert a
# binary search tree implemented this way into a doubly linked list. Values
# should be kept in order, and this should be done in place.

###
# Work
###
# Questions:
# WRRRRRRRY
# Output type? (assume (head, tail) of new dll)
# Size of tree?

class BiNode(object):
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

def convert(node):
  if node.left:
    left_head, left_tail = convert(node.left)
  else:
    left_head, left_tail = None, None
  if node.right:
    right_head, right_tail = convert(node.right)
  else:
    right_head, right_tail = None, None
  node.left = left_tail
  node.right = right_head
  if node.left:
    node.left.right = node
  if node.right:
    node.right.left = node
  return (left_head, right_tail)

# Test

#           10
#     5             15
#  3    7       13     17
#      6          14

root = BiNode(10)
root.left = BiNode(5)
root.right = BiNode(15)
root.left.left = BiNode(3)
root.left.right = BiNode(7)
root.left.right.left = BiNode(6)
root.right.left = BiNode(13)
root.right.left.right = BiNode(14)
root.right.right = BiNode(17)

tail, head = convert(root)
print tail, head
current = tail
while True:
  print current.value
  if not current.right: break
  current = current.right

# Time: 25 minutes (FAILED)

###
# Mistakes / Bugs / Misses
###
# This solution is correct if we add these two lines after line 39:
#  if left_head is None: left_head = node
#  if right_tail is None: right_tail = node

