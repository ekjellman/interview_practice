###
# Problem
###

# Write a method to compute all permutations of a string of unique
# characters

###
# Work
###

# Questions:
# Size of string?
# What do you mean by "Compute"? Print ok? Generator ok?
#  -- I'm going to use a generator
# Unicode related questions
# What do you mean by "permutation of a string"?
#  -- Assumedly "abc" -> abc, acb, bac, bca, cab, cba
# What solution for empty ("") case? (Assume empty list?)

# Solution 1
import itertools
def perms(s):
  for p in itertools.permutations(s):
    yield "".join(p)

# Solution 2
def perms(s):
  if not s:
    raise StopIteration   # Verify with interviewer.
  if len(s) == 1:
    yield s
  for i in xrange(len(s)):
    substring = s[:i] + s[i+1:]
    for p in perms(substring):
      yield s[i] + p

# tests
for p in perms("abcd"):
  print p

print list(perms(""))

# Time: 9 minutes

###
# Mistakes / Bugs / Misses
###
# Didn't ask questions about "" case until I started coding
# Didn't think about building from the other direction (i.e.: Inserting
#   one character at a time into the list of all permutations created).
#   I should think about how to turn that into a generator?

