###
# Problem
###

# Given a sorted list, remove duplicate elements
# ex: [2, 3, 5, 5, 5, 7, 11, 11, 11, 13] -> [2, 3, 5, 7, 11, 13]
# There are no requirements past the last valid element
# Don't use library functions that do this

###
# Work
###
# In place? (Assume yes)

def remove_dups(my_list):
  if len(my_list) <= 1: return
  left_index = 0
  for i in xrange(1, len(my_list)):
    if my_list[i] == my_list[left_index]:
      continue
    else:
      left_index += 1
      my_list[left_index] = my_list[i]
  left_index += 1
  while len(my_list) > left_index:
    my_list.pop()

# Tests:
a = [2, 3, 5, 5, 7, 11, 11, 11, 13]
remove_dups(a)
print a

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
remove_dups(a)
print a

a = []
remove_dups(a)
print a

a = [1]
remove_dups(a)
print a

a = [1, 1, 1, 1, 1, 2, 2, 2, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5]
remove_dups(a)
print a

# Time:

###
# Mistakes / Bugs / Misses
###
# Missed line 24, which caused me to drop the last element of the list.
