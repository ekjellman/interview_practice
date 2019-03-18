###
# Problem
###

# Make a linked list from the leaves of a binary tree. The leaves
# should appear in left-to-right order

###
# Work
###
# Questions:
# Size of the tree, use cases, etc
# What are we looking at for the return type here? A linked list
# where the values are tree nodes? (Assume yes)

from linked_list import ListNode

def leaves_list(node):
  head = ListNode(0)
  ll_helper(node, head)
  return head.next_node

def ll_helper(node, tail):
  if not node.left and not node.right:
    new_node = ListNode(node)
    tail.next_node = new_node
    return new_node
  else:
    if node.left:
      tail = ll_helper(node.left, tail)
    if node.right:
      tail = ll_helper(node.right, tail)
  return tail

# Test:
from binary_tree import BinaryTree
a = BinaryTree("A")
b = BinaryTree("B")
c = BinaryTree("C")
d = BinaryTree("D")
e = BinaryTree("E")
f = BinaryTree("F")
g = BinaryTree("G")
h = BinaryTree("H")
i = BinaryTree("I")
a.left = b
a.right = c
b.left = d
b.right = e
e.left = h
c.left = f
c.right = g
g.right = i

ll = leaves_list(a)
current = ll
while current:
  print current.value.value
  current = current.next_node

# Time:

###
# Mistakes / Bugs / Misses
###
# I need to think about what an actual, useful LinkedList data
# structure looks like when I'm doing these problems. For example,
# here I had to have the helper return the tail, because I
# was dealing with the structure I created for linked list problems.
# But in reality, and in an interview, a problem like this that
# is focusing in the binary tree won't care if I use a real
# linked list implementation like collections.deque. So do that.
# TODO: make a card, somehow?
