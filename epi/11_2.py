###
# Problem
###

# Efficiently sort a k-increasing-decreasing array. This is an
# array where the elements increase up to some index, then
# decrease, and this is repeated k-times.

###
# Work
###
# Questions:
# Size of the list
# Are we meant to do this in-place? (... I don't know)
# (I'm going to start with "no")
# Is the number of elements in each sequence the same? I don't
# think so, but the figure says 4-inc-dec when it only goes through
# 2 cycles? I'm a bit confused.

# Approaches:
# Just sort the thing. O(n log n)
# Find an increase-decrease cycle, and then merge sort
# O(n) time, O(n) space for output list
# I feel like since this is the heaps chapter there's a better
# solution, but I don't see it.

def sort_inc_dec(nums):
  # Reuse implementation from 11_1

def make_lists(nums):
  lists = []
  current_list = []
  increasing = True
  for num in nums:
    if increasing:
      if not current_list or num >= current_list[-1]:
        current_list.append(num)
      else:
        lists.append(current_list)
        increasing = False
        current_list = [num]
    else:
      if num <= current_list[-1]:
        current_list.append(num)
      else:
        current_list.reverse()
        increasing = True
        lists.append(current_list)
        current_list = [num]
  if not increasing:
    current_list.reverse()
  lists.append(current_list)
  return lists

# Tests:
print make_lists([57, 131, 493, 294, 221, 339, 418, 452, 442, 190])

# Time: 17 minutes

###
# Mistakes / Bugs / Misses
###
# Spent 10 minutes on an approach that wouldn't work. Read hint.
# Forgot colon on 30
