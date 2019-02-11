###
# Problem
###

# Given an array filled with letters and numbers, find the longest subarray
# with an equal number of letters and numbers

###
# Work
###
# Questions:
# Longest contiguous subarray? (Assume yes)
# What are letters? (assume numbers are 0-9 and everything else is a letter)
# Length of array?
# Input? (Assume string)
# Output? (Assume string)

# Approaches
# n**2 brute force
# Can't think of any way to do it by shrinking the sides.
# Can you count the whole thing and shrink the sides? I don't think this works
# There might be a slight optimization in grouping letters and numbers and then
# dealing with the groups, but I don't think it makes it better asymptotically.
# A similar thing can be done with keeping a list of just the number or letter
# positions.

# Brute force
def longest_substring(s):
  NUMBERS = "0123456789"
  best_substring = ""
  # TODO: Can abort early i and j loops if we can't find something better
  for i in xrange(0, len(s)):
    letter_count = 0
    number_count = 0
    for j in xrange(i, len(s)):
      if s[j] in NUMBERS:
        number_count += 1
      else:
        letter_count += 1
      if letter_count == number_count and letter_count + number_count > len(best_substring):
        best_substring = s[i:j+1]
  return best_substring

# Tests:
# best substring at start and end
print longest_substring("1a1a1aaaaaaaaa"), "1a1a1a"
print longest_substring("11111111a1a1a"), "1a1a1a"
print longest_substring("1aa11a111aa1111a1a"), "aa11a111aa"

# Time: 14 minutes to brute force (including thinking time)
# I spent a few more minutes looking for a better approach, but couldn't come
# up with anything. (FAILED)

###
# Mistakes / Bugs / Misses
###
# Didn't remember how to get a list of numbers out of string module. TODO
# The best solution is to keep a hashtable with the key
# (letter_count - number_count) and the value is the first time that difference
# appeared. As you go through the array, when you see a diffference, you can
# see when the first time that difference appeared is, and that gives you the
# beginning of a substring with equal numbers and letters.
# For example, if your array starts with "aaaa", that's a difference of 4. Later
# if you see a difference of 4 again, it means the number and letters counts
# from this beginning to there are equal.
# TODO make a card.
