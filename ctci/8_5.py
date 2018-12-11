###
# Problem
###

# Write a recursive function to multiply two numbers without using the
# * operator. You may use + - and bit shift, but minimize their use.

# Questions:
# Integers? (assuming yes)
# Can I use other bit operations? (assuming no)
# Are the integers negative? (assume no, see below)

###
# Work
###

def is_even(number):
  half = number >> 1
  return half + half == number

def multiply(a, b):
  if a == 0 or b == 0: return 0
  if b == 1: return a
  if a == 1: return b
  # Could use trick to figure out max of a and b, but I'll skip it for now
  if is_even(b):
    return multiply(a << 1, b >> 1)
  else:
    return a + multiply(a << 1, b >> 1)

# Tests
import random
for i in xrange(1000):
  a = random.randint(0, 1000)
  b = random.randint(0, 1000)
  my_answer = multiply(a, b)
  real_answer = a * b
  if my_answer != real_answer:
    print a, b, my_answer, real_answer

# Time: 10 minutes

###
# Mistakes / Bugs / Misses
###
# Should have asked about size of a and b (recursion depth)
# Forgot about 0 case. This reminded me of negative case
# If the numbers are negative this approach doesn't work. We would need to
# add checking for negative numbers and keep track of the parity to return
# the correct sign at the end. The problem is that checking for a < 0 is
# somewhat complicated if we're not allowed to use <. There's a bit-shifting
# trick to do it but I can't recall it off the top of my head. TODO: make card?

