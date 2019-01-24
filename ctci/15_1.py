###
# Problem
###

# What is the difference between a thread and a process?

###
# Work
###

# A process can have multiple threads. A thread cannot have multiple processes.
# Threads are more lightweight.
# Processes are more heavyweight.
# Threads started by the same process can share memory
# Processes can only share memory through inter-process communication of some
#   kind (network, hard drive, etc)
# In Python, multiple threads cannot operate at the same time due to the GIL,
#   but multiple processes can.

# Time: 3 minutes

###
# Mistakes / Bugs / Misses
###

