###
# Problem
###

# Design an algorithm to find the kth number such that the only prime factors
# are 3, 5, and 7.

###
# Work
###
# Questions:
# Size of k?

# Approaches
# brute force (generate all numbers up to 3**k 5**k 7**k and sort)
#   this would take k**3 space and k**3 log k**3 time.
# Set approach: find minimum of (set(3, 5, 7)). Add n*3, n*5, n*7 to set.
#               repeat. Takes o(3k) time per number, or O(k**2) time
# Queue approach:

import collections
def kth_multiple(k):
  if k == 0: return 0
  if k == 1: return 1  # or 0 index
  threes = collections.deque([3])
  fives = collections.deque([5])
  sevens = collections.deque([7])
  current_k = 2
  while True:
    assert threes[0] != fives[0] and threes[0] != sevens[0] and fives[0] != sevens[0]
    if threes[0] < fives[0] and threes[0] < sevens[0]:
      current_num = threes.popleft()
      threes.append(current_num * 3)
    elif fives[0] <= sevens[0]:
      current_num = fives.popleft()
      threes.append(current_num * 3)
      fives.append(current_num * 5)
    else:
      current_num = sevens.popleft()
      threes.append(current_num * 3)
      fives.append(current_num * 5)
      sevens.append(current_num * 7)
    if current_k == k:
      return current_num
    current_k += 1

def kth_multiple_brute(k):
  numbers = set()
  for i in xrange(0, k + 1):
    for j in xrange(0, k + 1):
      for k in xrange(0, k + 1):
        numbers.add(3**i * 5**j * 7**k)
  sorted_numbers = sorted(numbers)
  return sorted_numbers[k-1]


print kth_multiple(7), "21"
print kth_multiple(10), kth_multiple_brute(10)
print kth_multiple(100), kth_multiple_brute(100)

# Time: 23 minutes

###
# Mistakes / Bugs / Misses
###
