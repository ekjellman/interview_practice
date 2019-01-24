###
# Problem
###

# How would you measure the time spent in a context switch?

###
# Work
###

# "I don't know"
# I remember that context switches have something to do with the operating
#   system, and maybe it's the time spent switching between processes?
# My vague answer is that I'd like to figure out a way to trigger a context
#   switch, and measure that. It seems like there might be some non-determinism
#   there, so we might need to do it many times and look for a common minimum
#   time (in case some other thing happened in our timer start/end)

# Time: 3 minutes (FAILED)

###
# Mistakes / Bugs / Misses
###
# TODO: Make a card on context switches
# http://www.linfo.org/context_switch.html
# Her solution (TODO study further) is basically to have two processes and
# send a token back and forth between them measuring the time.
