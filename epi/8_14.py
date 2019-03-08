###
# Problem
###

# Given two linked lists that represent an integer in reversed order:
# 3 -> 1 -> 4 -> None = 413

# Return a list corresponding to their sum.

###
# Work
###
# Questions:
# Size of lists?
# Can we convert to an int first? (Assume no)
# Use cases
# Leading zeros? (Assume no)
# Assuming valid input
from linked_list import ListNode

def add(a, b):
  result = ListNode(0)
  result_head = result
  carry = 0

  while a or b or carry:
    a_digit = a.value if a else 0
    b_digit = b.value if b else 0
    a = a.next_node if a else None
    b = b.next_node if b else None
    digit_sum = a_digit + b_digit + carry
    new_digit = digit_sum % 10
    carry = digit_sum / 10
    result.next_node = ListNode(new_digit)
    result = result.next_node

  return result_head.next_node

# Tests:
a = ListNode.make_list([3, 1, 4])
b = ListNode.make_list([7, 0, 9])
result = add(a, b)
print result.traversal(), [0, 2, 3, 1]


a = ListNode.make_list([9, 9, 9, 9, 9, 9, 9])
b = ListNode.make_list([1])
result = add(a, b)
print result.traversal(), [0, 0, 0, 0, 0, 0, 0, 1]

b = ListNode.make_list([9, 9, 9, 9, 9, 9, 9])
a = ListNode.make_list([1])
result = add(a, b)
print result.traversal(), [0, 0, 0, 0, 0, 0, 0, 1]

b = ListNode.make_list([0])
a = ListNode.make_list([0])
result = add(a, b)
print result.traversal(), [0]

# Time: 10 minutes

###
# Mistakes / Bugs / Misses
###
# Make sure I have a card for this technique of having a dummy node
# at the front of a new list (TODO: card)
