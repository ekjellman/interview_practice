###
# Problem
###

# Given a max-heap, design an algorithm that computes the k largest elements
# in the max-heap. You cannot modify the heap.

###
# Work
###
# Questions:
# Size of the heap? Size of k
# Output type? (Assume a list)
# Do the results have to be in order? (Assume no)

# Approaches
# Copy the heap and extract
# Sort the list and extract
# Simulate heap pops

import heapq

def k_largest(max_heap, k):
  # Assume the max_heap has a None in element 0
  if len(max_heap) <= 1: return []
  heap = [(-max_heap[1], 1)]   # Python's heap is a min heap
  result = []
  while len(result) < k and heap:
    number, index = heapq.heappop(heap)
    result.append(-number)
    if len(max_heap) > index * 2:
      heapq.heappush(heap, (-max_heap[index * 2], index * 2))
    if len(max_heap) > index * 2 + 1:
      heapq.heappush(heap, (-max_heap[index * 2 + 1], index * 2 + 1))
  return result

# Test
max_heap = [None, 561, 314, 401, 28, 156, 359, 271, 11, 3]
print k_largest(max_heap, 4)

max_heap = [None, 561]
print k_largest(max_heap, 4)

max_heap = [None]
print k_largest(max_heap, 4)
# Time: (5)

###
# Mistakes / Bugs / Misses
###
# Didn't have cases at 31/33, so I would get array out of bounds.
# (TODO: make bug card?)
# They note in a 0-index heap the positions are 2i + 1, 2i + 2, (TODO: Make card)
