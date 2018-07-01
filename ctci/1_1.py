# 1-1: Implement an algorithm to determine if a string has all unique
#      characters

# Questions:
# -- What characters? ASCII? Unicode? (Assuming ASCII)
# -- Expected length of string? (Unknown.)
# -- Desired output for empty string (assumedly True)
# -- Is the string sorted? (Could use a single runthrough pass)
# -- Does case matter?

def is_unique(s):
  return len(set(s)) == len(s)

# Other possible approaches: Use an array of n characters, store counts
#                            Use a counter
#                            Use a bitvector
#                            If string is longer than possible number of
#                              characters, return False immediately

# Alternate: What if you cannot use additional data structures?

def is_unique_2(s):
  for char in s:
    if s.count(char) > 1: return False
  return True

# Tests:
tests = [("", True),
         ("abcdefgh", True),
         ("abcdefghh", False),
         ("abcdefgha", False),
         ("01230", False),
         ("01234", True)]

for test in tests:
  s, expected = test
  print is_unique(s), expected

###
# Mistakes / Misses / Bugs
###

# Line 33: Put "False" as result of test



