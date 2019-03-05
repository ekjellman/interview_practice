###
# Problem
###

# Given the head of a linked list, determine if there is a cycle. If there
# is, return the start of the cycle. If not, return None.

###
# Work
###
# Questions:
# Length of list
# Can I use a set? (assume no)
# Why does your linked list have cycles, anyway.

def cycle_test(head):
  fast = head
  slow = head
  while True:
    slow = slow.next_node
    fast = fast.next_node
    if fast: fast = fast.next_node
    if not fast: return None
    if slow == fast: break
  fast = head
  while fast != slow:
    slow = slow.next_node
    fast = fast.next_node
  return fast

# Test:
from linked_list import ListNode
ll = ListNode.make_list([1, 2, 3, 4, 5, 6, 7, 8])
start = ll.find(3)
end = ll.find(8)
end.next_node = start
result = cycle_test(ll)
print result == start, result, start

ll = ListNode.make_list(range(15))
start = ll.find(6)
end = ll.find(14)
end.next_node = start
result = cycle_test(ll)
print result == start, result, start

ll = ListNode.make_list(range(15))
result = cycle_test(ll)
print result, "None"

# Time: 10 minutes

###
# Mistakes / Bugs / Misses
###
# Made some mistakes making find(), which I wrote for this problem's tests
