###
# Problem
###

# Implement a circular queue using an array, and start/end indices.
# Implement dynamic sizing

###
# Work
###
# Questions:
# API? (it says enqueue, dequeue, size functions)

class CircularQueue(object):
  def __init__(self, size):
    self.size = size
    self._list = [None] * self.size
    self.start = 0
    self.end = 0
    self.items = 0

  def dequeue(self):
    if self.items == 0:
      raise ValueError("dequeue() called on empty queue")
    result = self._list[self.start]
    self.start = (self.start + 1) % self.size
    self.items -= 1
    return result

  def enqueue(self, item):
    if self.items == self.size:
      self._grow()
    self._list[self.end] = item
    self.end = (self.end + 1) % self.size
    self.items += 1

  def _grow(self):
    new_list = (self._list[self.start:] + self._list[:self.end] +
                [None] * self.size)
    self._list = new_list
    self.start = 0
    self.end = self.items
    self.size *= 2

  def __len__(self):
    return self.items

# Tests:
cq = CircularQueue(1)
cq.enqueue(0)
cq.enqueue(1)
cq.enqueue(2)
cq.enqueue(3)
cq.enqueue(4)
print cq._list, "0 1 2 3 4 N N N"
print "0", cq.dequeue()
print "1", cq.dequeue()
print "2", cq.dequeue()
print "3", cq.dequeue()
print "4", cq.dequeue()
cq.enqueue(0)
cq.enqueue(1)
cq.enqueue(2)
cq.enqueue(3)
cq.enqueue(4)
print cq._list, "3 4 x x x 0 1 2"
print "0", cq.dequeue()
print "1", cq.dequeue()
print "2", cq.dequeue()
print "3", cq.dequeue()
print "4", cq.dequeue()
try:
  cq.dequeue()
except ValueError:
  print "successfully threw"

import collections
import random
cq = CircularQueue(1)
cd = collections.deque()
for i in xrange(100000):
  if len(cd) == 0 or random.random() > .1:
    item = random.randint(0, 10000000)
    cd.append(item)
    cq.enqueue(item)
  else:
    expected = cd.popleft()
    result = cq.dequeue()
    assert expected == result

# Time: 22 minutes

###
# Mistakes / Bugs / Misses
###
# Forgot self on _grow
# Forgot to assign new_list to _list
# Didn't use self.items for dequeue error case (was self.start == self.end)
