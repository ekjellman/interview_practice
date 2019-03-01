###
# Problem
###

# Write a function that converts a spreadsheet column id to a corresponding
# int.
# Ex: "A" -> 1
# Ex: "Z" -> 26
# Ex: "AA" -> 27
# Ex: "ZZ" -> 702

###
# Work
###
# Questions:
# Size of string?
# Valid input assumed? (assume yes)
# Case? (Assume upper)

def column_to_int(s):
  number = 0
  for c in s:
    digit = ord(c) - ord("A") + 1
    number *= 26
    number += digit
  return number

print column_to_int("A"), 1
print column_to_int("D"), 4
print column_to_int("Z"), 26
print column_to_int("AA"), 27
print column_to_int("ZZ"), 702

# How to test more generically: generate the first say 3-letters worth of column
# IDs, and test the function with all of them

# Time: 4 minutes

###
# Mistakes / Bugs / Misses
###
# Forgot the +1 in line 23
