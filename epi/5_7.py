###
# Problem
###

# Write a program that takes a double x and an integer y and returns x**y. You
# can ignore overflow and underflow.

###
# Work
###
# Questions:
# Can I assume y is non-negative? (Let's say yes, but discuss it afterwards?)

def cheeky(x, y):
  return x ** y

def exp(x, y):
  multiplier = x
  result = 1
  while y > 0:
    if y & 1 == 1:
      result *= multiplier
    multiplier *= multiplier
    y >>= 1
  return result

# If we allowed non-negative y, return 1.0 / result?

# Tests:
print exp(3, 7), 3**7
print exp(10, 6), 10**6
import random
for x in xrange(20):
  x = random.random() + random.randint(0, 5)
  y = random.randint(0, 25)
  result = exp(x, y)
  actual = x ** y
  correct = .99999 <= (result / actual) <= 1.00001
  print correct, x, y, result, actual

# Time: 11 minutes

###
# Mistakes / Bugs / Misses
###
# the correct check was diff < .0001, but that didn't really work.
