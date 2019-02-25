###
# Problem
###

# The weight of a number is the number of bits set to 1 in its binary rep.
# Given a non-negative number x, return a number y which is not equal to x
# but with the same weight, with |y - x| as small as possible
# Assume the number is not all 0s or all 1s

###
# Work
###
# Questions:
# Assume a fixed bit-length? (Let's say no)

def closest_number(n):
  pos = 0
  while (n >> pos) & 1 == (n >> (pos + 1)) & 1:
    pos += 1
  n ^= (0b11 << pos)
  return n

# Tests
n = 0b100101101
print bin(closest_number(n)), "100101110"
n = 0b111101111
print bin(closest_number(n)), "111110111"
n = 6
print bin(closest_number(n)), "101"

# Time: 8 minutes

###
# Mistakes / Bugs / Misses
###
# Seems correct
