###
# Problem
###

# Implement an NxN jigsaw puzzle. Design the data structures and explain an
# algorithm to solve the puzzle. Assume you have a fits_with() method that takes
# two puzzle edges and returns True if the edges belong together.

###
# Work
###
# Questions:
# Do we know anything else about the pieces? For example, do we know if pieces
# are corner or edge pieces? Or anything like color content (Assume no, I guess)
# Are the pieces square and all the same size? (Assume yes)

# If the pieces are square, it seems like you'd have a puzzle pieces with four
# edges, something like:

class PuzzlePiece(object):
  def __init__(self, ...):
    self.edges = [...]

class Edge(object):
  def __init__(self, ...):
    # Whatever info we need to implement fitsWith

  @staticmethod
  def fitsWith(edge_a, edge_b):
    # TODO

# With no information about whether pieces are edge or center pieces, I'd
# implement the algorithm in two steps:

# First, determine the dimensions of the puzzle (if we're not given them) and
# get a "framework" for where the pieces go. So for example, start with a piece
# at random. We don't know where this is in the puzzle, so we start by building
# in one direction by trying every edge of every piece against the side that
# would grow it in that direction.

#     x------>

# We do this until we get no more matches. Then we do it in the other direction
#  <--xxxxxxxx

# We do the same with north and south. Now we have a cross (or possibly T or L)
# shape, and we know where pieces can be in the puzzle. We can now start
# building in any direction from this cross until we have the whole puzzle
# built. The runtime complexity is O(n**4): we have O(n**2) pieces to place, and
# for each spot in the puzzle, we have to try O(n**2) * 4 edges.

# We can cut this down some if we know, for example, the orientation of the
# pieces, or whether pieces are edges or corner, for example, but we're still
# O(n**4), albeit with a smaller constant factor.

# Time: 13 minutes

###
# Mistakes / Bugs / Misses
###
# Did not ask about whether we get n. Would put that in a puzzle object?
# Book solution assumes we know that edges are inner, outer, or flat, which
# lets us figure out edge or corner, and eliminate some pieces from
# consideration

