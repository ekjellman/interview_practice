###
# Problem
###

# Write a method that finds the maximum of two numbers. Don't use if/else
# or other comparison methods.

###
# Work
###
# To start with, I'm not sure how I would do this in Python.

# The basic idea is, subtract the two numbers.
# Say it's a - b. If a - b is positive, a is the number
#                 If a - b is negative, b is the number
# To find out if a-b is negative or positive, we'd want to check against
# the sign bit assumedly. So if that bit is going to be 0 or 1, we can do it
# like this:

def max(a, b):
  c = a - b
  d = b - a
  sign_c = -(c >> c.bit_length())  # ??
  sign_d = -(d >> d.bit_length())  # ??
  print sign_c
  print sign_d
  return (a * sign_d) + (b * sign_c)

# This works except for the equal case, where both sign_c and sign_d will be
# 0. We want to add a (or b) if sign_c and sign_d are 0, and not otherwise.

def max(a, b):
  c = a - b
  d = b - a
  sign_c = -(c >> c.bit_length())  # ??
  sign_d = -(d >> d.bit_length())  # ??
  equal = not (sign_c ^ sign_d)
  print sign_c
  print sign_d
  print equal
  return (a * sign_d) + (b * sign_c) + (a * equal)

print max(4, 12), 12
print max(-11, -16), -11
print max(0, 0), 0
print max(12, 12), 12

# This is a little dirty because equal is actually a boolean, whereas
# sign_c and sign_d are not, but it does work. >_<


# Time: 17 minutes

###
# Mistakes / Bugs / Misses
###
# initially had c and d instead of sign_d and sign_c
# Initially had - instead of not for equal, which doesn't work
# Didn't remember if bit_length() was the correct function
# Didn't remember if -1 >> n was -1
# Her code talks about overflow, but that's not a thing in Python
