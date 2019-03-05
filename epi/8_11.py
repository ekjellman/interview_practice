###
# Problem
###

# Given a linked list like:

# 0123456789

# Merge them even nodes first, then odd nodes
# 0246813579

###
# Work
###
# Questions
# Length of list, use cases, error cases, etc
# in-place? (assume yes)

from linked_list import ListNode

def even_odd(node):
  even_head = ListNode(0)
  odd_head = ListNode(0)
  even_current = even_head
  odd_current = odd_head
  on_even = True
  current = node
  while current:
    if on_even:
      even_current.next_node = current
      even_current = even_current.next_node
    else:
      odd_current.next_node = current
      odd_current = odd_current.next_node
    on_even = not on_even
    next_node = current.next_node
    current.next_node = None
    current = next_node
    #current, current.next_node = current.next_node, None
  odd_head = odd_head.next_node
  even_head = even_head.next_node
  even_current.next_node = odd_head
  return even_head

# Tests:
a = ListNode.make_list(range(12))
result = even_odd(a)
print result.traversal()

a = ListNode.make_list(range(1))
result = even_odd(a)
print result.traversal()

# Time: 11 minutes

###
# Mistakes / Bugs / Misses
###
# Forgot lines 35 and 42
# Line 39 doesn't work for a reason I don't understand. (TODO: Card)
# Probably something about the assignment order?
# Doesn't work with None as the list.
# Their solution of using a list for the even/odd lists is nice.
# (TODO: card)
