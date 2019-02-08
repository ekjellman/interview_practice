###
# Problem
###

# A list contains all the numbers from 0 to n, except for one number which
# is missing. We cannot access an entire integer from the list in a single
# operation, we can only access them with "fetch the jth bit of element i" which
# takes O(1) time. Write the code to find the missing integer in O(n) time.

###
# Work
###
# Questions:
# -- n is elements in the list?
# -- Size of n
# -- List sorted? (Assume no)

# Approaches:
# Doing the sum thing is O(n log n) now (since it takes log n time to read the
#  "average" number on the list.
# Can we do other stuff like store candidate indices in a list? (Assuming no)
# 

def fetch_bit(number, bit):
  return number & (1 << bit)

# I have an idea for an approach, but I couldn't work out the details in time.
# The idea would be, scan the lsb of each number. We should know how many zeros
# and ones we expect to have from 0-n. We'll be missing a zero or a one. Discard
# all the numbers with the lsb we're not missing. Repeat for the next bit
# until we find the missing number.

# Time: 25 minutes (failed)

###
# Mistakes / Bugs / Misses
###
# Instead of flailing over the exact number of 0s and 1s I should have had for
# each bit and trying to come up with an exact intuitive elegant answer, I
# should have
# -- First, separated it out into a function, and wrote the rest of the code
# -- Then, taken just an absolutely blunt approach to it, and refined

# Instead, I wasted 10-15 minutes thinking about the formula, and got nothing
# written.  TODO: Make card
# TODO: Study solution
