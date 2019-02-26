###
# Problem
###

# Write a program that takes a list A and an index into the list, and rearranges
# the elements such that all elements less than A[i] (a pivot) appear first,
# followed by the elements equal to the pivot, followed by elements greater
# than the pivot

###
# Work
###
# Questions:
# In-place? (assume yes)
# Error-checking? (assume valid input)

def national_flag(nums, pivot):
  # TODO: Error checking (valid pivot, non-empty list, whatever)
  current = 0
  left_swap = 0
  right_swap = len(nums) - 1
  pivot_num = nums[pivot]
  while current <= right_swap:
    if nums[current] < pivot_num:
      nums[left_swap], nums[current] = nums[current], nums[left_swap]
      current += 1
      left_swap += 1
    elif nums[current] > pivot_num:
      nums[right_swap], nums[current] = nums[current], nums[right_swap]
      right_swap -= 1
    else:
      current += 1

# Tests:
a = [4, 8, 1, 4, 2, 6, 4, 4, 9, 3]
national_flag(a, 0)
print a, "Pivot = 4"
a = [6, 6, 6, 6, 6, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4]
national_flag(a, 7)
print a, "Pivot = 5"
import random
for i in xrange(10):
  a = [random.randint(0, 9) for _ in xrange(15)]
  pivot_index = random.randint(0, 14)
  pivot_element = a[pivot_index]
  national_flag(a, pivot_index)
  print a, "Pivot = %d" % pivot_element


# Time: 19 minutes

###
# Mistakes / Bugs / Misses
###
# Had + instead of - on line 30
# Had < instead of <= on line 23
# Had 1 instead of 0 on line 19
# They had a cleaner solution where they do it in two passes, one to get the
# smaller numbers in place, then one to get the larger numbers in place. That's
# probably an approach I should remember. (TODO: make card)
