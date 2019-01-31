###
# Problem
###

# Design a method to find the frequencies of occurrences of any given word in
# a book. What if we were running this algorithm multiple times?

###
# Work
###

# Questions:
# Do we have to do any preprocessing? (i.e. do we have to worry about
# splitting the text into words, stemming issues, upper/lower case, punctuation,
# etc etc. Let's assume we get the text as a list of pre-processed words)
# How many words are in a book?
# Are we just doing this with one book, or multiple? (Let's think about one
# book for now)

# In the first case, the best we can do is a linear scan. Something like

# return words.count(word)

# In the second case, we can preprocess the book.

import collections

class WordFrequencies(object):
  def __init__(self, word_list):
    self.counter = collections.Counter(word_list)

  def word_count(self, word):
    # TODO: possibly canonicalize word
    return self.counter[word]

# This creates a hashtable from word -> word count, which will be an O(s)
# lookup where s is the length of the word.

# Time: 6 minutes

###
# Mistakes / Bugs / Misses
###
# Thought about but did not ask what to do if the word is not in the book.
# I guess that's slightly better. >_<


