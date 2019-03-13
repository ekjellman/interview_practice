###
# Problem
###

# Implement a queue using stacks

###
# Work
###
# Questions:
# Size of stacks, use cases, blah blah

class StackQueue(object):
  def __init__(self):
    self.stack = []
    self.holder = []

  def enqueue(self, item):
    self.stack.append(item)

  def dequeue(self):
    if not self.stack and not self.holder:
      raise ValueError("Dequeue on empty queue")
    if not self.holder:
      while self.stack:
        self.holder.append(self.stack.pop())
    return self.holder.pop()

# Tests:
sq = StackQueue()
sq.enqueue(1)
sq.enqueue(2)
sq.enqueue(3)
print "1", sq.dequeue()
sq.enqueue(4)
sq.enqueue(5)
print "2", sq.dequeue()
print "3", sq.dequeue()
print "4", sq.dequeue()
print "5", sq.dequeue()
try:
  sq.dequeue()
except ValueError:
  print "Successfully threw"


import collections
import random
sq = StackQueue()
cd = collections.deque()
for i in xrange(100000):
  if len(cd) == 0 or random.random() > .5:
    item = random.randint(0, 1000000)
    cd.append(item)
    sq.enqueue(item)
  else:
    expected = cd.popleft()
    result = sq.dequeue()
    assert expected == result

# Time:

###
# Mistakes / Bugs / Misses
###
# Had def instead of class for StackQueue
# line 22 had not self.stack and self.holder instead of not both
