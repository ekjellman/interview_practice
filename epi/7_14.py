###
# Problem
###

# Find the first occurrence of a substring

###
# Work
###
# Questions:
# Are we going to be searching the same string a lot? (could cache prefixes up
# to some length, make a trie or some other useful data structure)
# Sizes of string and substring

# I mean, realistically, my answer is this:

def first_occurrence(s, sub):
  return s.find(sub)

# Tests:
print first_occurrence("abc", "xyz")
print first_occurrence("abc", "aabbccababcaacc")
print first_occurrence("aabbccababcaacc", "abc")

# If I'm absolutely pressed to solve this on my own, I'm going to talk about
# a naive solution, then boyer-moore-horspool stuff.

# Time: 6 minutes

###
# Mistakes / Bugs / Misses
###
# Make card for these string algorithms. (TODO)
