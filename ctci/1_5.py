###
# Problem
###

# Find if two strings are one edit away. An edit is an insert, remove, or
# replace


###
# Work
###

# Questions:
# Case matters? (Assume yes)
# ASCII? (assume yes)

# Discarded approaches:
# Generate all one-edits of first string, see if second is in that set
# Calculating edit distance with Levenshtein

def one_away(a, b):
  if len(a) == len(b):  # Change case
    # or sum(1 for ... if a[i] != b[i]) for clarity
    return sum(a[i] != b[i] for i in xrange(len(a))) <= 1
  # Make a the longer string to avoid two equivalent cases
  if len(b) > len(a):
    a, b = b, a
  if len(a) - len(b) > 1: return False
  changes = 0
  for i in xrange(len(a) - 1):
    if a[i + changes] != b[i]:
      changes += 1
      if changes == 2:
        return False
  return True

tests = [("pale", "ple", True),
         ("pales", "pale", True),
         ("pale", "pales", True),
         ("pale", "bale", True),
         ("pale", "bae", False),
         ("", "", True),
         ("pale", "pale", True),
         ("", "a", True),
         ("", "aa", False),
         ("pale", "plea", False)]

for a, b, expected in tests:
  print a, b, expected, one_away(a, b)

# Time: 15 minutes

###
# Mistakes / Bugs / Misses
###

# Line 30: Didn't put -1 on the bounds
