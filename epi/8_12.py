###
# Problem
###

# Test whether a singly linked list is palindromic

###
# Work
###
# Questions:
# Length of list
# Return type? (Assume boolean)
# Can we destroy the list? (Assume no)
# Can we change the list if we restore it? (Assume yes)

def palindromic(head):
  length = head.length()  # TODO: Make pythonic
  breakpoint = (length / 2) - 1
  front_tail = head
  pos = 0
  while pos < breakpoint:
    front_tail = front_tail.next_node
    pos += 1
  back_head = front_tail.next_node
  front_tail.next_node = None
  reverse_current = reverse(back_head)
  back_head = reverse_current
  current = head
  result = True
  while current and reverse_current:
    if current.value != reverse_current.value:
      result = False
      break
    current = current.next_node
    reverse_current = reverse_current.next_node
  back_head = reverse(back_head)
  front_tail.next_node = back_head
  return result

def reverse(head):
  prev = None
  current = head
  while current:
    next_node = current.next_node
    current.next_node = prev
    prev = current
    current = next_node
  return prev

# Tests:
from linked_list import ListNode

a = ListNode.make_list([1, 2, 3, 4, 3, 2, 1])
print palindromic(a), "True"
print a.traversal()

a = ListNode.make_list([1, 2, 3, 3, 2, 1])
print palindromic(a), "True"
print a.traversal()

a = ListNode.make_list([1, 2, 3, 4, 2, 1])
print palindromic(a), "False"
print a.traversal()

a = ListNode.make_list([1])
print palindromic(a), "True"
print a.traversal()

a = ListNode.make_list([1, 1])
print palindromic(a), "True"
print a.traversal()

a = ListNode.make_list([1, 2])
print palindromic(a), "False"
print a.traversal()
# Time: 23 minutes

###
# Mistakes / Bugs / Misses
###
# Missed colon on 29
# Had "current" at 23 instead of front_tail from a rename
# Added line 26 to store the node to re-reverse later
# Forgot to break the list at 25
# Added "and reverse_current" at line 30 for 1 length case.
