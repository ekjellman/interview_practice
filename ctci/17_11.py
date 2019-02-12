###
# Problem
###

# Given a large text file containing words, and two words, find the shortest
# distance between them in the file. If the operation will be repeated
# many times for the same file, can you optimize your solution?

###
# Work
###
# Questions:
# What distance? Bytes? Word indices? (assuming word indices, it would not be
#   hard to modify)
# Input? (For simplicity, assuming list of words)
# Output? (The distance)
# Case sensitivity / unicode / etc? (assume string equality is fine)
# What to do if either word isn't in the file? (Assume return -1)

def word_distance(words, a, b):
  last_a = -1
  last_b = -1
  best_distance = float("inf")
  for i, word in enumerate(words):
    if word == a:
      last_a = i
    elif word == b:
      last_b = i
    else:
      continue
    if last_a == -1 or last_b == -1:
      continue
    best_distance = min(best_distance, abs(last_a - last_b))
  if last_a == -1 or last_b == -1:
    return -1
  return best_distance

# Tests:
print word_distance(["a", "b", "a", "b", "a", "b", "a"], "a", "c"), "-1"
print word_distance(["a", "b", "c", "b", "a", "b", "d"], "d", "c"), "4"
print word_distance(["d", "b", "c", "b", "a", "b", "d"], "d", "c"), "2"
print word_distance(["d", "c", "c", "c", "d", "c", "d"], "d", "c"), "1"
print word_distance(["a", "c", "a", "b", "a", "c", "b"], "b", "c"), "1"

# If the operation would be repeated many times for the same file, we would make
# a hashtable from word -> positions in the file. We could then use those lists
# of positions to calculate the best distance in a merge-sort kind of way. For
# example:

# a: 2 7 10 11 19
# b: 5 8 15 23

# We would compare 2 to 5, then advance a to 7, comparing 7 to 5, etc, until we
# go through both lists (finding distance of 1, with 7 and 8)

# Time: 14 minutes

###
# Mistakes / Bugs / Misses
###
# TODO: Make a card for unicode stuff, in case anyone actually says yes
# TODO: Wasn't sure about enumerate order, make card
# Didn't ask about word 1 or word 2 being first.
