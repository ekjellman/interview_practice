###
# Problem
###

# Write a program to swap odd and even bits in an integer in as few
# instructions as possible.

###
# Work
###
# Questions:
# Can I assume a 32 bit integer? (Assume yes)
# -- If no, it would take some more work to dynamically construct the bitmasks

def pairwise_swap(num):
  odd_bits = num & 0x55555555  # 0101
  even_bits = num & 0xAAAAAAAA  # 1010
  return (odd_bits << 1) | (even_bits >> 1)

print "9", pairwise_swap(6)  # 0110 -> 1001
print "10", pairwise_swap(5)
print "5", pairwise_swap(10)

# Time: 4 minutes

###
# Mistakes / Bugs / Misses
###
