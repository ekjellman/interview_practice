###
# Problem
###

# Given a positive integer, find the next smallest and next largest numbers that
# have the same number of 1 bits in their binary representation.

###
# Work
###
# Questions:
# Print or return? (assume return, although the book says print)

def find_digit(num, target, start_digit):
  # Watch out for infinite loop
  while num & (1 << start_digit) != (1 << start_digit if target else 0):
    start_digit += 1
  return start_digit

def next_largest(num):
  digit = find_digit(num, 1, 0)
  digit = find_digit(num, 0, digit)
  num |= 1 << digit
  ones = 0
  for i in xrange(digit):
    if num & (1 << i) != 0:
      ones += 1
    num &= ~(1 << i)
  num |= ((1 << ones) - 1)
  return num

print bin(next_largest(0b1001101)), "0b1001110"
print bin(next_largest(0b10001000)), "0b10010000"
print bin(next_largest(0b100011100)), "0b100100011"

def next_smallest(num):
  digit = find_digit(num, 0, 0)
  digit = find_digit(num, 1, digit)
  ones = 0
  for i in xrange(digit + 1):
    if num & (1 << i) != 0:
      ones += 1
    num &= ~(1 << i)
  num |= ((1 << ones) - 1) << (digit - ones)
  return num

print bin(next_smallest(0b10010001111)), "0b10001111100"
print bin(next_smallest(0b1001101)), "0b1001011"
print bin(next_smallest(0b10001000)), "0b10000100"
print bin(next_smallest(0b100011100)), "0b100011010"


# Time: 25 minutes

###
# Mistakes / Bugs / Misses
###
# find_digit had != target
# forgot = on &= at line 28
# forgot ones = 0 at line 39
# Should have broken the counting ones / zeroing things to functions
# My approach for zeroing out the ones is not optimal at all.
# Study this solution more
# REDO
