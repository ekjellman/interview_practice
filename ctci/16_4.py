###
# Problem
###

# Design an algorithm to figure out if someone has won a game of tictactoe

###
# Work
###

# Questions:
# Format of the board? (Assume whatever you want)
# Do we want this to be extensible? (Assume no is fine)
# What do we mean by "won"? (Assume the current position is terminal, not
# that someone could win with best play or anything like that)
# Otherwise test for board validity? (For example, both X and O winning,
# or other invalid game states? Assume no.)

def game_won(board):
  # Board is a 9 char string with X, O, or .
  assert len(board) == 9
  for win in ((0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
              (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
              (0, 4, 8), (2, 4, 6)):            # Diagonals
    a, b, c = win
    if (board[a] == board[b] and board[a] == board[c] and
        (board[a] == "X" or board[a] == "O")):
      return True
  return False

print "True", game_won("XXX......")
print "True", game_won("...OOO...")
print "True", game_won("......XXX")
print "True", game_won("X..X..X..")
print "True", game_won(".X..X..X.")
print "True", game_won("..X..X..X")
print "True", game_won("O...O...O")
print "True", game_won("..O.O.O..")
print "False", game_won(".........")
print "False", game_won("OXOOXOXOX")

# Time: 9 minutes

###
# Mistakes / Bugs / Misses
###
# Got my full board test wrong
# Didn't think about caching solution
# Didn't ask what to return, just returned True or False instead of winner,
#   which is probably more useful
