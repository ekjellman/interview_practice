###
# Problem
###

# You're placing k planks of wood end to end. There are two types of planks,
# one shorter of length s, one longer of length l. You must use exactly k
# planks of wood, Generate all possible total plank lengths.

###
# Work
###
# Questions:
# Extensibility? (Assume we're not worried about it)
# What to do with invalid input? Like negative plank lengths, negative values
# of k, etc. (Don't worry about it)
# What do you want as output? It says "generate" (Return a list)

def diving_board(k, s, l):
  if l - s == 0: return [k * s]
  return range(k*s, k*l+1, l-s)

print "[0]", diving_board(0, 3, 5)
print "[9, 11, 13, 15]", diving_board(3, 3, 5)
print "[9]", diving_board(3, 3, 3)

# Time: 4 minutes

###
# Mistakes / Bugs / Misses
###
# Did not think about the short == long case. My original code broke on that,
# untill I added line 19
