###
# Problem
###

# How would you test a pen?

###
# Work
###

# Questions:
# What kind of pen?
# What are the use cases for this pen? (That might sound like a weird question,
# but what do we expect it to write successfully on? Should the ink or marker
# or whatever dry within a certain people of time? Should it be erasable?)
# What are the edge cases for the pen? (More below)

# First I would try to establish what kind of pen it is. For example:
# ball-point? Fountain? Quill? Multi-color? What does it write on? Paper?
# Fabric? Metal? etc.
# I would start with "Does it work under ordinary use". For example if it's a
# multicolor pen, do all of the colors work? When I say work, what materials
# should it write on, does it do that?

# Then I start thinking about non-working cases. What happens when it runs out
# of ink? What happens if we write on something we're not supposed to? What
# happens if the pen has pressure applied to it in various ways. Are these
# things what we expect to happen? Can we break it in a way we don't expect?
# If we snap the pen in half does it make a bunch of shards that are dangerous
# or hard to clean up? Can ink be refilled easily, if we want it to be?

# This is basically about making sure that the pen acts how we want in both
# positive and negative cases.

# Time: 8 minutes

###
# Mistakes / Bugs / Misses
###
# None
