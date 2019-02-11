###
# Problem
###

# A circus tower is made of people standing on each others shoulders. However,
# each person on top must be shorter and lighter than the person below. Given
# a list of weights and heights, compute the largest number of people in a
# tower with those people.

###
# Work
###
# Questions:
# Number of people?
# Input? (Assume list of (weight, height) tuples
# Output? (Problem said number of people)

# I think there's a graph/dijkstra like approach, but I think I'll just go with
# recursion today.

def circus_tower(people):
  # Sorts by weight descending
  sorted_people = sorted(people, reverse=True)
  return circus_tower_inner(sorted_people)

def circus_tower_inner(people, base_index=-1, cache=None):
  if cache is None:
    cache = {}
  if base_index in cache:
    return cache[base_index]
  if base_index == -1:
    base_height = float("inf")
    base_weight = float("inf")
  else:
    base_height = people[base_index][0]
    base_weight = people[base_index][1]
  best = 0
  for i in xrange(base_index + 1, len(people)):
    if people[i][0] < base_height and people[i][1] < base_weight:
      best = max(best, 1 + circus_tower_inner(people, i, cache))
  cache[base_index] = best
  return best

# Test:
import random
people = [(50, 10), (20, 9), (30, 8), (15, 7), (25, 6), (5, 5), (10, 4),
          (12, 3), (8, 2), (15, 1)]
random.shuffle(people)
print circus_tower(people), 5

# Time: 15 minutes

###
# Mistakes / Bugs / Misses
###
# Forgot to use the sorted_people in line 24
# I'm not sure that I find the iterative solution much cleaner, but they both
# are O(n**2) (the memoization solution is O(n**2).
# Gayle talks about an n log n solution to this. The algorithm is called the
# "longest increasing subsequence" problem. TODO: Make card for n log n
