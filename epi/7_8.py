###
# Problem
###

# Return the nth value in the look-and-say sequence (1, 11, 21, 1211, etc)
# as a string

###
# Work
###
# Questions:
# Possible values of n
# Error checking
# 0 or 1 indexed? (assume 1)

def look_and_say(n):
  i = 1
  s = "1"
  while i < n:
    i += 1
    s = generate_next(s)
  return s

def generate_next(s):
  # TODO: Error checking. Assumes s is not empty
  pieces = []
  current = s[0]
  count = 1
  for i in xrange(1, len(s)):
    if s[i] != current:
      pieces.append(str(count))
      pieces.append(current)
      current = s[i]
      count = 1
    else:
      count += 1
  pieces.append(str(count))
  pieces.append(current)
  return "".join(pieces)

for i in xrange(1, 10):
  print look_and_say(i)

# Time: 8 minutes

###
# Mistakes / Bugs / Misses
###

