###
# Problem
###

# Write a program that takes an integer and reverses its digits
#

###
# Work
###
# Questions:
# Handle negative numbers? (Yes. Also there was a negative example)

def reverse_digits_cheeky(n):
  negative = n < 0
  n = abs(n)
  return int(("-" if negative else "") + "".join(reversed(str(n))))

def reverse_digits(n):
  negative = n < 0
  n = abs(n)
  result = 0
  while n > 0:
    next_digit = n % 10
    n /= 10
    result *= 10
    result += next_digit
  return -result if negative else result

# Tests
print reverse_digits(42), "24"
print reverse_digits(-314), "-413"

# Time: 4 minutes

###
# Mistakes / Bugs / Misses
###
