import linked_list

###
# Problem
###

# Take two linked list representations of numbers in reverse order and add them
# into another linked list

# Example:
# 3 -> 2 -> 1  (123)
# 5 -> 4 -> 6  (645)
# Output: 8 -> 6 -> 7 (768)

###
# Work
###

# Questions:
# Should I do input validation? (particularly nodes that aren't single digits)
# (Assume no)

def add(a, b):
  current_a = a.head
  current_b = b.head
  result = linked_list.LinkedList()
  carry = 0
  while current_a is not None or current_b is not None or carry > 0:
    if current_a is not None:
      a_digit = current_a.value
      current_a = current_a.next
    else:
      a_digit = 0
    if current_b is not None:
      b_digit = current_b.value
      current_b = current_b.next
    else:
      b_digit = 0
    new_digit = a_digit + b_digit + carry
    result.add(new_digit % 10)
    carry = new_digit / 10
  return result

a = linked_list.LinkedList()
a.add(9)
a.add(9)
a.add(9)
b = linked_list.LinkedList()
b.add(0)
b.add(9)
b.add(9)
b.add(8)
b.add(9)
c = add(a, b)
c.print_list()

# For the follow up, reverse the lists first.
# The book gives a solution with padding zeros onto the shorter list and
# implementing a partial sum, but reversing is still O(n)

# Time: 9 minutes

###
# Mistakes / Bugs / Misses
###
# line 36 had a copy/paste error (current_a = current_a.next)
# Didn't implement recursively. I guess. I don't think the recursive solution
# is superior.
