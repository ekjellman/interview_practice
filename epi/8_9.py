###
# Problem
###

# Given a linked list with sorted values, remove duplicate values

###
# Work
###
# Questions:
# Length of list
# Return type (assume none)

def remove_dupes(node):
  current = node
  while current:
    succ = current.next_node
    while succ and succ.value == current.value:
      succ = succ.next_node
    current.next_node = succ
    current = succ

# Tests:
from linked_list import ListNode
a = ListNode.make_list(range(10))
remove_dupes(a)
print a.traversal()

a = ListNode.make_list([0, 1, 1, 1, 2, 2, 3, 4, 5, 5, 5, 5, 6, 6])
remove_dupes(a)
print a.traversal()

# Time: 4 minutes

###
# Mistakes / Bugs / Misses
###
# Forgot colon on line 14
