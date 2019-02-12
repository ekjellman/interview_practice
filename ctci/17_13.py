###
# Problem
###

# Given a set of words and a string without spaces, write a function to split
# the string into words with a minimum number of unrecognized characters.

# Ex: "jesslookedjustliketimherbrother" ->
#     jess looked just like tim her brother (assumedly 7, jess and tim)

###
# Work
###
# Questions:
# Size of input string?
# output? (assume list of strings)
# case? (assume input lowercase)

def get_word_set(dict_file="/usr/share/dict/words"):
  word_set = set()
  with open(dict_file, "r") as file_in:
    for line in file_in.readlines():
      if len(line) > 2:  # Get rid of single letter words
        word_set.add(line.lower().strip())
  return word_set

def respace(s, word_set, cache=None):
  if not s: return (0, [])
  if cache is None:
    cache = {}
  if s in cache:
    return cache[s]
  best_error = float("inf")
  best_split = None
  for i in xrange(1, len(s) + 1):
    error, split = respace(s[i:], word_set, cache)
    if s[:i] not in word_set:
      error += i
    if error < best_error:
      best_error, best_split = error, [s[:i]] + split
  cache[s] = (best_error, best_split)
  return best_error, best_split

# Test:
word_set = get_word_set()
print respace("jesslookedjustliketimherbrother", word_set)
print respace("tzisbeatest", word_set)

# Time: 15 minutes

###
# Mistakes / Bugs / Misses
###
# Forgot colon at line 22
# Had if not cache at line 29, which doesn't work. TODO: make card
# Forgot to ask what to do about multiple solutions
