###
# Problem
###

# Cyclically shift a linked-list right k node

###
# Work
###
# Questions
# Length of list, use cases, etc etc
# is k valid? (assume yes, and less than the length of the list)
# return type? (new head)

def cyclic_shift(node, k):
  # TODO: error checking
  if k == 0: return
  # Might as well use the "clever" solution
  back = node
  front = node
  for _ in range(k):
    front = front.next_node
  while front.next_node:
    back = back.next_node
    front = front.next_node
  new_head = back.next_node
  back.next_node = None
  front.next_node = node
  return new_head

# Tests:
from linked_list import ListNode
a = ListNode.make_list(range(8))
b = cyclic_shift(a, 3)
print b.traversal(), "56701234"

# Time: 11 minutes

###
# Mistakes / Bugs / Misses
###
# screwed up doing the back/front pointers in the first loop
# line 28 had front.next_node = new_head, instead of node

