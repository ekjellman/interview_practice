###
# Problem
###

# Find out if two lists have a common node (i.e. they merge)

###
# Work
###
# Questions
# Lengths of lists
# Return type (says "if", so assuming boolean)

def merges(a, b):
  a_len, b_len = length(a), length(b)
  if a_len > b_len:
    a_len, b_len = b_len, a_len
    a, b = b, a
  diff = b_len - a_len
  a_pointer, b_pointer = a, b
  for _ in xrange(diff):
    b_pointer = b_pointer.next_node
  while b_pointer:
    if a_pointer == b_pointer: return True
    a_pointer, b_pointer = a_pointer.next_node, b_pointer.next_node
  return False

def length(node):
  if node is None: return 0
  result = 0
  current = node
  while current:
    current = current.next_node
    result += 1
  return result

# Tests:
from linked_list import ListNode
a = ListNode.make_list(range(15))
b = ListNode.make_list(range(6))
b_end = b.find(5)
a_mid = a.find(7)
b_end.next_node = a_mid
print "True", merges(a, b)

a = ListNode.make_list(range(15))
b = ListNode.make_list(range(6))
print "False", merges(a, b)

a = ListNode.make_list(range(15))
b = ListNode.make_list(range(6))
b_end = b.find(5)
a_mid = a.find(14)
b_end.next_node = a_mid
print "True", merges(a, b)

a = ListNode.make_list(range(1))
print "True", merges(a, a)
# Time: 10 minutes

###
# Mistakes / Bugs / Misses
###

