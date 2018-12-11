###
# Problem
###

# A magic index in an array A is one such that A[i] = i. Given a sorted
# array of distinct integers, write a method to find a magic index if one
# exists.

# Questions:
# Size of array?
# What should we do with an empty list?

###
# Work
###

def find_magic_index(a):
  if not a: return None
  low = 0
  high = len(a) - 1
  while high >= low:  # ?
    mid = (high + low) / 2
    if a[mid] == mid:
      return mid
    elif a[mid] > mid:
      high = mid - 1
    else:
      low = mid + 1
  return None

# Tests:
print find_magic_index([-1, 0, 1, 2, 3, 5, 7, 8, 9]), "5"
print find_magic_index([0]), "0"
print find_magic_index([]), "None"
print find_magic_index([0, 2, 3, 4, 5, 6]), "0"
print find_magic_index([-1, 0, 1, 2, 3, 4, 5, 6, 7, 9]), "9"
print find_magic_index([-2, -1, 0, 1, 2, 3, 40, 41, 42, 43]), "None"
# Could write something that generates random tests with a slower O(n)
# checker to really verify things

# Time: 13 minutes

###
# Mistakes / Bugs / Misses
###
# None?
# It took me a while to work out the end condition at line 21, so I should
# make a card for that.
# Probably "a" should be "array", or a better Pythonic name.

# Oops, actually, didn't mention the duplicates follow up.
