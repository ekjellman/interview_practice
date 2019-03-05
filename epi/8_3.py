###
# Problem
###

# Given a Linked List, and two integers s and f, reverse the portion of
# the linked list starting at the sth node (1-indexed) and ending at the
# fth node.

###
# Work
###
# Questions:
# Error checking? (i.e. are s and f in the list, is s < f, etc)
#   (Assume input is valid

def reverse_sublist(node, s, f):
  pos = 1
  current = node
  prev = None
  while pos < s:   # Error checking
    prev = current
    current = current.next_node
    pos += 1
  pre_list_tail = prev
  head = current
  while pos < f:   # Error checking
    prev = current
    current = current.next_node
    pos += 1
  tail = current
  post_list_head = current.next_node
  tail.next_node = None
  new_head, new_tail = reverse(head)
  if pre_list_tail:
    pre_list_tail.next_node = new_head
    result = node
  else:
    result = new_head
  new_tail.next_node = post_list_head
  return result

def reverse(node):
  current = node
  previous = None
  while current:
    next_node = current.next_node
    current.next_node = previous
    previous = current
    current = next_node
  return (previous, node)

# Test
from linked_list import ListNode
a = ListNode.make_list([1, 2, 3, 4, 5])
result = reverse_sublist(a, 2, 4)
print result.traversal(), 14325

a = ListNode.make_list([1, 2, 3, 4, 5])
result = reverse_sublist(a, 2, 5)
print result.traversal(), 15432

a = ListNode.make_list([1, 2, 3, 4, 5])
result = reverse_sublist(a, 1, 5)
print result.traversal(), 54321

# Time: 17 minutes

###
# Mistakes / Bugs / Misses
###
# Forgot pos += 1 lines.
# (1, 5) test did not work because I was not returning the new head, and
#   because pre_list_tail was None
# Their approach of just starting reversing at the correct element and
#   stopping at the correct element is nice. (TODO: make card)
