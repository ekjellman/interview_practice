###
# Problem
###

# Convert valid Roman numeral string to integer.

###
# Work
###
# Questions:
# Deal with invalid strings? (Assume no)
# Length of string?
# Case? (assume upper)

def roman_to_int(s):
  total = 0
  values = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
  i = 0
  while i < len(s):
    if i == len(s) - 1:
      total += values[s[i]]
      i += 1
    else:
      if values[s[i]] < values[s[i+1]]:
        total += values[s[i+1]]
        total -= values[s[i]]
        i += 2
      else:
        total += values[s[i]]
        i += 1
  return total

# Tests:
print roman_to_int("I"), 1
print roman_to_int("IV"), 4
print roman_to_int("IX"), 9
print roman_to_int("LIX"), 59
print roman_to_int("XXXXXIIIIIIIII"), 59
print roman_to_int("MMXIX"), 2019

# Time: 8 minutes

###
# Mistakes / Bugs / Misses
###
# Had a comma for one of the colons at 17
# Forgot i += 1 at 22
# DId not think about a right to left solution
