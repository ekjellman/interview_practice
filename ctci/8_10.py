###
# Problem
###

# Implement a paint fill function. Given a screen (a 2d array of colors), a
# point, and a new color, fill the surrounding area until the color changes
# from the original color

###
# Work
###

# Questions:
# 4 way or 8 way? (assuming 8 way)
# How are colors represented? (For ease of coding, assuming they're integers)
# If the old color and the new color are the same, what to do? (I don't think
#   this is actually an edge case; there should be no change)
# Modify in place?

# I think she wants this implemented with recursion, but I'd probably just use
# my own stack or queue here. DFS or BFS doesn't really matter; in the worst
# case the queue will be O(size of painted area) either way.

def in_screen(screen, x, y):
  return (len(screen) > y and
          len(screen[y]) > x and
          0 <= y and
          0 <= x)

def flood_fill(screen, x, y, new_color):
  if not in_screen(screen, x, y): return   # Verify with interviewer. Error?
  old_color = screen[y][x]
  if old_color == new_color: return
  stack = [(x, y)]
  while stack:
    cx, cy = stack.pop()
    if in_screen(screen, cx, cy) and screen[cy][cx] == old_color:
      screen[cy][cx] = new_color
      for dy in (-1, 0, 1):
        for dx in (-1, 0, 1):
          stack.append((cx + dx, cy + dy))

test = [[0, 0, 1, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0],
        [0, 0, 1, 1, 1, 1, 1],
        [0, 0, 1, 0, 0, 1, 0],
        [0, 0, 1, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 1, 0],
        [0, 0, 1, 1, 1, 1, 0],
        [0, 0, 1, 0, 0, 0, 0]]

flood_fill(test, 3, 0, 2)
for line in test:
  print line

# Other tests, test not copied for space reasons.
# flood_fill(test, 0, 0, 2)
# flood_fill(test, 2, 0, 1)
# flood_fill(test, 2, 0, 2)
# flood_fill(test, 2, 0, 0)
# flood_fill(test, 3, 3, 2)

# Time: 19 minutes

###
# Mistakes / Bugs / Misses
###
# Didn't ask about modifying in place until started coding
# Didn't handle the case where old color == new color, added line 33
