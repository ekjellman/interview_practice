###
# Problem
###

# How would you load test a webpage without using any test tools?

###
# Work
###

# Questions:
# What do you mean by "without any test tools"? (Basically, what are you
#   actually trying to stop me from using?)
# What do you mean by load test? What are we trying to test specifically?
# How should we measure "success"? Are we looking for 10/25/50/90/99th %ile
#   times? 500 errors? Something else?

# Depending on the answer to that question, here are some ideas.
# -- Put together a list of pages that exist and don't exist on the domain, and
#    use curl/wget with xargs (which I think has a parallel argument) to get
#    those pages, with lower and higher degrees of parallelism.
# -- If you don't like curl, do the same thing with nc / sed / awk with a basic
#    GET request?
# -- If you don't like that, make a simple program in Python

# Depending on what we want to get out of the test, some of this might be more
# difficult. But it basically comes down to figuring out what we want out of the
# test, and building tools to test it (or using existing command line tools in
# "novel" ways

# Time:

###
# Mistakes / Bugs / Misses
###
# Didn't know for sure if xargs had a parallel argument. (it does)
# Didn't know for sure if it was wget (it was)
