###
# Problem
###

# Given a list of numbers, positive and negative, find the contiguous sequence
# with the largest sum and output the sum.

###
# Work
###
# Questions:
# Size of n?
# What if there are no numbers? (Assume there are numbers, although 0 is fine)
# What if there are all negative numbers? (Return 0, for an empty sequence)

def lcs(numbers):
  best = 0
  current = 0
  for number in numbers:
    current += number
    if current < 0:
      if current - number > best:
        best = current - number
      current = 0
  return max(best, current)

# Tests
print lcs((2, -8, 3, -2, 4, -10)), "5"
print lcs((-1, -2, -3, -4)), "0"
print lcs(()), "0"
print lcs((-1, 2, 2, 2)), "6"

# Time: 5 minutes

###
# Mistakes / Bugs / Misses
###
# Use max at 22-23
