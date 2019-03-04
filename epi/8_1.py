###
# Problem
###

# Take two linked lists, each assumed to have sorted data, and merge them into
# one sorted list. You may only change the next field of any particular node.

###
# Work
###
# Questions:
# Use cases / size / generic questions
# Destroying a and b? (Assume yes)

def merge(a, b):
  result = None
  head = None
  while a and b:
    if a.value < b.value:
      next_node = a
      a = a.next_node
    else:
      next_node = b
      b = b.next_node
    if result is None:
      result = next_node
      head = next_node
    else:
      result.next_node = next_node
      result = result.next_node
  if a:
    result.next_node = a
  elif b:
    result.next_node = b
  else:
    result.next_node = None
  return head

# Tests
from linked_list import ListNode
a = ListNode(2)
a.next_node = ListNode(5)
a.next_node.next_node = ListNode(7)
b = ListNode(3)
b.next_node = ListNode(11)
r = merge(a, b)
print r.traversal()

# Time: 15 minutes

###
# Mistakes / Bugs / Misses
###
# Spent a long time looking for a bug here, when it was a bug in my library code.

