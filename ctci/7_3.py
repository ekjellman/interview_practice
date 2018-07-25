###
# Problem
###

# Design a musical jukebox using OOP

###
# Work
###
# Questions:
# Commercial or personal? Affects whether we need to consider payment, and in a
# modern day possibly credits, user accounts, etc. (Assume personal)
# Real or virtual? (Assume virtual)
# Basically, are we trying to mirror an old-school Jukebox, or are we trying to
# make something that's more applicable / convenient for today.

# Primarily, we need two classes, one for songs, one for the Jukebox itself.
# Let's start with Song.

class Song(object):
  def __init__(self, ...):
    self.title = ...      # but see below
    self.artist = ...
    self.song_data = ...  # the MP3/AAC/whatever
                          # It might make more sense to get metadata from here,
                          # or make accessor functions, so we don't violate DRY
    self.play_count = 0   # And other bookkeeping methods we might want for
                          # this individual Jukebox. Song rating, for example

  def play_song(self): pass

# Then on to the Jukebox. We want to think about what functions it should have
# I can imagine a lot, here are a starting sample.

class Jukebox(object):
  def __init__(self, ...):
    self.songs = ...    # A data structure of available songs. A good question
                        # to ask here is how many songs a Jukebox will have,
                        # as this affects UI or possibly search. Hundreds is
                        # easy, but if it's millions we'll want to do some
                        # optimization to avoid O(n) searches
    self.song_queue = ...

  def search(self, ...): # Search for a song
  def add_song(self, song):  # Add a song to the queue
  def random_song(self): # Get a random song, possibly influenced by play counts
                         # or ratings
  def most_played(self): # Get information about most played songs / play counts
  def skip_song(self):   # Not in commercial settings

# Time: 13 minutes

###
# Mistakes / Bugs / Misses
###
# Could have asked "how many songs" at first.
# Did not think about CD-level organization or methods
# Did not discuss UI/display in depth
# Did not discuss Users (but noted that assumption)
# I should more about discussing already existing systems. During this problem,
#   I was thinking about apps like Winamp, iTunes, Spotify, etc, but did not
#   say so. I should note that during my design discussions.
