###
# Problem
###

# Given an array of positive integers, find the majority element. Return -1
# if not exists. Do it in O(N) time and O(1) space. (Majority: more than half)

###
# Work
###
# Questions:
# Size of input array
# Use cases
# Approximate solutions? (Assume no)

# Approaches:
# Brute force: Use a set (but O(n) space)
# Check each element (but O(n**2) time)
# Sort and check runs (but O(n log n) time)

def majority(numbers):
  if not numbers: return -1
  current, count = -1, 0
  for number in numbers:
    if current == -1:
      current = number
      count = 1
    elif number == current:
      count += 1
    else:
      count -= 1
      if count == 0:
        current = -1
  if current == -1: return -1
  count = 0
  for number in numbers:
    if number == current: count += 1
  if count > len(numbers) / 2:
    return current
  return -1

# Tests:
print majority([1, 2, 3, 4, 5, 6, 7]), "-1"
print majority([1, 1, 1, 1, 2, 2, 2, 2]), "-1"
print majority([1, 2, 1, 2, 1, 2, 1, 2, 1]), "1"
print majority([2, 1, 2, 1, 2, 1, 2, 1, 1]), "1"
print majority([2, 1, 2, 1, 2, 1, 2, 1]), "-1"
print majority([1, 2, 3, 4, 5, 5, 5, 5, 5]), "5"

# Time: 10 minutes

###
# Mistakes / Bugs / Misses
###
# There is a better way of counting than 36-37, use count()
