###
# Problem
###

# Compute the LCA of two nodes in a binary tree

###
# Work
###
# Questions: size of tree, use cases, etc etc
# Return type? (Assume node)

def lca(node, m, n):
  m_path = find(node, m)
  n_path = find(node, n)
  if not m_path or not n_path: return None
  lca = None
  for i in xrange(len(m_path)):
    if m_path[i] == n_path[i]:
      lca = m_path[i]
    else:
      break
  return lca

def find(node, m, path=None):
  if not node:
    return None
  if not path:
    path = []
  new_path = path + [node]
  if node == m:
    return path
  else:
    r_find = find(node.right, m, new_path)
    if r_find: return r_find
    l_find = find(node.left, m, new_path)
    if l_find: return l_find
  return None

# Tests:
from binary_tree import BinaryTree
a = BinaryTree("a")
b = BinaryTree("b")
c = BinaryTree("c")
d = BinaryTree("d")
e = BinaryTree("e")
f = BinaryTree("f")
g = BinaryTree("g")
h = BinaryTree("h")
i = BinaryTree("i")

a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
c.right = g
f.left = h
f.right = i

print "C", lca(a, g, i).value
print "A", lca(a, b, g).value
print "F", lca(a, h, i).value
j = BinaryTree("j")
print "None", lca(a, h, j)

# Time: 15 minutes

###
# Mistakes / Bugs / Misses
###
# Had = instead of == at 19
# Started to do wind/unwind, but I don't have the brains for it right
#   now, so I just copied the list
# Had m and n instead of m_path and n_path at 16
# TODO: Make card about better approach, if I don't have one already
