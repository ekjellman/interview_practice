###
# Problem
###

# Implement run-length encoding and decoding. Assume the string to be encoded
# is all letters of the alphabet, with no digits, and decoded strings are valid

###
# Work
###
# Questions:
# Length of encoded/decoded strings?
# Deal with digits greater than 9? (assume yes)
# Case matters? (Assume yes)

import string

# Cheeky answer
import itertools
def encode_cheeky(s):
  parts = []
  for k, g in itertools.groupby(s):
    parts.append(str(len(list(g))))
    parts.append(k)
  return "".join(parts)

# Tests
print encode_cheeky("aaabbbbbcc"), "3a5b2c"
print encode_cheeky("aaaabcccaa"), "4a1b3c2a"

def encode(s):
  if not s: return ""
  current = s[0]
  length = 1
  parts = []
  for c in s[1:]:
    if c == current:
      length += 1
    else:
      parts.append(str(length))
      parts.append(current)
      current = c
      length = 1
  parts.append(str(length))
  parts.append(current)
  return "".join(parts)

# Tests
print encode("aaabbbbbcc"), "3a5b2c"
print encode("aaaabcccaa"), "4a1b3c2a"

def decode(s):
  tokens = decode_split(s)
  parts = []
  for l, c in tokens:
    parts.append(c * l)
  return "".join(parts)

def decode_split(s):
  tokens = []
  number = 0
  for c in s:
    if c in string.digits:
      number *= 10
      number += int(c)
    else:
      tokens.append((number, c))
      number = 0
  return tokens

# Tests
print decode("3e4f2e"), "eeeffffee"

import random
for i in xrange(20):
  parts = [random.choice(string.ascii_letters) * random.randint(1, 20) for _ in xrange(random.randint(3,20))]
  s = "".join(parts)
  print s
  e = encode(s)
  print e
  d = decode(e)
  print d
  print s == d

# Time: 18 minutes

###
# Mistakes / Bugs / Misses
###
# Make card for groupby (TODO)
# Forgot [1:] at 34
# I think regex would be good for decode_split. Make a card for it. (TODO)

