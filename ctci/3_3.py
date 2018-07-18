##
# Problem
###

# Implement a SetOfStacks data structure that works like a stack, but is
# composed of a set of stacks of no more than some size.

###
# Work
###

# Questions:
# Should there also be a capacity of number of stacks? (Assume no)
# More questions on the follow-up will be asked there

class SetOfStacks(object):
  def __init__(self, stack_capacity):
    self._stacks = [[]]
    self.stack_capacity = stack_capacity

  def push(self, value):
    if len(self._stacks[-1]) >= self.stack_capacity:
      self._stacks.append([])
    self._stacks[-1].append(value)

  def pop(self):
    while not self._stacks[-1]:
      if len(self._stacks) > 1:
        self._stacks.pop()
      else:
        raise ValueError("Cannot pop from an empty SetOfStacks")
    return self._stacks[-1].pop()

  # Follow-up: Implement popAt(index) which pops from a specific sub-stack
  # Questions: If a sub-stack is empty, go to the next sub-stack? (assume no)
  #            Should a push fill an earlier stack? (assume no)
  #            If a pop empties a sub-stack, should we remove it? (assume no)
  def popAt(self, stack):
    if stack >= len(self._stacks) or stack < 0:
      raise ValueError("Sub-stack index does not exist")
    if not self._stacks[stack]:
      raise ValueError("Sub-stack is empty")
    return self._stacks[stack].pop()

ss = SetOfStacks(10)
for i in range(100):
  ss.push(i)
assert len(ss._stacks) == 10
for i in range(99, -1, -1):
  value = ss.pop()
  assert value == i

ss = SetOfStacks(10)
for i in range(100):
  ss.push(i)
assert len(ss._stacks) == 10
for i in range(9, -1, -1):
  value = ss.popAt(4)
  assert value == 40 + i
for i in range(99, 49, -1):
  value = ss.pop()
  assert value == i
for i in range(39, -1, -1):
  value = ss.pop()
  assert value == i
# Also tested the ValueErrors


# Time: 11 minutes (19 with popAt and other ValueError tests)

###
# Mistakes / Bugs / Misses
###
# Line 22 was originally > instead of >=
# Line 29 was originally self._stacks[-1].pop()
# Did not really fully consider a left-shift right-shift scheme. I did ask some
#   questions that might lead to it, but it seems really complex to me.
