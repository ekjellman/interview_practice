###
# Problem
###

# Write a function to multiply two arbitrary length integers represented as
# arrays. If a number is negative, the first item in the array will be negative.

###
# Work
###
# Questions:
# Length of arrays

def multiply(a, b):
  negative = False
  if a[0] < 0:
    negative = not negative
    a[0] = abs(a[0])
  if b[0] < 0:
    negative = not negative
    b[0] = abs(b[0])
  total = [0]
  # Could swap a and b based on length here
  pos = 0
  while b:
    digit = b.pop()
    digit_result = digit_multiply(a, digit)
    for i in xrange(pos):
      digit_result.append(0)
    total = add(total, digit_result)
    normalize(total)
    pos += 1
  if negative:
    total[0] = -total[0]
  return total

def digit_multiply(a, digit):
  return [x * digit for x in a]

def add(a, b):
  # destroys a and b
  result = []
  while a or b:
    a_digit = a.pop() if a else 0
    b_digit = b.pop() if b else 0
    result.append(a_digit + b_digit)
  result.reverse()
  return result

def normalize(a):
  for i in xrange(len(a) - 1, 0, -1):
    if a[i] >= 10:
      a[i-1] += a[i] / 10
      a[i] %= 10
  while a[0] >= 10:
    carry = a[0] / 10
    a[0] %= 10
    a.insert(0, carry)

a = [1, 9, 3, 7, 0, 7, 7, 2, 1]
b = [-7, 6, 1, 8, 3, 8, 2, 5, 7, 2, 8, 7]
c = multiply(a, b)
print c
print "expected: -147573952589676412927"

a = [1, 1, 1, 1, 1]
b = [1, 1, 1, 1, 1]
c = multiply(a, b)
print c

# Time: 20 minutes

###
# Mistakes / Bugs / Misses
###
# Forgot if .reverse() worked. Go review cards.
# Forgot to implement digit_multiply
# Forgot to increment pos at line 32
# The book's solution is really interesting (TODO: Make card). Basically, they
# loop through the m * n digit multiplications, updating a single list of size
# len(a) + len(b) in the appropriate place for each digit * digit. This is
# better because you don't have to allocate as many lists.
