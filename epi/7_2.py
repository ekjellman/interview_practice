###
# Problem
###

# Given a string, a starting base, and an ending base, convert the number
# represented by the string from the starting base to the ending base
# Ex: f("615", 7, 13) -> "1A7"
# Assume the bases are in the range 2 <= base <= 16

###
# Work
###
# Questions:
# Size of numbers?
# Extensibility to other bases?
# Negative numbers? (Assume no... otherwise just do what we did last time)
# Output type? (string)

def convert(string, start_base, end_base):
  digits = "0123456789ABCDEF"
  number = 0
  # Get number in starting base
  for i in xrange(len(string)):
    digit = digits.find(string[-(i+1)])   # Could use ord
    number += digit * (start_base ** i)
  # Get new string from number
  chars = []
  while number > 0:
    digit = number % end_base
    number /= end_base
    chars.append(digits[digit])
  chars.reverse()
  return "".join(chars)

# Tests:
print convert("74", 10, 10), "74"
print convert("74", 10, 4), "1022"
print convert("615", 7, 13), "1A7"
print convert("65534", 10, 2), "1111111111111110"
print convert("65534", 10, 16), "FFFE"

# Time: 7 minutes

###
# Mistakes / Bugs / Misses
###
# Forgot to use find in line 24 (So had a int/str conversion error)
