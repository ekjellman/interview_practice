###
# Problem
###

# Given an array with all the numbers from 1 to N, N < 32,000 with possible
# duplicates, print the duplicate elements in the array. You only have 4kb
# memory

###
# Work
###

# It's pretty clear the point of this question is to make a bitvector and
# print whenever there's a duplicate. However, I would bring up that a Python
# instance itself is several MB, and the bitvector itself would probably take
# more than 4KB RAM here. However:

def print_duplicates(numbers):
  # TODO: Error checking
  bitset = 0
  for number in numbers:
    if bitset & (1 << number) != 0:
      print number
    else:
      bitset |= 1 << number

print_duplicates([1, 2, 3, 4, 4, 4, 5, 5, 6, 7, 8, 8])
print "(4, 4, 5, 8)"

# Time: 5 minutes

###
# Mistakes / Bugs / Misses
###
# Didn't ask any questions. I couldn't think of much relevant... I mean, I could
#   do them in order in n passes, for example.

