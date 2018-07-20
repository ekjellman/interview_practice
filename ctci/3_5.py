###
# Problem
###

# Write a program to sort a stack such that the smallest items are on top. You
# can use an additional stack, but not another data structure.

###
# Work
###

# Questions:
# Type of items on the stack? (Assume ints)
# Expected number of items on the stack. (Assume unknown)
# What order do we want things on the stack? (Assume smallest on top)

def sort_stack(stack):
  if not stack:
    return stack
  temp_stack = [stack.pop()]
  while stack:
    if not temp_stack or (stack[-1] >= temp_stack[-1]):
      temp_stack.append(stack.pop())
    else:
      reinsert_value = stack.pop()
      while temp_stack and temp_stack[-1] > reinsert_value:
        stack.append(temp_stack.pop())
      stack.append(reinsert_value)  # TODO: Put on temp instead?
  while temp_stack:
    stack.append(temp_stack.pop())

import random
items = [random.randint(0, 100) for _ in xrange(100)]
stack = items[:]
items.sort(reverse=True)
sort_stack(stack)
print items
print stack
print items == stack

# Time: 14 minutes

###
# Mistakes / Bugs / Misses
###
# Line 22: Forgot empty temp_stack case
# Line 26: Forgot empty temp_stack case
# There are probably some small optimizations where I don't have to put things
# back on stack.
