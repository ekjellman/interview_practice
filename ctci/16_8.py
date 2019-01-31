###
# Problem
###

# Given an integer, print an English phrase describing the integer.
# Ex: 1234 -> One Thousand, Two Hundred Thirty Four

###
# Work
###
# Questions:
# Limit of the integer? (assume trillions)
# Where do commas go? (assume between sets of three numbers)
# Ands? (assume no)
# Negative? Zero? (Assume yes)
DIGITS = ["", "One", "Two", "Three", "Four", "Five", "Six",
          "Seven", "Eight", "Nine"]
TEENS = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen",
         "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Ninteen"]
TENS = ["", "", "Twenty", "Thirty", "Forty", "Fifty",
        "Sixty", "Seventy", "Eighty", "Ninty"]
LARGE = ["", "Thousand", "Million", "Billion", "Trillion"]

def sub_thousand(n):
  assert 0 <= n <= 999
  hundreds = n / 100
  remainder = n % 100
  if hundreds:
    return [DIGITS[hundreds], "Hundred"] + sub_hundred(remainder)
  else:
    return sub_hundred(remainder)

def sub_hundred(n):
  if n < 10:
    return [DIGITS[n]]
  elif 10 <= n <= 19:
    return [TEENS[n - 10]]
  else:
    ten_digit = n / 10
    remainder = n % 10
    return [TENS[ten_digit], DIGITS[remainder]]

def english(n):
  if n == 0: return "Zero"
  if n < 0:
    negative = True
    n = -n
  pieces = []
  large_index = 0
  while n > 0:
    small = n % 1000
    pieces = sub_thousand(small) + [LARGE[large_index]] + pieces
    large_index += 1
    n /= 1000
  pieces = [x for x in pieces if x != ""]
  return " ".join(pieces)

print "234", english(234)
print "123456", english(123456)
print "70000", english(70000)
print "1234567890", english(1234567890)

# Time: 19 minutes

###
# Mistakes / Bugs / Misses
###
# Didn't remember a good way to filter out ""
# Typo in line 39
# Forgot else case in sub_thousand
# Had (n) instead of [n] in line 35 and 37
# Had 31 wrapped in a list
