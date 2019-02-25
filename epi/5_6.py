###
# Problem
###

# Compute x / y using only addition, subtraction, and shifting.
# Assume x and y are positive.

###
# Work
###
# Integer division? i.e., do you want the remainder or fractional part?
# (assuming no)
# Assumedly I can also use language constructs like if or for loops?

def div(x, y):
  factor = 1
  result = 0
  while x > y:
    factor <<= 1
    y <<= 1
  while factor != 0:
    if x >= y:
      x -= y
      result += factor
    factor >>= 1
    y >>= 1
  return result

print div(225, 15), "15"
print div(4096, 4), "1024"
print div(96, 15), "6"
import random
for i in xrange(20):
  x = random.randint(0, 100000000000)
  y = random.randint(0, 10000)
  result = div(x, y)
  correct = result == (x / y)
  print correct, x, y, result, x / y

# Time: 4 minutes

###
# Mistakes / Bugs / Misses
###
