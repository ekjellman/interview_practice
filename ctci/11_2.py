###
# Problem
###

# An application crashes when it is run. Running it in the debugger, after ten
# times it never crashes in the same place. The application is single threaded
# and uses only the C standard library. What could be causing the crash?
# How would you test it?

###
# Work
###

# If it were not single-threaded, I would suspect threading issues.
# Does it crash on accessing the same data or same data structure? Perhaps
#   there was an allocation error, or there is memory corruption.
# Does it crash on accessing some external resource, like a peripheral,
#   hard drive, network, etc? Perhaps there is some sort of bug there.
# Has the application ever worked? If so, when did it stop working? Can we do
#   something like git bisect to find the checkin or range of checkins that
#   caused the problem?
# Is there a log? Does it have anything interesting?
# That's what's in my head without discussion with an interviewer.

# Time: 10 minutes

###
# Mistakes / Bugs / Misses
###
# While I thought about peripherals, I didn't think about it in terms of
#   "user input" or random numbers
# I also didn't think about memory allocation (or running out of memory),
#   although I feel this would have shown up in the crash
# I didn't discuss or consider isolating the application more (closing other
#   application, running it on a different machine, disabling parts of it)
# I didn't think about using static analysis tools

