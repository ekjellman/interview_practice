###
# Problem
###

# We get a stream of integers via a function track(x). We want to be able to
# call getRankOfNumber(x) to find how many values less than or equal to x
# we've seen.

###
# Work
###

# Questions:
# How many numbers are we expecting to see? Will they all fit in memory?
# What is the range of these numbers?
# Time restrictions?
# What do you mean by "less than or equal to x not including x itself"?
#  isn't that just less than x?
#  Note: Apparently it means just don't count one of them.

# Approaches:
# Keep a sorted list and binary search
# Keep a counter and iterate
# Use a binary tree (we'll basically implement this)

class TrackingTree(object):
  def __init__(self, value):
    self.value = value
    self.count = 1
    self.left_count = 0
    self.right_count = 0
    self.left = None
    self.right = None

  def track(self, value):
    # TODO: Balance the tree.
    if self.value == value:
      self.count += 1
    elif self.value > value:  # Go left
      self.left_count += 1
      if self.left:
        self.left.track(value)
      else:
        self.left = TrackingTree(value)
    else: # Go right
      self.right_count += 1
      if self.right:
        self.right.track(value)
      else:
        self.right = TrackingTree(value)

  def get_rank(self, value):
    if self.value == value:
      my_count = 0 if self.count <= 1 else self.count - 1
      return self.left_count + my_count
    elif self.value > value:
      if self.left:
        return self.left.get_rank(value)
      else:
        return 0
    else:
      total_count = self.left_count + self.count
      if self.right:
        total_count += self.right.get_rank(value)
      return total_count

  def print_tree(self, indent=0):
    print " " * indent, self.value, self.count, "(%d %d)" % (self.left_count, self.right_count)
    if self.left:
      self.left.print_tree(indent + 1)
    if self.right:
      self.right.print_tree(indent + 1)

# Tests
tt = TrackingTree(5)
print "0", tt.get_rank(3)
print "0", tt.get_rank(5)
print "1", tt.get_rank(7)
tt.track(1)
tt.track(4)
tt.track(4)
tt.track(5)
tt.track(9)
tt.track(7)
tt.track(13)
tt.track(3)
print "0", tt.get_rank(1)
print "1", tt.get_rank(3)
print "3", tt.get_rank(4)

# Time: 24 minutes

###
# Mistakes / Bugs / Misses
###
# Got logic for the equals case wrong at first
# Didn't increment left_count and right_count when creating the nodes.
# Did not ask about what to do if x is not in the structure. AGAIN.
#   I did handle it, but apparently they wanted it to be an error?
#   This doesn't seem quite correct.
