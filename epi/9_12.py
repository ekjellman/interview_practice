###
# Problem
###

# Implement a queue with max API

###
# Work
###
# Questions:
# Unique elements? (Assume no)
# Use cases, etc.

from collections import deque

class MaxQueue(object):
  def __init__(self):
    self.queue = deque()
    self.max_queue = deque()

  def enqueue(self, item):
    self.queue.append(item)
    while self.max_queue and self.max_queue[-1] < item:
      self.max_queue.pop()
    self.max_queue.append(item)

  def dequeue(self):
    # TODO: error checking on deque
    result = self.queue.popleft()
    if self.max_queue[0] == result:
      self.max_queue.popleft()
    return result

  def max(self):
    # TODO: max on empty list
    return self.max_queue[0]

# Tests
import random
cd = deque()
mq = MaxQueue()
for i in xrange(100000):
  if len(cd) == 0 or random.random() > .5:
    item = random.randint(0, 1000000)
    cd.append(item)
    mq.enqueue(item)
  else:
    result = mq.dequeue()
    expected = cd.popleft()
    assert result == expected
    if len(cd) > 0:
      assert mq.max() == max(cd)



# Time: 16 minutes

###
# Mistakes / Bugs / Misses
###
# Forgot to return result at 32
