###
# Problem
###

# Given an integer where you can flip exactly one bit from 0 to 1, write code
# to find the length of the longest sequences of 1s you can create

###
# Work
###
# Questions:
# Do we have to flip a one? (Assume no)
# Can we assume the integer is positive? (Assume yes, due to Python wackiness)
# -- If we couldn't, we'd ask whether to use sign magnitude or two's complement

def flip_to_win(num):
  prev = 0
  curr = 0
  found_zero = 0
  best = 0
  while num > 0:
    bit = num & 1
    if bit == 1:
      curr += 1
    if bit == 0:
      found_zero = 1
      best = max(best, curr + prev + found_zero)
      prev = curr
      curr = 0
    num >>= 1
  best = max(best, curr + prev + found_zero)
  return best

print "8", flip_to_win(1775)
print "5", flip_to_win(31)
print "0", flip_to_win(0)  # ?
print "7", flip_to_win(0b1111110011011011)
print "8", flip_to_win(0b11011101111011)



# Time: 11 minutes

###
# Mistakes / Bugs / Misses
###
# Forgot to shift over the number (line 28)
# Forgot to add the zero we flip, which led to another bug, in the 31 case.
