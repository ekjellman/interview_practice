###
# Problem
###

# Compress a string using the counts of repeated characters.
# EX: "aabcccccaaa" - "a2b1c5a3"
# If the compressed string is not smaller, return the original.
# Assume the string only has uppercase/lowercase letters

###
# Work
###

# Questions:
# Return old string on equal size? (Assume yes)
# Can there be double digits or more of a character in a row? (assume yes)

# Possible optimizations:
# Calculate new string length first?
# itertools.groupby()?
# Abort early if the new_string_pieces are already longer

import itertools
def compress_string(s):
  if not s: return s
  new_string_pieces = []
  current_char = s[0]
  current_count = 1
  for char in s[1:]:
    if char != current_char:
      new_string_pieces.append("%s%d" % (current_char, current_count))
      current_char = char
      current_count = 1
    else:
      current_count += 1
  new_string_pieces.append("%s%d" % (current_char, current_count))
  new_string = "".join(new_string_pieces)
  if len(new_string) >= len(s):
    return s
  return new_string

tests = [("aabcccccaaa", "a2b1c5a3"),
         ("", ""),
         ("abc", "abc"),
         ("aabb", "aabb"),
         ("a" * 10, "a10"),
         ("a" * 100, "a100")]

for s, expected in tests:
  print s, expected, compress_string(s)

# Time: 11 minutes

###
# Mistakes / Bugs / Misses
###

# Oof.
# Forgot lines 34-35
# Forgot [:1] in line 29
# Used > instead of >= on line 38

