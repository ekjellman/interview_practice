###
# Problem
###

# Write a function that adds two numbers. You should not use + or any
# arithmetic operators.

###
# Work
###
# It's hard to know what approach to go for without an interviewer. >_<
# Questions:
# How are the numbers given to us? (Assume as numbers)
# Can I use bit operations? (Assume yes, more in a moment)
# Error checking questions (overflow? / invalid inputs / etc) (Ignoring)
# Negative numbers? (assume no, although this might be lazy)

# I can think of two general approaches.
# -- Convert to a string (or handle digit by digit) and simulate addition using
#    a function with a lookup table.
# -- Binary

# I'm going to go with binary

def add(a, b):
  result = 0
  carry_digit = 0
  current_digit = 1
  while a or b:
    a_digit = a & 1
    b_digit = b & 1
    new_digit = a_digit ^ b_digit
    new_carry = a_digit & b_digit
    """
    if new_digit:  # only one of a and b digits
      new_digit ^= carry_digit
      new_carry = new_digit & carry_digit
    else: # 0 or 2
      new_digit ^= carry_digit
      new_carry = new_carry
    """
    if new_digit:
      new_carry = new_digit & carry_digit  # TODO: Get rid of if
    new_digit ^= carry_digit
    if new_digit:
      result |= current_digit
    current_digit <<= 1
    carry_digit = new_carry
    a >>= 1
    b >>= 1
  if carry_digit:
    result |= current_digit
  return result

# Test:
import random
print add(15, 18), 33
print add(0, 0), 0
for _ in xrange(20):
  a = random.randint(0, 1000000000)
  b = random.randint(0, 1000000000)
  print add(a, b), a + b

# Time: 24 minutes

###
# Mistakes / Bugs / Misses
###
# Line 44 was before the preceding if, which was an error
# Her solution is much more elegant, and I'm not sure I fully understand it.
# I think it's something like this:
# You have two numbers, and you separate out the adding from the carrying:

#        000010  (Carry, a&b)
#
#        100110  (38)
#      + 001010  (8)
#        ------
#        101100  (add, a^b)

# Then, the carry part can be shifted over 1 (since it's basically saying "add
# me one digit over"), and you start over with this new problem:

#       101100 (44)
#     + 000100 (4)

# Eventually you will run out of carry (since it keeps shifting left) and when
# you do, you have the answer.

# This is more efficient than my solution, but I'm not sure I could have come
# up with it. Regardless: TODO: Make a card
