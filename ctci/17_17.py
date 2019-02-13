###
# Problem
###

# Given a (larger) string b and a list of smaller strings T, design a method
# to search b for each small string in T

###
# Work
###
# Questions:
# Relative sizes of b and items in T (and T itself)
# Input? (assume b and list T)
# Output? (positions of T's strings in b?)
# -- If a string in T appears multiple times in b, what do we do?
#    (return the first one?)
# If a string in T doesn't appear in b, what do we do? (None for that element)

def multi_search_brute(b, t):
  results = []
  for s in t:
    pos = b.find(s)
    if pos != -1:
      results.append(pos)
    else:
      results.append(None)
  return results

"""
# Test
b = "thisisatestlalala"
t = ["this", "is", "a", "test", "la", "pizza"]
print multi_search_brute(b, t), (0, 2, 6, 7, 11, None)
"""

def multi_search(b, t):
  trie = Trie()
  for s in t:
    trie.add(s)
  current_paths = []
  results = {}
  for i, c in enumerate(b):
    current_paths.append(trie)
    new_paths = []
    for path in current_paths:
      child = path.child(c)
      if child is not None:
        new_paths.append(child)
        if child.terminal:
          if child.word not in results:
            results[child.word] = i - len(child.word) + 1  # we get last letter
    current_paths = new_paths
  return results   # TODO: Convert back to list if we care

class Trie(object):
  def __init__(self):
    self.word = None
    self.terminal = False
    self.children = {}

  def add(self, s):
    current = self
    for c in s:
      if c not in current.children:    # TODO: defaultdict?
        current.children[c] = Trie()
      current = current.children[c]
    current.terminal = True
    current.word = s

  def child(self, c):  # TODO: could add use this?
    if c in self.children:
      return self.children[c]
    else:
      return None

# Test
b = "thisisatestlalala"
t = ["this", "is", "a", "test", "la", "pizza"]
print multi_search(b, t), (0, 2, 6, 7, 11, None)

# Time: 25 minutes

###
# Mistakes / Bugs / Misses
###
# Test had 4 for pos of "is", when it's also in "this". Oops.
# Line 65 had self instead of current
# Line 51 calc was wrong
# Lines 47-49 were not under the if.
# This code needs refactoring. >_< But I ran out of time.
