###
# Problem
###

# "Hello_World!" in a sinusoidal fashion looks like this:

#  e   _   l
# H l o W r d
#    l   o   !

# Write a program that takes a string, and outputs that string top/bottom
# --> "e_lHloWrdlo!

###
# Work
###

def snake_string(s):
  return s[1::4] + s[::2] + s[3::4]

# Test:
print snake_string("Hello World!"), "e lHloWrdlo!"
print snake_string("Test"), "eTst"
print snake_string("Tes"), "eTs"
print snake_string("Te"), "eT"
print snake_string("T"), "T"

# Time: 2 minutes

###
# Mistakes / Bugs / Misses
###
