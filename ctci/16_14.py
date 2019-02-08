###
# Problem
###

# Given a two-dimensional graph with points on it, find a line which passes
# through the most points.

###
# Work
###
# Questions:
# How many points? (If the number is small enough, go with a O(n**3) approach)
# Is a little bit of error ok? (Assume yes, to allow for a binning approach)
# What if many lines have the same number of points? (assume pick any)

import collections

class Point(object):
  def __init__(self, x, y):
    self.x = x
    self.y = y

class Line(object):
  def __init__(self, a, b):  # Two Points
    x_diff = b.x - a.x
    y_diff = b.y - a.y
    if x_diff == 0:
      self.slope = None
      self.y_intercept = None
      self.x_value = a.x
    else:
      self.slope = y_diff / float(x_diff)
      self.y_intercept = a.y - (a.x * self.slope)
      self.x_value = None
      self.slope = round(self.slope, 5)
      self.y_intercept = round(self.y_intercept, 5)

  def get_tuple(self):
    return (self.slope, self.y_intercept, self.x_value)

def most_lines(points):
  bucket = collections.defaultdict(set)
  for i in xrange(len(points)):
    for j in xrange(i + 1, len(points)):
      line = Line(points[i], points[j])
      bucket[line.get_tuple()].add(points[i])
      bucket[line.get_tuple()].add(points[j])
  largest_bucket = None
  largest_count = 0
  for line in bucket:
    if len(bucket[line]) > largest_count:
      largest_bucket, largest_count = line, len(bucket[line])
  return largest_bucket, largest_count

# Tests:
# Test Line. Omitted because the points test the vertical case, but we'd want
# to test a few things there. (mostly the rounding and vertical cases)
# Test solution
points = (Point(0, 0), Point(1, 1), Point(2, 2), Point(2, 3), Point(3, 2), Point(3, 3))
print most_lines(points)

# Time: 21 minutes

###
# Mistakes / Bugs / Misses
###
# Not sure how round function works
# TODO: There's a way to do the defaultdict thing without defaultdict. Make a
#       card for it
# Had x.diff instead of x_diff at line 32
# forgot () for get_tuple at 46, 47
# Should have had epsilon configurable
