###
# Problem
###

# Write a function that removes all of a given element from an array.
# Don't use library functions that do this.
# Do it in place. Elements past the last valid element do not matter.

###
# Work
###
# Questions
# Size of array?
# Expected number of removals?

def remove(my_list, element):
  left_index = 0
  for i in xrange(len(my_list)):
    if my_list[i] == element:
      continue
    else:
      my_list[left_index] = my_list[i]
      left_index += 1
  while len(my_list) > left_index:
    my_list.pop()

a = [5, 3, 7, 11, 2, 3, 13, 5, 7]
remove(a, 3)
print a

a = [3, 3, 3, 3, 3, 3, 3, 3]
remove(a, 3)
print a

a = [4, 3, 3, 3, 3, 3, 3, 3]
remove(a, 3)
print a

a = [3, 3, 3, 4, 3, 3, 3, 3]
remove(a, 3)
print a

a = [3, 3, 3, 3, 3, 3, 3, 4]
remove(a, 3)
print a

# Time: 5 minutes

###
# Mistakes / Bugs / Misses
###

