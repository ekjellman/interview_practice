###
# Problem
###

# You have two strings, pattern and value. pattern consists of letters a and b
# describing a patter within a string. For example "catcatgocatgo" matches
# "aabab" with a = "cat" and b = "go". It also matches other patterns.
# Write a method to determine if value matches pattern.

###
# Work
###
# Questions:
# Can a and b be empty? (Assuming no)
# Case, etc (assume case sensitive)
# Extensible?

def matches(pattern, value, pattern_map=None):
  if not pattern: return len(value) == 0
  if pattern_map is None:
    pattern_map = {}
  letter = pattern[0]
  if letter in pattern_map:
    if value.startswith(pattern_map[letter]):
      return matches(pattern[1:], value[len(pattern_map[letter]):], pattern_map)
    else:
      return False
  else:
    for length in xrange(1, len(value) + 1):
      pattern_map[letter] = value[:length]
      result = matches(pattern[1:], value[len(pattern_map[letter]):], pattern_map)
      del pattern_map[letter]
      if result:
        return True
    return False

# Tests
print "All true"
print matches("aabab", "catcatgocatgo")
print matches("bbaba", "catcatgocatgo")
print matches("a", "catcatgocatgo")
print matches("ab", "catcatgocatgo")
print matches("b", "catcatgocatgo")
print "All false"
print matches("aaa", "catcatgocatgo")
print matches("aaaa", "catcatcat")
print matches("aaaa", "catcatcatcatcat")

# Time: 15 minutes

###
# Mistakes / Bugs / Misses
###
# Off by one error at 29. only went to len(value). I need len(value) + 1 to
#   get the whole string (TODO: Make card)
# There are probably some improvements if all letters in pattern are known
# Thought about but did not implement the length optimization for the a and b
#   only case, since I made it more generalized than that.
