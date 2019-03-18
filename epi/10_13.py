###
# Problem
###

# Compute the exterior of a binary tree.
# This is:
# The nodes from root to leftmost leaf
# The leaves from leftmost to rightmost
# The nodes from rightmost left to root

###
# Work
###
# Questions:
# ... Wrrrry?
# Size of tree (assume fits in memory)
# Edge cases:
# -- What about a binary tree with only left nodes, for example?
# Does order matter? (assume yes?)
# I'm assuming we only want each node in the exterior once.

# This feels kind of brute force, but I'm not sure how else to do it.

def tree_exterior(node):
  left = tree_left(node)
  bottom = []
  tree_bottom(node, bottom)
  right = tree_right(node)
  node_set = set()
  exterior = []
  for node_list in (left, bottom, right):
    for n in node_list:
      if n in node_set: continue
      exterior.append(n)
      node_set.add(n)
  return exterior

def tree_left(node):
  result = []
  current = node
  while current:
    result.append(current)
    if current.left:
      current = current.left
    elif current.right:
      current = current.right
    else:
      current = None
  return result

def tree_right(node):
  result = []
  current = node
  while current:
    result.append(current)
    if current.right:
      current = current.right
    elif current.left:
      current = current.left
    else:
      current = None
  result.reverse()
  return result

def tree_bottom(node, leaves=None):
  if leaves is None:
    raise ValueError("Must pass a leaves_list")
  if not node.left and not node.right:
    leaves.append(node)
    return
  if node.left:
    tree_bottom(node.left, leaves)
  if node.right:
    tree_bottom(node.right, leaves)

# Tests:
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
ext = tree_exterior(a)
for node in ext:
  print node.value

a = BinaryTree("a")
b = BinaryTree("b")
c = BinaryTree("c")
d = BinaryTree("d")
e = BinaryTree("e")
f = BinaryTree("f")
g = BinaryTree("g")
h = BinaryTree("h")
i = BinaryTree("i")
j = BinaryTree("j")
k = BinaryTree("k")
l = BinaryTree("l")
m = BinaryTree("m")
n = BinaryTree("n")
o = BinaryTree("o")
p = BinaryTree("p")
a.left = b
a.right = i
b.left = c
b.right = f
c.left = d
c.right = e
f.right = g
g.left = h
i.left = j
i.right = o
j.right = k
k.left = l
k.right = n
l.right = m
o.right = p
print
ext = tree_exterior(a)
for node in ext:
  print node.value,

# Time: 22 minutes

###
# Mistakes / Bugs / Misses
###
# Had current instead of result at 42, 55
# Had leaves_list instead of leaves at 64
# Had node instead of current at 42, 55
# Forgot to reverse result of right side.



