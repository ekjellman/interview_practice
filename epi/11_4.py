###
# Problem
###

# You have the coordinates of 10**12 stars in a file. How would you find the
# k closest stars to earth?

###
# Work
###

# Not going to write the code for this. You would use a heap to store the
# k closest stars you've seen so far, reading them in from the file.
# If k is really large (greater than the size of memory, for example) you
# would probably have to do an external sort instead.

# Time: 3 minutes

###
# Mistakes / Bugs / Misses
###
# I didn't talk about whether to use a min-heap or a max-heap. You want a max
# heap so that you can easily evict the largest one that you have.
