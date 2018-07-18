import linked_list

###
# Problem
###

# Write a function to check if a linked list is a palindrome

###
# Work
###

# Questions:
# Is O(n) space ok? (See approaches below)
# Singly linked list? (Assume yes)

# Approaches:
# I don't see how to do this in O(n) time and O(1) space. I can see a few
# O(n) time and O(n) space approaches:
# -- Simplest is to shuffle the items into a more convenient list
# -- If we are following the spirit of the problem, we could copy the list and
#    then reverse it, and traverse both. This takes O(n) space for the copy
# -- We could use recursion / generators, and "traverse" from the end of the
#    list using the generator. This takes O(n) space on the stack.
# -- We could use slightly less space by making a copy of the second half of the
#    list and reversing and traversing that. That still takes O(n) time and
#    space, but it's halved at least.
# I'll implement the copy/reverse, and see what she says about it.

def is_palindrome(ll):
  list_copy = linked_list.LinkedList()
  current = ll.head
  while current is not None:
    list_copy.add(current.value)
    current = current.next
  reverse_linked_list(list_copy)
  list_current = ll.head
  reverse_current = list_copy.head
  while list_current is not None:
    if list_current.value != reverse_current.value:
      return False
    list_current = list_current.next
    reverse_current = reverse_current.next
  return True

def reverse_linked_list(ll): # I should just memorize this. >_<
  current = ll.head
  previous = None
  next_node = current.next
  while current is not None:
    current.next = previous
    previous = current
    current = next_node
    if current is not None:
      next_node = current.next
  ll.head, ll.tail = ll.tail, ll.head

test_list = linked_list.LinkedList()
test_list.add(1)
test_list.add(2)
test_list.add(3)
test_list.add(4)
test_list.add(5)
test_list.print_list()
reverse_linked_list(test_list)
test_list.print_list()

print is_palindrome(test_list)  # False

test_list = linked_list.LinkedList()
test_list.add(1)
test_list.add(2)
test_list.add(3)
test_list.add(2)
test_list.add(1)
test_list.print_list()
print is_palindrome(test_list)  # True

test_list = linked_list.LinkedList()
test_list.add(1)
test_list.add(2)
test_list.add(3)
test_list.add(3)
test_list.add(2)
test_list.add(1)
test_list.print_list()
print is_palindrome(test_list)  # True

test_list = linked_list.LinkedList()
test_list.add(1)
test_list.add(2)
test_list.add(3)
test_list.add(4)
test_list.add(2)
test_list.add(1)
test_list.print_list()
print is_palindrome(test_list)  # False

# Time: 17 minutes

###
# Mistakes / Bugs / Misses
###
# Missed case at 54 for reverse
# Did not think about the stack approach
# Did not think about the fast/slow runner approach for getting half the list
# 
