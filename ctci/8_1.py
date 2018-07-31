###
# Problem
###

# A child is running up a staircase with n steps. They can climb 1, 2, or 3
# steps at a time. How many different ways can the child run up the stairs?

###
# Work
###
# Questions:
# Size of n? (might matter in languages without arbitrary longs)
# Does running over the top of the staircase count as a different way? (No)

def ways(n):
  # If the child could jump more than three, or an arbitrary number, I'd just
  # start with table[0] = 1, and build it with bounds checking or min on index
  if n == 0: return 1
  if n == 1: return 1
  if n == 2: return 2
  table = [0] * (n + 1)
  table[0] = 1
  table[1] = 1
  table[2] = 2
  for x in xrange(3, len(table)):
    table[x] = table[x-3] + table[x-2] + table[x-1]
  return table[n]

print ways(0), "1"
print ways(1), "1"
print ways(2), "2"
print ways(3), "4"
print ways(4), "7"

# Time: 5 minutes

###
# Mistakes / Bugs / Misses
###
# Line 25 had xrange(table), both didn't use len() or a lower bound of 3
