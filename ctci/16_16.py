###
# Problem
###

# Given a list of integers, write a method to find m and n such that if you
# sorted elements m through n, the entire list would be sorted. Minimize
# n - m (to find the smallest subrange)

###
# Work
###
# Length of the list?
# What if the entire list is sorted?
#

def subrange(numbers):
  for i in xrange(len(numbers) - 1):
    if numbers[i + 1] < numbers[i]: break
  else:
    return None
  left_edge = i
  for i in xrange(len(numbers) - 1, 0, -1):
    if numbers[i - 1] > numbers[i]: break
  right_edge = i
  min_unsorted = min(numbers[left_edge + 1:right_edge])
  max_unsorted = max(numbers[left_edge + 1:right_edge])
  left, right = None, None
  for i in xrange(len(numbers)):
    if numbers[i] > min_unsorted:
      left = i
      break
  for i in xrange(len(numbers) - 1, -1, -1):
    if numbers[i] < max_unsorted:
      right = i
      break
  return left, right

# Tests
print subrange((1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19)), (3, 9)

# Time: 15 minutes (FAILED)

###
# Mistakes / Bugs / Misses
###
# Forgot closing parens on 25, 26
# Used len(numbers) instead of len(numbers) - 1 at 22, 32
