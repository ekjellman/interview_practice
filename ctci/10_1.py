###
# Problem
###

# Given two sorted lists, A and B, where A has enough buffer at the end to
# hold B, merge A and B

###
# Work
###

# Questions:
# In place? (Assume yes)
# Sizes of A and B
# Types of items?

# Simple coding solution: Copy B into A, sort. O(n log n)
# Let's do what we're supposed to do for an O(n) solution, though.

def merge(a, a_length, b):
  assert len(a) == len(b) + a_length
  a_pointer = a_length - 1
  b_pointer = len(b) - 1
  merge_pointer = len(a) - 1
  while a_pointer >= 0 and b_pointer >= 0:
    if a[a_pointer] > b[b_pointer]:
      a[merge_pointer] = a[a_pointer]
      a_pointer -= 1
      merge_pointer -= 1
    else:
      a[merge_pointer] = b[b_pointer]
      b_pointer -= 1
      merge_pointer -= 1
  while a_pointer >= 0:
    a[merge_pointer] = a[a_pointer]
    a_pointer -= 1
    merge_pointer -= 1
  while b_pointer >= 0:
    a[merge_pointer] = b[b_pointer]
    b_pointer -= 1
    merge_pointer -= 1

# Tests:
a = [1, 2, 3, 4, None, None, None, None]
b = [5, 6, 7, 8]
merge(a, 4, b)
print a

a = [5, 6, 7, 8, None, None, None, None]
b = [1, 2, 3, 4]
merge(a, 4, b)
print a

a = [None, None, None, None]
b = [1, 2, 3, 4]
merge(a, 0, b)
print a

a = [1, 2, 3, 4]
b = []
merge(a, 4, b)
print a

a = [1, 2, 3, 4, None, None, None, None]
b = [1, 2, 3, 4]
merge(a, 4, b)
print a

# Time: 22 minutes. I had a working solution in 12 minutes, but with the
#       code duplication above. I tried to get rid of it but failed, which
#       feels really dumb.

###
# Mistakes / Bugs / Misses
###
# Forgot to move merge pointer
# Didn't handle the end of the merge properly (when only items from one list
#   remain)
# Gayle's solution is cleaner and deals with the code duplication problem.
"""
# Modified solution based on Gayle's solution
def merge(a, a_length, b):
  assert len(a) == len(b) + a_length
  a_pointer = a_length - 1
  b_pointer = len(b) - 1
  merge_pointer = len(a) - 1
  while b_pointer >= 0:
    if a_pointer >= 0 and a[a_pointer] > b[b_pointer]:
      a[merge_pointer] = a[a_pointer]
      a_pointer -= 1
    else:
      a[merge_pointer] = b[b_pointer]
      b_pointer -= 1
    merge_pointer -= 1
"""
# I'm actually not going to fail myself on this one, but I do feel dumb and want
# to remember this solution. TODO
