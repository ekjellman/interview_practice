###
# Problem
###

# Given a (largish) number of sorted lists, write a function that
# returns the full sorted list.

# Note: This is an abstraction of the "true" problem, which is to
#       merge multiple large files, so keep that problem in mind.

###
# Work
###
# Questions:
# Number / size of lists

import heapq

# I'm writing this with some functions that would be inefficient
# if they were actually being done on in-memory lists, to make
# testing easier. I'll note them below.
# This destroys the lists
def merge_lists(lists):
  result = []  # Would actually be a file to append to
  heap = []
  for i in xrange(len(lists)):
    heapq.heappush(heap, (lists[i].pop(0), i))  # Would be a file read
  while heap:
    item, list_num = heapq.heappop(heap)
    result.append(item)
    if lists[list_num]:
      heapq.heappush(heap, (lists[list_num].pop(0), list_num))  # file read
  return result

# Tests:
lists = [[3, 5, 7], [0, 6], [0, 6, 28]]
print merge_lists(lists)

# Time: 9 minutes

###
# Mistakes / Bugs / Misses
###

