###
# Problem
###

# Write a method to insert M into bit positions j through i.

# EX: n = 100000000000  m = 10011  i = 2  j = 6
# Output: n = 10001001100
#                 -----

# You can assume that bits j through i have enough space for all of m

###
# Work
###
# Questions:
# What if m is smaller than the space we have? (assume 0-pad)
# Can we assume valid input? i.e., j is greater than i, etc. (assume yes)
# Can we assume n will be long enough for j? (assume yes)
# Do we overwrite bits in n / can we assume they're zeros? (assume zeros)

def insert_bits(n, m, i, j):
  return n | (m << i)

print bin(insert_bits(0b10000000000, 0b10011, 2, 6))

# Time: 20 minutes (failed)

###
# Mistakes / Bugs / Misses
###
# Started to read solution, realized that they were not assuming zeros.
# REDO
# Make card for zeroing out bits in Python.
