###
# Problem
###

# Write a program to return the first n rows of Pascal's triangle

###
# Work
###
# Questions:
# Do we need it "centered", or is left-justified ok? Formatting?
# (assume formatting doesn't matter)
# Size of n? (overflow in some languages)
# Output? (Assume list of lists)

def pascals(n):
  if n <= 0: return []
  result = [[1]]
  while len(result) < n:
    next_row = [1]
    for x in xrange(1, len(result)):
      next_row.append(result[-1][x-1] + result[-1][x])
    next_row.append(1)
    result.append(next_row)
  return result

# Test
for row in pascals(10):
  print row

# There is also the pure numerical answer (calculate (n k) for each)
# It is probably not faster, but better if you just want a specific row.

# Time: 6 minutes

###
# Mistakes / Bugs / Misses
###
# Line 22 has comma instead of plus
# Line 21 had len(result) - 1 instead of len(result)
