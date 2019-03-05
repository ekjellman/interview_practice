###
# Problem
###

# Reverse a linked list

###
# Work
###
# Questions
# 1) Really?

def reverse(node):
  prev = None
  current = node
  while current:
    next_node = current.next_node
    current.next_node = prev
    prev = current
    current = next_node
  return prev

# Test:
from linked_list import ListNode
a = ListNode.make_list([1, 2, 3, 4, 5])
a = reverse(a)
print a.traversal()

# Time: 8 minutes (includes making "make_list" method of library)

###
# Mistakes / Bugs / Misses
###
# 18: previous -> prev
# Forgot line 19
# Make a card for this crap I guess (TODO)
