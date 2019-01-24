###
# Problem
###

# Design a class which provides a lock only if there are no possible deadlocks

###
# Work
###

# Questions:
# It seems like we would need to know what locks each requester is going to
# need. How do we get that information? (Assume we design it ourselves)
# Use cases?
# What do we do if we can't provide the lock? (Assume return None. We could also
#   block)
# What are our goals for designing this class? Are we trying to improve
#   efficiency in some way?

# It seems like we can only do this if we somehow know which locks are going to
#   be requested by some thread. Or actually, is that true?
# We could have a class that holds all of the locks that we are handling for
#   our system. Then, when a thread requests a lock, we check to see if it holds
#   locks with a higher ID. If not, we reject the request. This would require
#   that locks be obtained in ascending order of ID if multiple locks are
#   required.
# Can this system still deadlock? I don't think so. To deadlock, two threads
#   need to be waiting on locks each other has. For example thread 1 has A
#   and wants B, thread 2 has B and wants A. We can think of this like a cycle
#   in a graph, but by enforcing this ascending numeric constraint, we ensure
#   that there are no cycles (since the locks have a strict ordering)

# Time: 11 minutes

###
# Mistakes / Bugs / Misses
###
# They did talk about a thread pre-registering what locks it will need
# They used a full graph approach. Probably this allows for more people to get
#   the locks they need faster, but my approach does work.
