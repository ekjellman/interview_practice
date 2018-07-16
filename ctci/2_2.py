import linked_list

###
# Problem
###

# Find the kth to last element of a singly linked list

###
# Work
###

# Questions:
# What is the last element of the list? k = 0, or k = 1? (assume k = 0)
# What is the return type? the node, or the value? (Assume value)
# What should we do if k is too large? (Return an error)

def find_k_to_last(ll, k):
  if k < 0:
    raise ValueError("k must be 0 or greater")
  # Get length of list
  length = 0
  current = ll.head
  while current is not None:
    length += 1
    current = current.next

  if k + 1 > length:
    raise ValueError("k is too large for this list")

  advances = length - k - 1
  current = ll.head
  while advances > 0:
    assert current is not None
    current = current.next
    advances -= 1
  return current.value

test_list = linked_list.LinkedList()
test_list.add(8)
test_list.add(7)
test_list.add(6)
test_list.add(5)
test_list.add(4)
test_list.add(3)
test_list.add(2)
test_list.add(1)
test_list.add(0)

print find_k_to_last(test_list, 0)
print find_k_to_last(test_list, 3)
print find_k_to_last(test_list, 8)
try:
  print find_k_to_last(test_list, -1), "whoops"
except ValueError:
  print "correctly caught error for -1"
try:
  print find_k_to_last(test_list, 9), "whoops"
except ValueError:
  print "correctly caught error for 9"

# Note: There is an alternate solution where you advance a leader node k
#       nodes, then run current and the leader ahead until the leader hits
#       the end of the list. I don't believe this solution is better in the
#       general case. In specific cases, it might be worth doing with testing.

# Time: 12 minutes

###
# Mistakes / Bugs / Misses
###
# -- Did not think of return type question before implementing.
# -- Did not think of k > length of list question until implementing tests.
