###
# Problem
###

# Reverse the words in a string (words are separated by whitespace)
# We do not need to keep the original string

###
# Work
###
# Questions:
# Am I getting a string or a character array? If it's a string, I might as well
# not do it in place since Strings are immutable. (Assume char array)
# Size of string?
# Punctuation? (Assume goes with the word)
# What is whitespace? (assume actual literal space character)

def reverse_words(chars):
  reverse_range(chars, 0, len(chars) - 1)
  start = 0
  try:
    end = chars.index(" ")
  except ValueError:
    reverse_range(chars, 0, len(chars) - 1)
    return
  while end != -1:
    reverse_range(chars, start, end - 1)
    start = end + 1
    try:
      end = chars.index(" ", start)
    except ValueError:
      break
  reverse_range(chars, start, len(chars) - 1)

def reverse_range(chars, start, end):
  # TODO: error checking
  while start < end:
    chars[start], chars[end] = chars[end], chars[start]
    start += 1
    end -= 1

# Tests:
chars = list("Alice likes Bob")
reverse_words(chars)
print chars

chars = list("   Alice likes   Bob ")
reverse_words(chars)
print chars

chars = list("      AlicelikesBob    ")
reverse_words(chars)
print chars

chars = list("    ")
reverse_words(chars)
print chars

chars = list("")
reverse_words(chars)
print chars

chars = list("AliceLikesBob")
reverse_words(chars)
print chars
# Time: Didn't track start. 15 minutes

###
# Mistakes / Bugs / Misses
###
# Thought list had a find() method. It does not. (TODO: make card)
# Failed when string was one word with no spaces. Added line 24
# I probably should have just written a find method instead of the try/except
