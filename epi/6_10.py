###
# Problem
###

# Given an array A and a permutation P, apply P to A.
# A permutation P is an array that specifies the location of each element in
# a permuation. Example: A = [A, B, C, D], P = [2, 0, 1, 3], after application
# the array is [B, C, A, D]

###
# Work
###
# Questions:
# How large is A? (the straightforward answer is just to make a new array and
# copy items into the correct spots) (Assume we want to do it in place)
# Error checking? (Is the permutation valid?
# Can I modify P? (Assume yes, discuss after)

def apply(my_list, p):
  # TODO: Error checking:
  for i in xrange(len(p)):
    if p[i] is None or p[i] < 0:
      continue
    else:
      next_index = p[i]
      current_index = i
      storage = my_list[current_index]
      first_element = None
      while next_index is not None and next_index > 0:
        storage, my_list[next_index] = my_list[next_index], storage
        if p[current_index] != 0:
          p[current_index] = -p[current_index]
        else:
          p[current_index] = None   # "-0"
        current_index = next_index
        next_index = p[next_index]
        if next_index is None:
          next_index = 0

a = list("ABCDEF")
p = [1, 0, 3, 2, 5, 4]
apply(a, p)
print a

a = list("ABCD")
p = [2, 0, 1, 3]
apply(a, p)
print a

# Time: 25 minutes (failed)

###
# Mistakes / Bugs / Misses
###
# The current solution misplaces the first element. I didn't get a solution in
# time, I'm kind of stupidly tired. (TODO: Make card)
# The approach was basically right. However, instead of my stupid None hack, I
# should have just subtracted the length of the array to make it negative.
