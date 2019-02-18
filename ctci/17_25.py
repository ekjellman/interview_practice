###
# Problem
###

# Given a list of words, design an algorithm to make the largest possible
# rectangle of letters such that every row forms a word l to r and every col
# forms a word top to bottom.

###
# Work
###
# Questions:
# Case / unicode / etc? (assume everything is lowercase)
# What does "largest rectangle" mean? (assume area)
import collections

def make_word_bins(dict_file):
  bins = collections.defaultdict(set)
  with open(dict_file, "r") as file_in:
    for line in file_in.readlines():
      word = line.lower().strip()
      bins[len(word)].add(word)
  return bins

def make_prefix_sets(word_bins):
  prefix_sets = collections.defaultdict(set)
  for length in word_bins:
    for word in word_bins[length]:
      for i in xrange(1, length + 1):
        prefix_sets[length].add(word[:i])
  return prefix_sets

def get_dimensions(n):
  dimensions = []
  for i in xrange(n, 0, -1):
    for j in xrange(i, 0, -1):
      dimensions.append((i * j, i, j))
  dimensions.sort(reverse=True)
  return [(y, z) for (x, y, z) in dimensions]

def largest_rectangle(dict_file="/usr/share/dict/words"):
  word_bins = make_word_bins(dict_file)
  prefix_sets = make_prefix_sets(word_bins)
  max_area = 0
  longest_word = max(word_bins.keys())
  # Two approaches: For each word length, find the largest rectangle possible
  #                 Or, go rectangle by rectangle.
  dimensions = get_dimensions(longest_word)
  for r, c in dimensions:
    print "Trying %d x %d" % (r, c)
    rectangle = make_rectangle(r, c, word_bins, prefix_sets)
    if rectangle:
      return rectangle

def check_rectangle(current_rectangle, prefix_set):
  for ci in xrange(len(current_rectangle[0])):
    prefix = "".join(word[ci] for word in current_rectangle)
    if prefix not in prefix_set:
      return False
  return True

def make_rectangle(r, c, word_bins, prefix_sets, current_rectangle=None):
  if current_rectangle is None:
    current_rectangle = []
  if len(current_rectangle) == c:
    return current_rectangle
  for word in word_bins[r]:
    current_rectangle.append(word)
    if check_rectangle(current_rectangle, prefix_sets[c]):
      rectangle = make_rectangle(r, c, word_bins, prefix_sets, current_rectangle)
      if rectangle:
        return rectangle
    current_rectangle.pop()
  return None

print largest_rectangle()

# Possible optimizations
# Assume square
# Assume symmetric
# A trie might be faster than the prefix set slightly, hard to tell.
# Parallelize


# Time: 31 minutes (+ run time)

###
# Mistakes / Bugs / Misses
###
# Couldn't remember how to do the custom comparator for get_dimensions (TODO CARD)
# Had extra colon on line 26
# Couldn't remember if line 39 worked, make card (TODO)
# Forgot colon on line 69
