###
# Problem
###

# You have a synchronized method A and a normal method B. If you have two
# threads in one instance of the problem, can they both execute A at the same
# time? Can they execute A and B at the same time?

###
# Work
###

# Assuming Java:
# 1) No they cannot. That's the point of synchronized.
# 2) Yes they can, unless the object is synchronized or something like that.

# Time: 1 minute

###
# Mistakes / Bugs / Misses
###
# The idea I was missing is that if you had two synchronized methods, two
# threads could not call different synchronized methods because synchronized
# essentially puts a lock on the object. (TODO make card)
