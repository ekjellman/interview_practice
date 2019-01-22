###
# Problem
###

# Sort an array of strings so that anagrams are next to each other.

###
# Work
###

# Questions:
# Do we care about spacing?
# Do we care about case?
# Number of strings to sort?

# For this problem, we'll assume all the strings are actually lowercase a-z.
# We can modify the comparator if we want.

def group_anagrams(strings):
  return sorted(strings, key=sorted)

# Tests
print group_anagrams(["ace", "cab", "eca", "bac", "eac", "abc", "", "test"])

# Time: 3 minutes.
# Note: If we wanted to handle spacing / case / etc, we could just make a
#       function that returned the canonical version of the string, and use that
#       for key.

###
# Mistakes / Bugs / Misses
###
# I got cute with my one-line solution, so I didn't think about bucketing by
# anagram. That would have been a better solution. I'm not going to fail this,
# but I want to make a card for it. TODO
