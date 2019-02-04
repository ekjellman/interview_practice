###
# Problem
###

# For the game of mastermind, given an actual solution and a guess, compute
# how many hits and almost hits there are.

###
# Work
###
# Questions:
# Length of the strings? (Assume they're the same at least)
# Number of possible colors? (Assume any character)
#   -- If it were just 4 letters and 4 colors each, a cache would be possible
# Case-sensitive? (Assume yes)

import collections

def hits(solution, guess):
  hits = 0
  psuedo_hits = 0
  solution_counts = collections.defaultdict(int)
  guess_counts = collections.defaultdict(int)
  assert len(solution) == len(guess)
  for i in xrange(len(solution)):
    if solution[i] == guess[i]:
      hits += 1
    else:
      solution_counts[solution[i]] += 1
      guess_counts[guess[i]] += 1
  for letter in solution_counts:
    psuedo_hits += min(solution_counts[letter], guess_counts[letter])
  return hits, psuedo_hits

# Tests
print (4, 0), hits("RGBY", "RGBY")
print (0, 4), hits("RGBY", "GRYB")
print (1, 1), hits("RGBY", "GGRR")
print (0, 0), hits("RRGG", "YYBB")

# Time: 7 minutes

###
# Mistakes / Bugs / Misses
###
# Didn't ask about case until writing tests
# Forgot to import collections
