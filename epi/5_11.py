###
# Problem
###

# Write a program which tests if two rectangles have a non-empty intersection.
# If the intersection is non-empty, return the rectangle formed by their
# intersection

###
# Work
###
# Questions:
# Input format? (Assume a rectangle object we create)

class Rectangle(object):
  def __init__(self, x1, y1, x2, y2):
    self.x1 = x1
    self.x2 = x2
    self.y1 = y1
    self.y2 = y2

  def __str__(self):
    return "(%d %d %d %d)" % (self.x1, self.y1, self.x2, self.y2)

def intersects(r1, r2):
  # This is the dumb way, but I can't remember/figure out the smart way right now.
  if r1.x1 > r2.x1:
    r1, r2 = r2, r1
  if r1.x2 > r2.x1:
    x_int = (r2.x1, min(r1.x2, r2.x2))
  else:
    return None
  if r1.y1 > r2.y1:
    r1, r2 = r2, r1
  if r1.y2 > r2.y1:
    y_int = (r2.y1, min(r1.y2, r2.y2))
  else:
    return None
  return Rectangle(x_int[0], y_int[0], x_int[1], y_int[1])

# Tests:
a = Rectangle(0, 0, 5, 5)
b = Rectangle(3, 3, 7, 7)
print intersects(a, b), "(3, 3, 5, 5)"
print intersects(b, a), "(3, 3, 5, 5)"
c = Rectangle (5, 5, 10, 10)
print intersects(a, c), "None"
d = Rectangle(1, 1, 4, 4)
print intersects(a, d), "(1, 1, 4, 4)"

# Time: 17 minutes

###
# Mistakes / Bugs / Misses
###
# Mixed up > and < at 27 and 33
# Didn't have mins on 30 and 36
# Make algorithm card (TODO) Don't use their solution, use my book's probably
