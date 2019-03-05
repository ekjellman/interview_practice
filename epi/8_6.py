###
# Problem
###

# Given two linked lists, if the two lists merge, return the first
# node encountered while traversing the two lists that is in both
# lists. The lists may have cycles, and you can return either first
# node (depending on which list you start with)

###
# Work
###
# Questions:
# ... really.
# ... lengths of lists, can we use a set, etc etc etc

# I'm gonna go with brute force.

def overlap(a, b):
  node_set = set()
  current = a
  while current:
    if current in node_set: break
    node_set.add(current)
    current = current.next_node
  current = b
  while current:
    if current in node_set: return current
    current = current.next_node
  return None

# Tests
from linked_list import ListNode
a = ListNode.make_list(range(8))
loop = a.find(3)
end = a.find(7)
end.next_node = loop
b = ListNode.make_list(range(5))
end = b.find(4)
end.next_node = loop
result = overlap(a, b)
print result == loop, result, loop

# Time: 8 minutes

###
# Mistakes / Bugs / Misses
###
# It took a few minutes to make my brain even engage with this
# question, tbh.
# Make a card for the O(1) space solution (TODO)
