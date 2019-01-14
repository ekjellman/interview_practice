###
# Problem
###

# Print all the ways of arranging eight queens on an 8x8 chess board.

###
# Work
###

# Questions:
# Should we make it extensible? (i.e. n x n)
# Method of output? (I'm going to just output an array of columns, but for
#   example we might print out an actual board

def queens(n, partial=None):
  if partial is None:
    partial = []
  if len(partial) == n:
    print partial
    return
  for column in xrange(n):
    if column in partial: continue   # Inefficient depending on size of n
    for i in xrange(len(partial)):
      row_diff = len(partial) - i
      col_diff = partial[i] - column
      if abs(row_diff) == abs(col_diff): break   # diagonal
    else:
      partial.append(column)
      queens(n, partial)
      partial.pop()

# Tests
queens(8)
queens(4)

# Time: 13 minutes

###
# Mistakes / Bugs / Misses
###
# Note: The line at 23 could be inefficient if n is larger. We could, at the
#       start of the loop, convert partial to a set. Or, we could also pass
#       along a bitfield saying which columns have been used.
# Screwed up the continue inside the i for loop, since I want it to skip to the
#   next column.
# Had for i in partial instead of line 24
