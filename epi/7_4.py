###
# Problem
###

# Given a list of characters, apply the following rules:
# Replace every a with two ds
# Remove all bs

# for example: "acdbbca" -> "ddcdcdd"

###
# Work
###
# Questions:
# Extensibility? (other rules, etc)
# Length of string?
# Case? (assume lower)

# Not in place version
def rep_remove(s):
  chars = []
  for c in s:
    if c == "a":
      chars.append("d")
      chars.append("d")  # Or "dd" once, but pretending it's a char array
    elif c == "b":
      continue
    else:
      chars.append(c)
  return "".join(chars)

# Tests:
print rep_remove("acdbbca"), "ddcdcdd"

def rep_remove(chars, size):
  # Remove bs
  char_pointer = 0
  for i in xrange(size):
    if chars[i] == "b":
      continue
    else:
      chars[char_pointer] = chars[i]
      char_pointer += 1
  last_char = char_pointer - 1
  char_pointer = len(chars) - 1
  for i in xrange(last_char, -1, -1):
    if chars[i] == "a":
      chars[char_pointer] = "d"
      chars[char_pointer - 1] = "d"
      char_pointer -= 2
    else:
      chars[char_pointer] = chars[i]
      char_pointer -= 1
  # Move to front
  char_pointer += 1
  for i in xrange(len(chars) - char_pointer):
    chars[i] = chars[i + char_pointer]
  return chars

print rep_remove(list("acdbbca"), 7), "ddcdcdd"
print rep_remove(list("aaaa    "), 4), "dddddddd"
print rep_remove(list("abababab    "), 8), "dddddddd"
print rep_remove(list("cababababc    "), 10), "cddddddddc"


# Time: 4 minutes to not in-place. (11) 22 minutes to full solution
# Looked at hint at :06

###
# Mistakes / Bugs / Misses
###
# overloaded char_pointer at 44-45 (didn't have last_char)
# Didn't pass size
# Forgot to move characters to the front (could have maybe solved a different way)

