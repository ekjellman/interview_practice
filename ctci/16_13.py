###
# Problem
###

# Given two squares in a 2D plane, find a line that bisects them. Assume the
# squares are axis aligned.

###
# Work
###
# Questions:
# What do the Square objects look like? (Assume an upper left corner and a
#   side length)
# Output? (Assume a Line object)
# What does the line object look like? (We'll assume the two points define it)
#   Otherwise we'd have to deal with vertical lines, etc etc
# What to do about errors? (Assume everything is valid)

class Square(object):
  def __init__(self, x, y, side):
    # TODO: Error checking for illegal squares (non-positive side, for example)
    self.x = x
    self.y = y
    self.side = side

class Line(object):
  def __init__(self, x1, y1, x2, y2):
    # TODO: Error check for illegal lines (points are the same?)
    self.x1 = x1
    self.x2 = x2
    self.y1 = y1
    self.y2 = y2

  def __str__(self):
    return " ".join((str(self.x1), str(self.y1),
                     str(self.x2), str(self.y2)))

def bisect_squares(a, b):
  # Any line that goes through the middle of a square bisects it.
  # So we need a line that goes through the middle of both, which is just
  # the line defined by both centers.
  # If both squares have the same center, we would raise an error, which
  # hopefully we'd get from Line
  x1 = a.x + (a.side / 2.0)
  x2 = b.x + (b.side / 2.0)
  y1 = a.y + (a.side / 2.0)
  y2 = b.y + (b.side / 2.0)
  return Line(x1, y1, x2, y2)

# Tests:
# Error case tests, if we were doing them
a = Square(0, 0, 10)   # 5, 5
b = Square(10, 10, 6)  # 13, 13
print bisect_squares(a, b), "(5, 5, 13, 13)"


# Time: 12 minutes

###
# Mistakes / Bugs / Misses
###
# Forgot self at line 35
# Forgot str() at line 35
# Forgot to put the strings in a tuple at line 35
# Didn't think about the option of "line starts at the edge of the squares"
# It does make the problem a little more interesting, but not enough that I
# want to redo it.
