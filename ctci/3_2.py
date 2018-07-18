###
# Problem
###

# Implement a stack which, in addition to push and pop, also has a min function
# that returns the minimum element. push/pop/min should take O(1) time.

###
# Work
###

# Questions:
# Various stack usage questions (capacity? value types? other functions like
#   len or peek?) (Assume no capacity, value types are int, no other functions)
#   (Probably in Java we'd like to use <T> or whatever)

class MinStack(object):
  def __init__(self):
    self._stack = []
    self._min_stack = []

  def push(self, value):
    self._stack.append(value)
    if not self._min_stack or value <= self._min_stack[-1]:
      self._min_stack.append(value)

  def pop(self):
    if not self._stack:
      raise ValueError("Can't pop from empty stack")
    return_value = self._stack.pop()
    if return_value == self._min_stack[-1]:
      self._min_stack.pop()
    return return_value

  def min(self):
    if not self._min_stack:
      raise ValueError("Can't get min of an empty stack")
    # TODO: Implement as __min__? Does that exist?
    return self._min_stack[-1]

import random
ms = MinStack()
for i in xrange(100):
  num = random.random()
  ms.push(num)
  min_num = min(ms._stack)
  assert ms.min() == min_num
for i in xrange(99):
  ms.pop()
  min_num = min(ms._stack)
  assert ms.min() == min_num
assert ms._stack[0] == ms._min_stack[0]

# Time: 12 minutes

###
# Mistakes / Bugs / Misses
###
# Do Python lists have a peek other than [-1]?
# Is there a generic __min__ method for min()?
# Forgot empty stack case for push()
# Used min(ms) instead of ms.min() in test cases
