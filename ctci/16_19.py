###
# Problem
###

# Given an integer matrix representing a plot of land, where the value in
# the matrix represents height above sea level, and 0 represents water, find
# the sizes of all the ponds. (Ponds are connected horizontally, vertically, or
# diagonally)

###
# Work
###
# Questions:
# Size / representation of the matrix (memory not an issue, list of lists)
# Input? (List of lists)
# Output? (List of pond sizes)
# What if no ponds? (Empty list)
# What if ragged matrix? (Assume valid input)

def find_ponds(matrix):
  # TODO: Error checking
  visited = set()
  pond_sizes = []
  for y in xrange(len(matrix)):
    for x in xrange(len(matrix[y])):
      if matrix[y][x] == 0 and (y, x) not in visited:
        pond_sizes.append(handle_pond(matrix, y, x, visited))
  return pond_sizes

def handle_pond(matrix, y, x, visited):
  current_pond = set()
  current_pond.add((y, x))
  visited.add((y, x))
  stack = [(y, x)]
  while stack:
    cy, cx = stack.pop()
    for dy in (-1, 0, 1):
      for dx in (-1, 0, 1):
        ny = cy + dy
        nx = cx + dx
        if (ny, nx) not in visited and in_matrix(matrix, ny, nx) and matrix[ny][nx] == 0:
          current_pond.add((ny, nx))
          stack.append((ny, nx))
          visited.add((ny, nx))
  return len(current_pond)

def in_matrix(matrix, y, x):
  return y >= 0 and y < len(matrix) and x >= 0 and x < len(matrix[y])

# Test:
matrix = [[0, 2, 1, 0],
          [0, 1, 0, 1],
          [1, 1, 0, 1],
          [0, 1, 0, 1]]

print find_ponds(matrix)

# Time: 17 minutes

###
# Mistakes / Bugs / Misses
###
# Forgot to check if the square we're checking is a pond or in the matrix at 40
# At line 31, had current_pond = set((y, x))
# I still don't understand why this doesn't work. TODO: Card
