###
# Problem
###

# Design Othello

###
# Work
###
# Questions:
# Use cases? One computer? Played across the internet? Two players, or vs.
# computer only? (Assume: one computer, one or two player)

# Player object
# -- name information
# -- possibly win/loss record, rating, etc
# -- possibly preferences (difficulty settings, etc)
# -- make_move(Game object), abstract

# AI object (extends Player)
# -- Difficulty, Play style, funny fake names, etc.
# -- implements AI in make_move()

# HumanPlayer object (extends player)
# -- make_move() through Display object, probably.

# Game object
# -- Calls on display to get two players of the correct type
# -- Holds board and pieces, implements game rules
# -- calls Player.make_move() to get moves from players
# -- Has legal_moves() method, used by AI and Display object.
#   -- Display object responsible for getting a legal move from the player,
#      although the Game object should also reject illegal moves and not make
#      them
# -- Has game_over() method
# -- Has score() method (and possibly winner() methods)

# Display object
# -- Shows the board to the end user, takes user input
# -- has panes for game preferences, setting up a game, possibly loading and
#    saving games in progress

# Time: 10 minutes

###
# Mistakes / Bugs / Misses
###
# Didn't go into detail about things like board implementation (In my mind I
# had a list of lists for the board, and ints for the pieces, for example. It
# would probably be useful to have a few more methods on the game object to make
# life easier for the AI / display

