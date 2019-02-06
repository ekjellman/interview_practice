###
# Problem
###

# You have an ant on an infinite grid of white and black squares. It starts
# facing right. At each step, it does the following:

# -- On a white square, flip the color of the square, turn 90 degrees right,
#    and move forward one.
# -- On a black square, flip the color of the square, turn 90 degrees left, and
#    move forward one unit.

# Write a program to simulate the first K moves the ant makes, and print the
# final board as a grid. All you are given is K.

###
# Work
###
# Questions:
# limits of K? (assume memory isn't a problem)
# What is the initial state of the grid? (Assuming a checkerboard, with the
#  starting square being white?)
# What do we print? (assume a square of the furthest the ant has been)

class Board(object):
  # white = 0, black = 1
  def __init__(self):
    self.board = {}
    self.min_coord = 0
    self.max_coord = 0
    self.board[(0, 0)] = 0

  def get(self, x, y):
    if (x, y) in self.board: return self.board[(x, y)]
    #color = (x + y) % 2
    return 0

  def flip(self, x, y):
    color = self.get(x, y)
    color = (color + 1) % 2
    self.board[(x, y)] = color
    self.update(x, y)

  def update(self, x, y):
    self.min_coord = min(self.min_coord, x, y)
    self.max_coord = max(self.min_coord, x, y)

  def print_board(self):
    for y in xrange(self.max_coord, self.min_coord - 1, -1):
      for x in xrange(self.min_coord, self.max_coord + 1):
        print "O."[self.get(x, y)],
      print

def print_k_moves(k):
  DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
  board = Board()
  ant_x = 0
  ant_y = 0
  ant_dir = 1
  for move in xrange(k):
    color = board.get(ant_x, ant_y)
    board.flip(ant_x, ant_y)
    if color == 0:  # White
      ant_dir = (ant_dir + 1) % 4
    else:
      ant_dir = (ant_dir - 1) % 4
    dx, dy = DIRS[ant_dir]
    ant_x, ant_y = ant_x + dx, ant_y + dy
  board.print_board()

# Tests
print_k_moves(10000)

# Time: 18 minutes

###
# Mistakes / Bugs / Misses
###
# Missed : on an else (65)
# Lines 64 and 66 had messed up %=   (ant_dir %= (ant_dir - 1) etc.)
# The grid turns out to be uninteresting with a checkered pattern to start,
#   so switched it to a purely white board
# It probably would have been better to have min/max x and y coords, instead
#   of just printing a square
