###
# Problem
###

# Given two straight line segments (represented as a start point and an end
# point) compute the point of intersection, if any.

###
# Work
###

# Questions:
# How are the points represented? (Assume x, y tuples)
# What if there are multiple points of intersection? (i.e. overlapping lines)
# (assume any point is fine)
# What if two lines touch at one point, is it considered overlap? (Assume yes?)
# How much do we have to worry about floating point error? (Don't worry about
# it)
# We might also think about if an approximate answer is ok.

# I'm concerned about vertical lines, we'll have to special case it.

# (4 minutes in)
class Point(object):   # Also namedtuple
  def __init__(self, x, y):
    self.x = x
    self.y = y

class LineSegment(object):
  def __init__(self, point_a, point_b):
    if point_a.x <= point_b.x:
      self.start, self.end = point_a, point_b
    else:
      self.start, self.end = point_b, point_a
    if self.start.y == self.end.y:
      self.slope = None
      self.y_intercept = None # Either no intercept, or the whole y axis
    else:
      self.slope = (self.end.y - self.start.y) / (self.end.x - self.start.x)
      self.y_intercept = self.start.y + (-self.start.x * self.slope)

  def contains_x(self, x_intersection):
    return self.start.x <= x_intersection <= self.end.x

  def y_pos_at(self, x_position):
    return self.y_intercept + (self.slope * x_position)

def intersects(start_a, end_a, start_b, end_b): # All Point objects
  # TODO handle vertical lines
  line_a = LineSegment(start_a, end_a)
  line_b = LineSegment(start_b, end_b)
  if line_a.slope == line_b.slope:
    if line_a.y_intercept != line_b.y_intercept:
      return None
    elif # Time ran out here. If the two lines overlap, return a point
  x_intersection = ((line_a.y_intercept - line_b.y_intercept) /
                    (line_b.slope - line_a.slope))
  if line_a.contains_x(x_intersection) and line_b.contains_x(x_intersection):
    return (x_intersection, line_a.y_pos_at(x_intersection))
  else:
    return None

# Time: 25 minutes. (Timed out. FAIL)

###
# Mistakes / Bugs / Misses
###
# Her solution is like mine, but more Javay and without thinking about the
# vertical line case (her line constructor would crash there)
# I don't feel like I did particularly badly here, although tests might have
# revealed problems. I need to be faster.
