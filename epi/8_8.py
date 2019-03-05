###
# Problem
###

# Remove the kth-to-last element from a linked list
# you cannot record the length of the list, because reasons

###
# Work
###
# Questions:
# ... REALLY.

def remove_kth_last(node, k):
  # TODO: error checking
  back = node
  front = node
  while k > 0:
    k -= 1
    front = front.next_node
  while front:
    front = front.next_node
    back = back.next_node
  # Probably a bug. Probably I'm supposed to keep prev around.
  back.value = back.next_node.value
  back.next_node = back.next_node.next_node

# Test
from linked_list import ListNode
a = ListNode.make_list(range(10))
remove_kth_last(a, 3)
print a.traversal()   # removes 7

# Time: 7 minutes

###
# Mistakes / Bugs / Misses
###
# While I hate this question and everything it stands for, I need to
# remember to delete a node just using node.next.next, and not muck
# with the values (TODO: make card)
