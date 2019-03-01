###
# Problem
###

# Implement atoi and itoa. Your code should handle negative numbers.

###
# Work
###
# Questions:
# Error handling? (Assume input is valid)
# size of strings / numbers? (It's Python, don't worry about it)

def atoi(s):
  if s[0] == "-":
    negative = True
  else:
    negative = False
  number = 0
  for c in s:
    if c == "-": continue   # Only works if input is valid
    digit = ord(c) - ord("0")
    number *= 10
    number += digit
  if negative:
    number = -number
  return number

def itoa(n):
  if n < 0:
    negative = True
    n = -n
  elif n == 0:
    return "0"
  else:
    negative = False
  digits = []
  while n > 0:
    digit = n % 10
    n /= 10
    digits.append(chr(ord("0") + digit))
  if negative:
    digits.append("-")
  digits.reverse()
  return "".join(digits)

# Tests
print atoi("1234"), "1234"
print atoi("-520"), "-520"
print atoi("3"), "3"
print itoa(0), "0"
print itoa(1234567), "1234567"
print itoa(-54321), "-54321"


# Time: 10 minutes

###
# Mistakes / Bugs / Misses
###
# Line 41 directly appended the digit to the list, instead of turning it into
#   a character
# Forgot lines 42-43
