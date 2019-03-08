###
# Problem
###

# Implement a stack with a max function

###
# Work
###
# Questions:
# Space/Time tradeoffs? (Assume O(1) time for max(), regardless of
#   additional space
# Size of stack?
# Types of items?
# Use cases?
# Desired API (Assume push / pop / max)

class MaxStack(object):
  # TODO: Error checking. popping on empty stacks, max on empty stacks
  def __init__(self):
    self._stack = []
    self._max_stack = []

  def push(self, item):
    self._stack.append(item)
    if not self._max_stack or item >= self._max_stack[-1]:
      self._max_stack.append(item)

  def pop(self):
    item = self._stack.pop()   # Or remove last
    if item == self._max_stack[-1]:
      self._max_stack.pop()
    return item

  def max(self):
    return self._max_stack[-1]

# Test
import random
for _ in xrange(100):
  a = []
  ms = MaxStack()
  for i in xrange(1000):
    item = random.randint(0, 1000)
    a.append(item)
    ms.push(item)
  for i in xrange(1000):
    assert max(a) == ms.max()
    assert a.pop() == ms.pop()

# Time: 10 minutes

###
# Mistakes / Bugs / Misses
###
# Did not think about pushing onto an empty stack for max_stack (TODO: make card)
# Forgot to return the item for pop (TODO: make card)
