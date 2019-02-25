###
# Problem
###
# Compute x * y only using:
#  -- Assignment
#  -- Bitwise operators >> << | & ~
#  -- equality checks (and boolean combinations thereof)

# You may not increment, decrement, or use comparison operators
# x and y are non-negative integers

###
# Work
###
# Questions:
# Who the hell has bitwise operators but not addition?
# Can I use functions? (Sure, why not, everyone loves stacks to avoid addition)
def add(a, b):
  # or: if a == 0 or b == 0: return a | b
  if a == 0: return b
  if b == 0: return a
  carry = (a & b) << 1
  rest = a ^ b
  return add(carry, rest)

def multiply(a, b):
  total = 0
  # This works since we know a and b are non-negative
  while b != 0:
    if b & 1 == 1:
      total = add(total, a)
    b >>= 1
    a <<= 1
  return total

# Tests:
print multiply(15, 25), "375"
print multiply(22, 11), "242"
import random
for i in xrange(50):
  a = random.randint(0, 100000000)
  b = random.randint(0, 100000000)
  result = multiply(a, b)
  correct = a * b == result
  print correct, a, b, result, a * b

# Time: 9 minutes

###
# Mistakes / Bugs / Misses
###
# They use a different method to add. I'll keep mine, although if I really
# wanted to get into the spirit of the problem, I'd avoid recursion.
