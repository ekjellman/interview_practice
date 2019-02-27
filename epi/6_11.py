###
# Problem
###

# Given a permutation, return the next lexicographic permutation.
# ex: [1, 0, 3, 2] -> [1, 2, 0, 3]
# ex: [2, 0, 1] -> [2, 1, 0]
# ex: [3, 2, 1, 0] -> None


###
# Work
###
# Questions:
# Size of n
# Are the numbers guaranteed to be between 0-(n-1)? (Assume no)

def next_permutation(p):
  if len(p) <= 1: return None
  for i in xrange(len(p) - 2, -1, -1):
    if p[i] < p[i+1]:
      break
  else:
    return None
  swap_element = i + 1
  next_highest = p[i+1]
  for j in xrange(i + 2, len(p)):
    if p[j] > p[i] and p[j] < next_highest:
      swap_element = j
      next_highest = p[j]
  p[i], p[swap_element] = p[swap_element], p[i]
  return p[:i+1] + sorted(p[i+1:])

# Tests:
print next_permutation([1, 0, 3, 2]), "1203"
print next_permutation([2, 0, 1]), "210"
print next_permutation([3, 2, 1, 0]), "None"

p = [0, 1, 2, 3]
while p is not None:
  print p
  p = next_permutation(p)

# Time: 15 minutes

###
# Mistakes / Bugs / Misses
###
# Forgot to swap the next element in. Then screwed up what the next element was.
# Missed a couple of optimizations:
# element. Example:
# p = [6, 2, 1, 5, 4, 3, 0].
#            ^ swap this with next greatest
# p = [6, 2, 3, 5, 4, 1, 0]  (note I could have searched from right side, and
#                             not had to keep track of next largest)
#  Now sort     ^^^^^^^^^^
#  But I don't have to sort. This is in reverse order. I can just flip it.
# p = [6, 2, 3, 0, 1, 4, 5]   And we're done.
# TODO: Make card
