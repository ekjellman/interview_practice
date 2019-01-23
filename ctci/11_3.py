###
# Problem
###

# A Piece class has a method can_move(x, y) which returns True if a piece can
# move to that position and False otherwise. How would you test this method?

###
# Work
###

# Questions:
# Are we testing the legality of the moves, or just whether the move is in
#   the correct range of the pieces?

# There are a few classes of tests I can think of.
# -- Standard tests. These are basically "is this move in the correct range
#    of motion for the piece". i.e. Rooks move left right up down, not
#    diagonally
# -- Off the board. We can't move to a position that isn't on the board
# -- Edge cases involving legality. For example: Is castling handled? How about
#    en passant? What about discovered check, or if the king is already in
#    check?
# -- Capture. Can a piece move to a square with another piece and capture it?
# -- Blocking. What if there's a piece in the way? Is this not applied to
#    knights?
# -- Colors. Do pieces of opposite colors behave the same? i.e. does flipping
#    the color of all the pieces change the result

# For all of these tests, we want cases where the test returns True or False.
# We also would like to organize these tests in a way that we can eliminate
# unnecessary code. For example, a lot of these tests might look very similar.
# Imagine a test for checking if a piece can move out of the way and leave a
# discovered check. You could make a test with a white king, a black piece
# attacking the king, and a white piece interposed which can't move out of the
# way. We don't want to have to write this test six times, but the frame of it
# would be the same each time.

# Time: 10 minutes

###
# Mistakes / Bugs / Misses
###
# Didn't think about full/empty boards

