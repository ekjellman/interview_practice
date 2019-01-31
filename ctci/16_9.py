###
# Problem
###

# Write methods to implement multiply, subtract, and divide operations for
# integers. The results are integers. Use only the add operator.

###
# Work
###
# Subtract:
# Can I use unary minus? (I'd assume yes?)
# Maybe I'm missing the point
# Can I bit-shift? (Assume no)
# Are a and b positive? (Assume yes)

def subtract(a, b):
  return a + -b

def divide(a, b):
  # TODO: Error checking (div 0, etc)
  multiples = [b]
  powers = [1]
  while multiples[-1] < a:
    multiples.append(multiples[-1] + multiples[-1])
    powers.append(powers[-1] + powers[-1])
  total = 0
  while multiples:
    if a >= multiples[-1]:
      total += powers[-1]
      a = subtract(a, multiples[-1])
    multiples.pop()
    powers.pop()
  return total

def multiply(a, b):
  print "called", a, b
  if b == 1:
    return a
  if a == 0 or b == 0:
    return 0
  half = divide(b, 2)
  if half + half == b:
    return multiply(a + a, half)
  else:
    return multiply(a + a, half) + a

print divide(70000, 7), 10000
print divide(3, 7), 0

print multiply(100, 100), 10000
print multiply(1000, 1000), 1000000
print multiply(1, 100), 100
print multiply(6, 100), 600

# Time: 15 minutes

###
# Mistakes / Bugs / Misses
###
# Line 25: Used power instead of powers for the second powers[-1]
# Line 23: Had multiples[0] instead of multiples[-1]
# Line 38: Had return b instead of return a
# Not sure I understand her negate() function. TODO (page 478)
# Her multiplication function does not use division, which is why I
# implemented division first
# I did assume all numbers were positive. It is something I would have asked,
# though
