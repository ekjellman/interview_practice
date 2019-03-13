###
# Problem
###

# Given a set of building heights, return the set of buildings that
# view a sunset. The buildings are in E->W order. Any building to
# the east of a taller building can't view the sunset.
# Buildings are specified by their height.

###
# Work
###
# Unique heights? (Assume yes)
# Number of buildings

def sunset(buildings):
  stack = [float("inf")]
  for b in buildings:
    while b > stack[-1]:
      stack.pop()
    stack.append(b)
  return stack[1:]

# Tests:
print sunset([2, 4, 3, 6, 5, 1]), "6 5 1"
print sunset([]), "[]"
print sunset([7, 5, 3, 2, 1]), "7 5 3 2 1"
print sunset([1, 2, 3, 4, 5]), "5"

# Time: 4 minutes

###
# Mistakes / Bugs / Misses
###
# They said buildings are specified by their height, but then have
# a solution with building ids. If I were going to do that, I'd have
# made a class as well, or at least a (height, id) tuple
# I thought about but did not write what to do if buildings had
# equal height, since I assumed buildings all had unique heights.
