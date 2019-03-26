###
# Problem
###

# How would you implement a stack with a heap?

###
# Work
###
# Questions:
# Size of stack
# Memory limitations
# Use cases

import heapq

class Stack(object):
  def __init__(self):
    self.heap = []
    self._index = 0

  def push(self, item):
    heapq.heappush(self.heap, (self._index, item))
    self._index -= 1

  def pop(self):
    if self._index == 0: return None
    index, item = heapq.heappop(self.heap)
    self._index += 1
    assert self._index == index
    return item

# Test
stack = Stack()
stack.push(1)
stack.push(2)
print "2", stack.pop()
print "1", stack.pop()
print "none", stack.pop()
print "none", stack.pop()
stack.push(1)
stack.push(2)
print "2", stack.pop()
stack.push(3)
stack.push(4)
print "4", stack.pop()
print "3", stack.pop()
print "1", stack.pop()
print "none", stack.pop()

# Time: 6 minutes

###
# Mistakes / Bugs / Misses
###
