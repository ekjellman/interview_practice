###
# Problem
###

# Given an image in an NxN matrix of 4 byte pixels, write a method to rotate
# the image 90 degrees. Do it in place.

###
# Work
###

# Questions:
# Does "4 byte pixel" mean integer? (assume yes)
# Clockwise? (Assume yes)
# Error check the size of the matrix? (Assume no)

# 1 2 3 4   D 9 5 1
# 5 6 7 8   E A 6 2
# 9 A B C   F B 7 3
# D E F G   G C 8 4

# (x, y) -> (y, len(x) - x - 1)


# Optimizations:
# There must be a numpy.rotate or something, but I don't know it.
# XOR tricks to avoid storage / "simplify" code

def rotate_matrix(matrix):
  for x in xrange((len(matrix) + 1) / 2):
    for y in xrange(len(matrix) / 2):
      cx, cy = x, y
      temp = matrix[cx][cy]
      for _ in range(4):
        nx, ny = cy, len(matrix) - cx - 1
        temp, matrix[nx][ny] = matrix[nx][ny], temp
        cx, cy = nx, ny

test = [[10, 11, 12, 13],
        [14, 15, 16, 17],
        [18, 19, 20, 21],
        [22, 23, 24, 25]]

rotate_matrix(test)
for row in test:
  print row

print
print "22 18 14 10"
print "23 19 15 11"
print "24 20 16 12"
print "25 21 17 13"


test = [[10, 11, 12, 13, 14],
        [15, 16, 17, 18, 19],
        [20, 21, 22, 23, 24],
        [25, 26, 27, 28, 29],
        [30, 31, 32, 33, 34]]

rotate_matrix(test)
for row in test:
  print row

print
print "30 25 20 15 20"
print "31 26 21 16 11"
print "32 27 22 17 12"
print "33 28 23 18 13"
print "34 29 24 19 14"


# Time: 24 minutes

###
# Mistakes / Bugs / Misses
###

# Line 31: Had len(y) instead of len(matrix)
# Line 30-31: Bounds of x, y were wrong for odd N case
#             (Had (len(matrix) - 1) / 2 for y instead of making x bigger
#             Either can work but I did the rounding wrong
