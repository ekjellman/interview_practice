###
# Problem
###

# Sort a stack in descending order. Use O(1) memory.
# You can only use push, pop, peek, and checking if the stack is empty

###
# Work
###
# Questions:
# Do I assume there's another stack or that I can create another stack?
# (Assume yes, because I can't see how to do it otherwise)

def stack_sort(stack):
  if not stack: return stack
  holder = []
  while True:
    holder.append(stack.pop())
    while stack and stack[-1] <= holder[-1]:
      holder.append(stack.pop())
    if not stack: break
    new_element = stack.pop()
    while holder and new_element >= holder[-1]:
      stack.append(holder.pop())
    stack.append(new_element)
    while holder:
      stack.append(holder.pop())
  while holder:
    stack.append(holder.pop())

# Tests:
stack = [4, 6, 3, 2, 9, 5]
stack_sort(stack)
print stack

import random
for _ in xrange(10):
  stack = [random.randint(0, 20) for _ in xrange(20)]
  result = sorted(stack)
  stack_sort(stack)
  print result
  print stack
  print result == stack

# Time: 13 minutes

###
# Mistakes / Bugs / Misses
###
# Had => instead of >= in 24
# Their answer is recursive (TODO: Make card)
