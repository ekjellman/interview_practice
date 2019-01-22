###
# Problem
###

# A Listy data structure has no len() function, but has a get(i) function that
# returns either the element at index i in o(1), or returns -1 if the element
# does not exist (and so a Listy only contains positive elements). Given a Listy
# with sorted positive integers, find the index at which an element x occurs.
# If x occurs multiple times, return any of them.

###
# Work
###

# Questions:
# Possible maximum size of the listy? (could binary search over that)
# Ascending order?
# What if the element is not in the Listy? (return -1)
# Python note: a Listy could return None instead in Python.

class Listy(object):
  def __init__(self, my_list):
    self._list = my_list

  def get(self, i):
    # TODO: Error checking
    if i >= len(self._list):
      return -1
    return self._list[i]

def find_element(element, listy):
  # Note: If we were implementing the Listy, we'd make this a function of Listy
  # TODO: Error checking (-1 in particular)
  high = 1
  while listy.get(high) != -1 and listy.get(high) < element:
    high *= 2
  low = high / 2
  while high >= low:
    mid = (high + low) / 2
    # Could store listy.get(mid)
    if listy.get(mid) == element: return mid
    elif listy.get(mid) == -1 or listy.get(mid) > element:
      high = mid - 1
    else:
      low = mid + 1
  return -1

# Tests
listy = Listy([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
for i in xrange(10):
  print i, find_element(i, listy)
print "-1", find_element(15, listy)
listy = Listy([0, 1, 2, 3, 5, 6, 7, 8, 9])
print "-1", find_element(4, listy)

# Time: 14 minutes

###
# Mistakes / Bugs / Misses
###
# Didn't think about the item not being in the listy until after coding start
# Had > instead of >= in line 27
