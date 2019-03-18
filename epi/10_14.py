###
# Problem
###

# Write a program that takes a perfect binary tree, and sets a
# "level_next" field on each node. The level_next node is a node's
# sibling on the right (on the same height of the tree)

###
# Work
###
# Questions:
# Size of tree
# Can I use O(n) space? (Assume yes, since we're adding the field anyway)
import collections

def set_level_next(node):
  traversal = level_order_with_nones(node)
  for i in xrange(len(traversal)):
    if traversal[i] is None: continue
    traversal[i].level_next = traversal[i+1]

def level_order_with_nones(node):
  result = []
  queue = collections.deque()
  queue.append(node)
  queue.append(None)
  while queue:
    current = queue.popleft()
    result.append(current)
    if current is None:
      if len(queue) > 0: queue.append(None)
    else:
      if current.left: queue.append(current.left)
      if current.right: queue.append(current.right)
  return result

# Tests
from binary_tree import BinaryTree
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
trav = level_order_with_nones(a)
print "***"
for n in trav:
  print n.value if n else "None"
print "***"

set_level_next(a)
for node in (a, b, c, d, e, f, g):
  print node.value, node.level_next.value if node.level_next else "None"

# Time: 15 minutes

###
# Mistakes / Bugs / Misses
###
# Used node instead of current at 34, 35
# Their solution is better. TODO: Make card
