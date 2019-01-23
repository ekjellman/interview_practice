###
# Problem
###

# In an array of integers, a peak is an element which is greater than or
# equal to the adjacent integers, and a valley is less than or equal to the
# adjacent integers. Take in an array, and sort it into an alternating
# sequence of peaks and valleys

###
# Work
###

# Questions:
# Size of the array?
# Any sort of extensibility?
# Return type for odd input? (array with no entries, for example)
# Modify the list in place? (Assuming yes)

def alternating_sort(numbers):
  for i in xrange(1, len(numbers) - 1):
    # Split out into a function?
    if numbers[i - 1] > numbers[i] and numbers[i] > numbers[i + 1]:
      numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
    elif numbers[i - 1] < numbers[i] and numbers[i] < numbers[i + 1]:
      numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]

# Other approaches:
# Sort, then take alternating from both ends

# Tests:
numbers = []
alternating_sort(numbers)
print "()", numbers

numbers = [1, 2, 3, 4, 5, 6]
alternating_sort(numbers)
print "(1 3 2 5 4 6)", numbers

numbers = [5, 3, 1, 2, 3]
alternating_sort(numbers)
print "(5 1 3 2 3)", numbers

# If I were actually writing tests for this, I would probably write a verifier
# and test using that, since there are multiple possible valid answers for a
# given list of numbers. This would also let me add some random testing.

# Time: 10 minutes

###
# Mistakes / Bugs / Misses
###
# None?
