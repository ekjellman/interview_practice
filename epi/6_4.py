###
# Problem
###

# You start at position 0 on a board. At each square is a maximum number n of
# spaces you can advance; you can advance any of 1-n spaces.

# Determine if it is possible to reach the end of the array.
# Ex: [3, 3, 1, 0, 2, 0, 1] -> True. Can go from 0 to 1 to 4 to 6.
# Ex: [3, 2, 0, 0, 2, 0, 1] -> False. No moves can get you past 3.

###
# Work
###
# Questions:
# Length of input
# size of numbers

# We could do a recursive solution, but since we can advance any of 1-n, we can
# instead just mark the farthest we can go, knowing we can get to any square
# before that if needed

def winnable(board):
  if len(board) <= 1:
    return True
  farthest = board[0]
  for i in xrange(len(board)):
    if i > farthest: return False
    farthest = max(farthest, i + board[i])
  return True

# Tests
print winnable([3, 3, 1, 0, 2, 0, 1]), "True"
print winnable([3, 2, 0, 0, 2, 0, 1]), "False"
print winnable([0]), "True"
print winnable([1, 1, 1, 1, 1, 1, 1, 1]), "True"
print winnable([1, 1, 0, 1, 1, 1, 1, 1]), "False"
print winnable([0, 1, 1, 1, 1, 1, 1, 1]), "False"
print winnable([1, 1, 1, 1, 1, 1, 1, 0]), "True"
print winnable([99, 0, 0, 0, 0, 0, 0]), "True"
print winnable([5, 0, 0, 0, 0, 1, 0]), "True"

# Time: 5 minutes

###
# Mistakes / Bugs / Misses
###
