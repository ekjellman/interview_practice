###
# Problem
###

# Use a single array to implement three stacks

###
# Work
###

# This problem doesn't fit super well in Python, since lists are not of a
# fixed size.

# The first approach I can think of, which still does work in Python, is to
# use mod. Stack 1 goes in 0, 3, 6, ..., Stack 2 goes in 1, 4, 7, ... and
# Stack 3 goes in 2, 5, 8, .... If adding to a stack would exceed capacity, then
# we can add three to the list.

# If we assume fixed length, we could just divide the list in three 0-(n/3-1)
# and so on.
# Another way that might possibly give better flexibility and capacity is to
# grow one stack from one end of the list, a second from the other end, and
# the third stack from the middle. This is quite complex, however.

# I'll implement the first approach.

class ThreeStackList(object):
  # TODO: Make extensible? (i.e. more or less than three stack)
  def __init__(self, initial_capacity=100):
    self.internal_list = [None] * (initial_capacity * 3)
    self.capacity = initial_capacity
    self.stack_counts = [0, 0, 0]

  def _grow_stack(self):
    self.capacity += 1
    self.internal_list.extend([None] * 3)

  def push(self, stack_number, value):
    # TODO: raise errors instead of assertions
    assert 0 <= stack_number <= 2
    if self.stack_counts[stack_number] >= self.capacity:
      self._grow_stack()
    new_pos = (self.stack_counts[stack_number] * 3) + stack_number
    self.internal_list[new_pos] = value
    self.stack_counts[stack_number] += 1

  def pop(self, stack_number):
    assert self.stack_counts[stack_number] > 0
    self.stack_counts[stack_number] -= 1
    pos = (self.stack_counts[stack_number] * 3) + stack_number
    value = self.internal_list[pos]
    self.internal_list[pos] = None
    return value

a = ThreeStackList()
for i in xrange(600):
  a.push(i % 3, i)
for i in xrange(599, -1, -1):
  value = a.pop(i%3)
  print i, value

# Time: 17 minutes

###
# Mistakes / Bugs / Misses
###
# Ask questions before coding.
# Assertion at line 47 was >= 0. This meant it would look at index -1 if the
#   stack was empty once.
# Did not consider the flexible approach where you allocate/reallocate parts
#   of the list. (Would not have tried to code it regardless)
