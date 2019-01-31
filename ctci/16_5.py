###
# Problem
###

# Write an algorithm which computes the number of trailing zeros in
# n factorial

###
# Work
###
# Questions:
# How to deal with invalid n? (Assume n is valid)

def trailing_zeros(n):
  total = 0
  while n >= 5:
    total += n/5
    n /= 5
  return total

# Tests
import math
def count_zeros(n):
  f = math.factorial(n)
  s = str(f)
  for pos in xrange(-1, -len(s) - 1, -1):
    if s[pos] != "0":
      return -(pos) - 1

for i in xrange(1000):
  if count_zeros(i) != trailing_zeros(i):
    print i, count_zeros(i), trailing_zeros(i)

# Time: 8 minutes

###
# Mistakes / Bugs / Misses
###
# Had while n > 5 in line 16
# Off by one error in line 26 (-len(s) instead of -len(s) - 1)
# had 0 instead of "0" in line 27
