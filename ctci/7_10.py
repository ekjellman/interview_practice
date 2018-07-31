###
# Problem
###

# Implement minesweeper

###
# Work
###
# Questions:
# NxN? not NxM?
# Text-based meaning playable on the command-line? (assume yes)

# We need a Game class to start.

# Game object:
# -- Holds board information
#   -- Size
#   -- What is in cells (bomb, number, or blank)
#     -- Can precompute these when the board is created
#   -- What cells are displayed to the user (?, number, or * for game over)
# -- make_move(self, x, y)
#   -- returns whether a bomb is hit, and updates what cells are displayed
#   -- If it's a bomb or a number, this is easy, just update the one cell
#   -- If it's a blank, do a flood-fill algorithm with BFS to find surrounding
#      blank cells
# -- game_over()
#   Return True if a bomb was hit, or all non-bomb cells are exposed.
#   O(n**2) regardless.

# Display object:
# -- Might not be worth it for a text-based version, since we could just
#    implement __str__() to display the board
# -- If we do, also get moves from user
# -- Tricky problem: Making this useable in a text version with larger boards.

# Time: 10 minutes

###
# Mistakes / Bugs / Misses
###
# not doing the implementation because OOP problem. TODO as a project?
# Keeping track of unexposed cell count in the Game object is better than
# scanning each time.
# Did not note the game initialization method, although I did think about it.
# Placing the bombs through shuffling is interesting. I would not do this
# probably, although this also brings up configuration of the board, which I
# did not talk about. The user will probably want a way of selecting board size
# and number of bombs. To make the not-shuffling better, it woudl be good to
# put a limit on number of bombs compared to board size.

