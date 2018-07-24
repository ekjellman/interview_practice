###
# Problem
###

# Determine how many bits you would need to flip to an integer to another.

# Ex: 29 (11101), 15 (01111)

# 11101
# 01111
# 2 bits are different, so the answer is 2

###
# Work
###
# Questions: Do I have to handle negative numbers? (Assume no, Python wackiness)
# -- As before, if I do, ask about sign magnitude or two's complement

def conversion(a, b):
  convert_bits = a ^ b
  count = 0
  while convert_bits != 0:   # Does not work with negative numbers in Python
    count += 1
    convert_bits &= (convert_bits - 1)
  return count

print conversion(29, 15), "2"
print conversion(0b111000, 0b000111), "6"
print conversion(31, 31), "0"

# Time: 4 minutes

###
# Mistakes / Bugs / Misses
###

