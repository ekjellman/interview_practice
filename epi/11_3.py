###
# Problem
###

# Write a program that takes a long sequence of numbers and prints the numbers
# in sorted order. Each number is at most k away from its correctly sorted
# position


###
# Work
###
# Questions
# Size of list and k
# Input / Output types

import heapq

class AlmostSorter(object):
  def __init__(self, k):
    self.heap = []
    self.k = k

  def add_number(self, number):
    heapq.heappush(self.heap, number)
    if len(self.heap) > self.k:
      return heapq.heappop(self.heap)
    else:
      return None

  def clear(self):
    return sorted(self.heap)  # Could repeatedly pop depending on size of k

# Tests
numbers = range(20)
numbers[4], numbers[7] = numbers[7], numbers[4]
numbers[5], numbers[8] = numbers[8], numbers[5]
numbers[11], numbers[15] = numbers[15], numbers[11]
aso = AlmostSorter(4)

result = []
for number in numbers:
  result.append(aso.add_number(number))
result += aso.clear()
print result

# Time: 9 minutes

###
# Mistakes / Bugs / Misses
###
# Had += aso.clear in 44. (TODO: Make card for this kind of bug)
