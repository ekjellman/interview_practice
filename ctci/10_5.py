###
# Problem
###

# Given a sorted array of strings interspersed with empty strings, write a
# method to find the location of a given string.

###
# Work
###

# Questions:

# What to do if asked to find an empty string? (Assume ignore this for now, but
#   throwing an error would be fine)
# Sorted how? Do I have to worry about case / punctuation / etc? (Assume that
#   comparison operators work)
# What to do if the string isn't found?

def scan_list(string_list, starting_point):
  while starting_point >= 0:
    if string_list[starting_point] == "":
      starting_point -= 1
    else:
      return starting_point
  return -1

def sparse_search(string_list, element):
  low = 0
  high = len(string_list) - 1
  while high >= low:
    mid = (low + high) / 2
    pos = scan_list(string_list, mid)
    if pos != -1 and string_list[pos] == element:
      return pos
    elif pos == -1 or string_list[pos] < element:
      low = mid + 1
    else:
      high = mid - 1
  return -1

# Tests
for i in xrange(20):
  strings = [""] * 20
  strings[i] = "test"
  print i, sparse_search(strings, "test")

strings = ["a", "", "", "bad", "", "test", "", "", "this", "would", "zbe"]
print "-1", sparse_search(strings, "nope")

strings = ["at", "", "", "", "ball", "", "", "car", "", "", "dad", "", ""]
print "0", sparse_search(strings, "at")
print "4", sparse_search(strings, "ball")
print "7", sparse_search(strings, "car")
print "10", sparse_search(strings, "dad")

# Time: 16 minutes

###
# Mistakes / Bugs / Misses
###
# Wasn't sure if comparison operators worked on strings, had to check.
# Didn't ask what to do if the string isn't found. Again.
# Forgot to implement scan_list
# Had scan_list check against the element instead of just looking for a blank
#   spot. This didn't work.
# Forgot to ever return pos
