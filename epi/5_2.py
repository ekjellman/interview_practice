###
# Problem
###

# Swap two given bits in a given number. (Assume it's 64 bit)

###
# Work
###
# Questions:
# Can we assume the numbers are positive, since it's Python? (Yes, we're
#   them as a bitvector)

def swap_bits(num, a, b):
  a_value = num & (1 << a)
  b_value = num & (1 << b)
  if a_value == b_value: return num
  if a_value != 0:
    num -= a_value    # Don't rememeber how to clear
    num |= 1 << b
  else:
    num -= b_value
    num |= 1 << a
  return num

# Tests:
num = 0b10110101
print bin(swap_bits(num, 0, 3)), "0b10111100"
num = 0b10110101
print bin(swap_bits(num, 1, 5)), "0b10010111"
num = 0b10101010
print bin(swap_bits(num, 0, 4)), "0b10101010"
num = 0b10101010
print bin(swap_bits(num, 1, 5)), "0b10101010"

# Time: 11 minutes

###
# Mistakes / Bugs / Misses
###
# Didn't remember how to clear a bit.
# Line 23 had b instead of a
# Didn't think of using XOR for a bit flip. TODO: card
# Checking a bit using >> is also interesting
