###
# Problem
###

# Given a list of words, write a program to find the longest word made of other
# words in the list

###
# Work
###
# Questions:
# case? (assume everything lower)
# ascii/unicode/etc (assume everything ascii)
# Ties? (assume return any word)

def longest_word(word_set):
  # optional
  word_list = list(word_set)
  word_list.sort(key=len, reverse=True)
  for word in word_list:
    if splitable(word, word_set):
      return word
  return None

def can_split(word, word_set):
  # TODO: caching
  for i in xrange(1, len(word)):  # not including whole word
    front = word[:i]
    back = word[i:]
    if front in word_set:
      if back in word_set: return True
      if can_split(back, word_set): return True
  return False

def get_word_set(dict_file="/usr/share/dict/words"):
  word_set = set()
  with open(dict_file, "r") as file_in:
    for line in file_in:
      if len(line) > 2:  # Ignore single character words
        word_set.add(line.lower().strip())
  return word_set

# Tests
word_set = get_word_set()
print longest_word(word_set)

word_set = set(("this", "is", "a", "test"))
print longest_word(word_set), "None"

word_set = set(("this", "is", "a", "test", "for", "mal", "formal", "formality"))
print longest_word(word_set), "formal"

# Time: 13 minutes

###
# Mistakes / Bugs / Misses
###
# Didn't think about ties until coding
