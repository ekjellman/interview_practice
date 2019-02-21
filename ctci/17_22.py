###
# Problem
###

# Given two words of equal length in the dictionary, write a method to transform
# one word into another by changing only one letter at a time. The new word you
# get each step must be in the dictionary


###
# Work
###
# Error checking? (Assume input is valid) (word length, words are words, etc)
# No answer? (Return None)
# Output? (List of words)
# Do we care about length of chain? (Assume shortest)
# Case / Unicode / Etc  (assume all lowercase ascii)

import collections
import string

def get_word_set(dict_file="/usr/share/dict/words"):
  words = set()
  with open(dict_file, "r") as file_in:
    for line in file_in:
      words.add(line.lower().strip())
  return words

def word_chain(word_set, a, b):
  visited = set()
  backtrack = {}
  queue = collections.deque()
  queue.append(a)
  backtrack[a] = None
  visited.add(a)
  while queue:
    current = queue.popleft()
    for neighbor in get_neighbors(word_set, current):
      if neighbor not in visited:
        queue.append(neighbor)
        backtrack[neighbor] = current
        visited.add(neighbor)
    if b in visited:
      break
  else:
    return None
  path = []
  current = b
  while current:
    path.append(current)
    current = backtrack[current]
  return path[::-1]

def get_neighbors(word_set, s):
  neighbors = set()
  for i in xrange(len(s)):
    for letter in string.ascii_lowercase:
      neighbor = s[:i] + letter + s[i+1:]
      if neighbor in word_set:
        neighbors.add(neighbor)
  return neighbors

# Tests:
word_set = get_word_set()
print word_chain(word_set, "damp", "like")
print word_chain(word_set, "apple", "zebra")
print word_chain(word_set, "zzzzz", "aaaaa")
# Would like a better set of two words not connected

# Time: 22 minutes

###
# Mistakes / Bugs / Misses
###
# Forgot a loop in get_word_set()
# Forgot to add a to visited at 35
# Had reversed(path), which returns a listiterator.
# Original output had a None at the beginning. Fixed. (Because it appended the
# last None, and then reversed)
# Did not consider bidirectional search.
# Did not consider her wildcard solution. I don't think that's actually an
# improvement... generating the list will take O(nl) time where n is the number
# of words and l is the average length. If you could generate it while creating
# the dictionary it might be ok, but even then, making the neighbors at each
# step is O(l), and it's not clear to me it's better.
# Of course, if you're calling this many times and can just hold to the cache
# it's a good idea, so I should remember it.
