###
# Problem
###

# You are given an array with all the numbers from 1 to N appearing exactly once
# except for one number that is missing. How can you find the missing number
# in O(N) time and O(1) space?

###
# Work
###
# Questions:
# Size of numbers?
# In non-Python contexts, overflow?
# Missing how? (Assume just not in the list)

def missing_one(numbers):
  # +2 because we're missing one number, and xrange doesn't include the last
  # This is still O(n), but I could use a formula for the first part
  # TODO: Error checking? (numbers not as expected)
  return sum(xrange(1, len(numbers) + 2)) - sum(numbers)

# Test
print missing_one((1, 2, 3, 5, 6, 7, 8)), 4
print missing_one(()), 1
print missing_one((1, 2, 3, 4, 5, 6, 7, 8, 9)), 10
print missing_one((1, 9, 8, 2, 7, 4, 6, 5)), 3

# Follow up: What if there are two numbers missing?
# Questions:
# Can I modify the list? (Then I could sort them in O(n) time because bucket
#   sort, and then scan for the missing ones

import math
def missing_two(numbers):
  # This is almost certainly not intended
  s = sum(numbers)
  difference = sum(xrange(1, len(numbers) + 3)) - s
  p = reduce(lambda a, b: a * b, numbers) if numbers else 1
  divisor = math.factorial(len(numbers) + 2) / p
  for a in xrange(difference / 2, difference + 1):
    b = difference - a
    if a * b == divisor:
      return a, b

print missing_two((1, 2, 3, 4, 6, 7, 9, 10)), (5, 8)
print missing_two(()), (1, 2)
print missing_two((12, 11, 9, 8, 7, 6, 5, 4, 3, 2)), (10, 1)

# Question: is math.factorial(n) really O(n)? Not reaaaaaaally?

# Last approach I have is to, if we can't modify the list (or at least we can
# only do it temporarily) is to negate an index if the number is in the list,
# and then look for the numbers that aren't negated. We'd need O(1) space for
# the two numbers we don't have space for in the list. We can then set them
# all back to positive.

# Time: 19 minutes.

###
# Mistakes / Bugs / Misses
###
# Did not think of sum of squares, which is nice. Still probably not REALLY
# O(n), but better than my factorial approach
