###
# Problem
###
# Now do it with duplicate characters. Don't generate duplicates.

###
# Work
###

# Same questions as last time

def perms(s):
  if not s: raise StopIteration
  if len(s) == 1: yield s
  for c in set(s):
    substring = s.replace(c, "", 1)
    for p in perms(substring):
      yield c + p

for p in perms("aabb"):
  print p

# Time: 8 minutes

###
# Mistakes / Bugs / Misses
###
# Could not remember the replace() function. I originally put:
    # Assuming a function to remove a char from a string. I can't remember it
    # substring = s.remove(c)
# The version in the book (making a hashtable of character counts and recursing
# with that) is an approach I should remember. It's probably better than making
# a new set at every level.
