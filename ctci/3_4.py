###
# Problem
###

# Implement a MyQueue class which implements a queue using two stacks

###
# Work
###

# Questions:
# -- Use cases
# -- Required methods (assume poll and offer)
# -- Handling error cases
# -- Capacity? (Assume no)

class MyQueue():
  def __init__(self):
    self._input_stack = []
    self._queue_stack = []

  def offer(self, value):
    self._input_stack.append(value)

  def _fill_queue_stack(self):
    while self._input_stack:
      self._queue_stack.append(self._input_stack.pop())

  def poll(self):
    if not self._queue_stack:
      self._fill_queue_stack()
    if not self._queue_stack:
      raise ValueError("Cannot poll from an empty MyQueue")
    return self._queue_stack.pop()

import random
queue = []
my_queue = MyQueue()
for i in range(200):  # Reduce to make errors more likely
  value = random.random()
  queue.append(value)
  my_queue.offer(value)
for i in range(10000):
  if random.random() > .5:
    if len(queue) == 0:
      print "Expect an error"
    assert my_queue.poll() == queue.pop(0)
  else:
    value = random.random()
    queue.append(value)
    my_queue.offer(value)


# Time: 14 minutes

###
# Mistakes / Bugs / Misses
###
