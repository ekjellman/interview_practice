###
# Problem
###

# Solve Towers of Hanoi. Write a program to move the disks from the first
# tower to the third.

###
# Work
###

# Questions:
# What do you mean "move"? (I'm going to just print the moves)
# Size of tower?
# Optimizations using multiple other towers?

def move(size, first_tower, end_tower, spare_tower):
  if size == 1:
    print "move 1 from %d to %d" % (first_tower, end_tower)
    return
  move(size - 1, first_tower, spare_tower, end_tower)
  print "move %d from %d to %d" % (size, first_tower, end_tower)
  move(size - 1, spare_tower, end_tower, first_tower)

# Test
move(3, 1, 3, 2)

# Time: 8 minutes

###
# Mistakes / Bugs / Misses
###
# Forgot to return after the base case
