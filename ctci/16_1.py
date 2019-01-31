###
# Problem
###

# Write a function to swap a number in place (i.e. without temp variables)

###
# Work
###

# Questions:
# Function? Because especially if we're dealing with Java and Python, things
#   are passed by value and not by reference. (Assume we're just writing the
#   code to do it)

a = 3
b = 2
a, b = b, a   # ;-)
print "(2, 3)", a, b

# More in the spirit of the question, we could do this with addition or xor.
# xor has the bonus that we can probably do it with things other than numbers.

a = 3
b = 2
b = a + b   # a = a, b = a + b
a = b - a   # a = b, b = a + b
b = b - a   # a = b, b = a
print "(2, 3)", a, b

a = 3
b = 2
b = a ^ b   # a = a, b = a ^ b
a = b ^ a   # a = b, b = a ^ b
b = b ^ a   # a = b, b = a
print "(2, 3)", a, b

# Time: 8 minutes

###
# Mistakes / Bugs / Misses
###
# None, I think.
