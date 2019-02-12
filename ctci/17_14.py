###
# Problem
###

# Design an algorithm to find the smallest K numbers in an array.

###
# Work
###
# Size of array and use cases?
# -- Really, the simplest answer is:

"""
def smallest_k(numbers, k):
  return sorted(numbers)[:k]
"""

# And this is likely to be best until the size of the array is huge.

# Otherwise, the answer is going to be something like, in psuedocode:

"""
def smallest_k(numbers, k):
  heap = MaxHeap(numbers[:k])
  for i in xrange(k, len(numbers)):
    if numbers[i] < heap.peek():  # Our number is less than the largest in heap
      heap.push(numbers[i])       # Put the number in
      heap.pop()                  # Remove the largest
  return list(heap)
"""

# Time: 8 minutes

###
# Mistakes / Bugs / Misses
###
# Make a card for python's heap data structure, so I can do more than this.
# I assumed they didn't want me to actually implement a heap.
# I did not think about selection rank
