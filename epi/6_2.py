###
# Problem
###

# Given an array of digits encoding a decimal number, update the array to
# represent the number D + 1.

# Example: [1, 2, 9] (129) -> [1, 3, 0]
# Your algorithm should work even if it is implemented in a language with
# finite-precision arithmetic

###
# Work
###
# Questions:
# Size of array? (Assume fits in memory)
# Output? (Assume modify list in place)

def increment(nums):
  # TODO: Error checking (all numbers 0 <= x <= 9, for example)
  if not nums: return None
  nums[-1] += 1
  for i in xrange(len(nums) - 1, 0, -1):  # Don't do this to first element
    if nums[i] == 10:   # Assumes valid input
      nums[i] = 0
      nums[i-1] += 1
    else:
      break
  else:
    if nums[0] == 10:
      nums[0] = 0
      nums.insert(0, 1)

# Tests:
nums = [4, 2, 3]
increment(nums)
print nums, "424"
nums = [1, 2, 9]
increment(nums)
print nums, "130"
nums = [4, 2, 9, 9, 9]
increment(nums)
print nums, "43000"
nums = [4, 2, 9, 8, 9]
increment(nums)
print nums, "42990"
nums = [9, 9, 9, 9, 9, 9]
increment(nums)
print nums, "1000000"

# Time: 6 minutes

###
# Mistakes / Bugs / Misses
###
# Had == instead of = on line 31
