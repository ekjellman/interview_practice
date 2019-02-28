###
# Problem
###

# Write a function to determine if a 9x9 2d-list representing a partially
# completed sudoku is valid. Blanks are represented by 0

###
# Work
###
# Questions:
# Extensibility?
# Return type? (assume boolean)
# OO stuff

def check_sudoku(puzzle):
  # TODO: Error checking
  return check_rows(puzzle) and check_columns(puzzle) and check_cells(puzzle)

def check_rows(puzzle):
  for row in puzzle:
    if not check_numbers(row): return False
  return True

def check_columns(puzzle):
  for i in xrange(len(puzzle[0])):
    numbers = [row[i] for row in puzzle]
    if not check_numbers(numbers): return False
  return True

def check_cells(puzzle):
  for x in (0, 3, 6):
    for y in (0, 3, 6):
      numbers = [puzzle[x+dx][y+dy] for dx in xrange(3) for dy in xrange(3)]
      if not check_numbers(numbers): return False
  return True

def check_numbers(numbers):
  used = set()
  for number in numbers:
    if number == 0: continue
    if number in used: return False
    used.add(number)
  return True

# Tests:
puzzle = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
          [6, 0, 0, 1, 9, 5, 0, 0, 0],
          [0, 9, 8, 0, 0, 0, 0, 6, 0],
          [8, 0, 0, 0, 6, 0, 0, 0, 3],
          [4, 0, 0, 8, 0, 3, 0, 0, 1],
          [7, 0, 0, 0, 2, 0, 0, 0, 6],
          [0, 6, 0, 0, 0, 0, 2, 8, 0],
          [0, 0, 0, 4, 1, 9, 0, 0, 5],
          [0, 0, 0, 0, 8, 0, 0, 7, 9]]

print check_sudoku(puzzle), "True" 

puzzle = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
          [6, 0, 0, 1, 9, 5, 0, 0, 0],
          [0, 9, 8, 0, 0, 0, 0, 6, 0],
          [8, 0, 0, 0, 6, 0, 0, 0, 3],
          [4, 0, 0, 8, 0, 3, 0, 8, 1],
          [7, 0, 0, 0, 2, 0, 0, 0, 6],
          [0, 6, 0, 0, 0, 0, 2, 8, 0],
          [0, 0, 0, 4, 1, 9, 0, 0, 5],
          [0, 0, 0, 0, 8, 0, 0, 7, 9]]
print check_sudoku(puzzle), "False"

puzzle = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
          [6, 0, 0, 1, 9, 5, 0, 0, 0],
          [0, 9, 8, 0, 0, 0, 0, 6, 0],
          [8, 0, 0, 0, 6, 0, 0, 0, 3],
          [4, 0, 0, 8, 0, 3, 0, 0, 1],
          [7, 0, 0, 0, 2, 0, 0, 0, 6],
          [0, 6, 0, 0, 0, 0, 2, 8, 0],
          [0, 0, 0, 4, 1, 9, 0, 6, 5],
          [0, 0, 0, 0, 8, 0, 0, 7, 9]]
print check_sudoku(puzzle), "False"

puzzle = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
          [6, 0, 0, 1, 9, 5, 0, 0, 0],
          [0, 9, 8, 0, 0, 0, 0, 6, 0],
          [8, 0, 0, 0, 6, 0, 0, 0, 3],
          [4, 0, 0, 8, 0, 3, 0, 0, 1],
          [7, 0, 0, 0, 2, 0, 0, 0, 6],
          [0, 6, 0, 0, 0, 0, 2, 8, 0],
          [0, 0, 0, 4, 1, 9, 0, 0, 5],
          [0, 0, 0, 0, 8, 0, 5, 7, 9]]
print check_sudoku(puzzle), "False"

# Time: 12 minutes

###
# Mistakes / Bugs / Misses
###
# Line 26 had row instead of puzzle
# I still feel like I could do better on code duplication
# They use a list of booleans instead of a set. I feel like I should have
# offered the idea of using a bitvector (I thought about it but didn't type
# anything)
# There's also a little list copying that's unpleasant, but it's for cleaner
# code
