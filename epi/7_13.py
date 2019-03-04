###
# Problem
###

# Write a function that takes a filename and a number of lines to be printed,
# and prints the last k lines of a file (i.e. the UNIX tail command)

###
# Work
###
# Expected sizes of file and k?
# Is Python's definition of "line" ok? (assume yes)

# Two approaches: Read from the start of the file using readlines, keep the last
#                 k lines. Use a deque for performance

import collections

def tail(filename, k):
  # TODO: error checking (filename, value of k)
  lines = collections.deque()
  with open(filename, "r") as file_in:
    for line in file_in.readlines():
      if len(lines) < k:
        lines.append(line)
      else:
        lines.append(line)
        lines.popleft()
  for line in lines:
    print line,

# Test
tail("/usr/share/dict/words", 10)

# Or: Read from the end, looking for linebreaks.
# This is probably worse in some sense, because the buffering won't be as good
# or it's not the expected usecase. But it might be better for really large
# files.
# Can improve this by implementing my own buffering, for example.
import os
def tail(filename, k):
  with open(filename, "r") as file_in:
    file_in.seek(-1, os.SEEK_END)
    pos = file_in.tell()
    lines = []
    current_line = []
    while len(lines) < k and pos >= 0:
      file_in.seek(pos)
      c = file_in.read(1)
      if c == "\n":
        if lines or current_line:
          current_line.reverse()
          lines.append("".join(current_line))
          current_line = []
      else:
        current_line.append(c)
      pos -= 1
    if pos < 0:
      current_line.reverse()
      lines.append("".join(current_line))
    lines.reverse()
    print lines
    for line in lines:
      print line

# Test
tail("/usr/share/dict/words", 10)
tail("./short", 10)

# Time: 25 minutes

###
# Mistakes / Bugs / Misses
###
# didn't have , on at line 30, this inserts an extra linebreak we don't want
# I absolutely didn't know how to seek to the end of a file. TODO: Card
# Forgot colon at 57
# Line 51 feels fragile. want more tests.
