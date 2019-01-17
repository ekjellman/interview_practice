###
# Problem
###

# Design a personal financial manager like mint. This system would connect to
# your bank accounts, analyze spending habits, and make recommendations.

###
# Work
###

# Questions:
# Who are we aiming this software at? The kinds of recommendations we would
#   make for different kinds of people at different places in live should
#   probably be different
# 

# The first thing that comes to mind with this kind of system is security. We
# are going to have a lot of people's personal financial data in our systems,
# and we need to protect it. So we need to think about user authentication,
# probably offer two-factor auth (maybe with Google Authenticator or something
# similar), and have internal controls on access to the data so even employees
# don't have full access to the data.

# Next I think about how we connect to bank accounts and other online financial
# institutions like Fidelty/Vanguard/etc.. I am pretty sure there is not an
# open standard for these kinds of systems, so we're going to have to make a
# bunch of one-off solutions. We'll probably also want to have a legal team look
# at our liability in terms of accessing and storing this data.

# Since these systems are all likely to be different, we're going to need to
# build a normalization layer that will take data in whatever format the banks
# give us, and convert it to our own internal format.

# In terms of what that internal format is, at a first pass we'll want to have
# a database of transactions, including what a transaction is from, the category
# of it (rent / groceries / entertainment / etc), the amount, date and time,
# and whatever other info we think is necessary about a transaction. From a UI
# standpoint, we'll want to make sure people can edit these, particularly the
# category of a transaction, which we'll probably have to make a guess for
# (which might be wrong). We'll need to come up with a system for that guess,
# too.

# The recommendations part is difficult as well. Each person is likely to have
# a relatively small number of transactions that we would be considering, so
# processing isn't too bad, but what the recommendations are is difficult. To
# start with, I'd want to work with some financial experts on some example data,
# to get an idea what they look at. Based on that work, we could start building
# a set of recommendations and a set of rules to trigger them. This seems like
# it could be somewhat fragile though.

# Another possibility as we get more data would be to try to apply machine
# learning. If we can see which people are doing "better" somehow, we could
# apply clustering to people with similar incomes and situations (projected
# number of kids, geographic area, whatever is relevant) and show suggestions
# based on a comparison between users. This could be really touchy from a
# security standpoint, and it might not have good optics, either. It's an idea
# we could iterate on.

# Time: 15 minutes (time limit for design problems) (FAILED)

###
# Mistakes / Bugs / Misses
###
# I did a really bad job of scoping the problem and asking questions
# There's a lot of ground I didn't cover
# TODO: Study this answer more.
