###
# Problem
###

# Compute the order of nodes in a binary tree in order of increasing depth.

###
# Work
###
import collections

class BinaryTree(object):
  def __init__(self, value):
    self.left = None
    self.right = None
    self.value = value

def level_order(tree):
  order = []
  queue = collections.deque()
  queue.append(tree)
  while queue:
    current = queue.popleft()
    order.append(current)
    if current.left: queue.append(current.left)
    if current.right: queue.append(current.right)
  return order

# Tests
a = BinaryTree("a")
b = BinaryTree("b")
c = BinaryTree("c")
d = BinaryTree("d")
e = BinaryTree("e")
f = BinaryTree("f")
g = BinaryTree("g")
a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
c.right = g
print [x.value for x in level_order(a)]

# Time: 6 minutes

###
# Mistakes / Bugs / Misses
###
# Forgot to check if node exists before putting it in the queue
