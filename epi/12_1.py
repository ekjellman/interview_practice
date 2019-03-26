###
# Problem
###

# Write a method that takes a sorted array and a key and returns the index
# of the first occurrence of the key in the array.

###
# Work
###
# Questions:
# Types of the keys (assuming int)
# Size of list (Small enough, use find() or whatever it's called

def first(numbers, key, low=None, high=None):
  if low is None:
    low = 0
    high = len(numbers) - 1
  if low > high:
    return None
  mid = (low + high) / 2
  if numbers[mid] == key:
    while mid > 0 and numbers[mid - 1] == key:
      mid -= 1   # Could also binary search for key - 1
    return mid
  elif numbers[mid] > key:
    return first(numbers, key, low, mid - 1)
  else:
    return first(numbers, key, mid + 1, high)

# Tests
print first([-14, -10, 2, 108, 108, 243, 285, 285, 285, 401], -14), "0"
print first([-14, -10, 2, 108, 108, 243, 285, 285, 285, 401], -10), "1"
print first([-14, -10, 2, 108, 108, 243, 285, 285, 285, 401], 401), "9"
print first([-14, -10, 2, 108, 108, 243, 285, 285, 285, 401], 285), "6"
print first([-14, -10, 2, 108, 108, 243, 285, 285, 285, 401], 108), "3"

# Time: 9 minutes

###
# Mistakes / Bugs / Misses
###
# Their solution is better. (TODO: Make card)
