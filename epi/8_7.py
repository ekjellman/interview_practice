###
# Problem
###

# Delete a node in a singly-linked list in O(1) time. You may modify
# the value field, and the node is not the last one in the list.

###
# Work
###
def delete_node(node):
  node.value = node.next_node.value
  node.next_node = node.next_node.next_node

# Tests
from linked_list import ListNode
a = ListNode.make_list(range(10))
node = a.find(6)
delete_node(node)
print a.traversal(), "6 deleted"

# Time: 2 minutes

###
# Mistakes / Bugs / Misses
###
