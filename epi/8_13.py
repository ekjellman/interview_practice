###
# Problem
###

# Implement list pivoting on a singly-linked list.
# The pivot should be stable.

###
# Work
###
# Questions:
# Size of the list
# Destroy original list? (Assume yes)
# O(1) space? (Assume yes)

from linked_list import ListNode

def pivot(head, k):
  less = ListNode(0)
  equal = ListNode(0)
  more = ListNode(0)
  less_head, equal_head, more_head = less, equal, more

  current = head
  while current:
    next_node = current.next_node
    current.next_node = None
    # Could do voodoo to make [equal, more, less] list, but this is clearer
    if current.value == k:
      equal.next_node = current
      equal = equal.next_node
    elif current.value > k:
      more.next_node = current
      more = more.next_node
    else:
      less.next_node = current
      less = less.next_node
    current = next_node
  less.next_node = equal_head.next_node
  equal.next_node = more_head.next_node
  return less_head.next_node

# Tests:
a = ListNode.make_list([1, 2, 3, 1, 2, 3, 1, 2, 3])
b = pivot(a, 2)
print b.traversal()

a = ListNode.make_list([2, 2, 2, 3, 2, 2])
b = pivot(a, 2)
print b.traversal()

a = ListNode.make_list([1, 1, 1, 1, 1, 2, 1, 1, 1])
b = pivot(a, 2)
print b.traversal()

a = ListNode.make_list([1])
b = pivot(a, 2)
print b.traversal()

# Time: 12 minutes

###
# Mistakes / Bugs / Misses
###
# Forgot to progress to next node after adding current to appropriate list
# had more instead of more_head at 40
