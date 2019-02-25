###
# Problem
###

# Reverse the bits in a 64 bit word.

###
# Work
###
# Questions:
# Are we doing this a lot? (i.e. caching solutions. Assuming no)
# Assuming each number is 64-bit? (Yes. Could use bit_length otherwise)
# Assuming number is positive? (Yes, since Python)

def reverse_bits(n):
  result = 0
  for i in xrange(64):
    next_bit = n & 1
    n >>= 1
    result = (result << 1) | next_bit
  return result

# Tests

num = 0xAAAAAAAAAAAAAAAA
print bin(reverse_bits(num) & 0xFFFFFFFFFFFFFFFF), "010101..."
num = 0x5555555555555555
print bin(reverse_bits(num) & 0xFFFFFFFFFFFFFFFF), "101010..."
num = 0x9999999999999999
print bin(reverse_bits(num) & 0xFFFFFFFFFFFFFFFF), "1001..."

# Time: 10 minutes

###
# Mistakes / Bugs / Misses
###
