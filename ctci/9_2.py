###
# Problem
###

# Design the data structures for a large social network like Facebook or
# LinkedIn. Describe the algorithm to show the shortest path between two
# people.

###
# Work
###

# Questions:
# What are our use cases for the users or the data? What kind of information
#   should we store? (I know I'd be expected to think about some of that)
# How many users do we expect to have?
# How many requests a day do we expect to have? (for the shortest path thing)
# Do we care about exact answers for shortest path, or are estimates acceptable
# in worst case scenarios? Particularly, if the path is longer than n nodes,
# can we abort?

# ---

# Assumedly, we expect to have a very large number of users and requests.
# I think Facebook has something like a billion users, and LinkedIn is certainly
# 8 (if not 9) digits. So we're going to have to consider scalability,
# and especially storing data on multiple machines.

# First, let's think about a user object. The data we'd store would be different
# for these different websites, so I will focus on Facebook. We might have
# things like:
# - User ID (int)
# - Display Name (string)
# - Email Address (string)
# - Friends (list of User)
# - other data for other parts of the site. For example, if we're talking about
#   news feed we might store data about known preferences so we can curate a
#   feed for them more easily, and so forth. I'd imagine this object would get
#   quite large, so parts of it might get put in other objects that can be
#   easily referenced by user id instead.

# Even this small amount of data might make the average user object a few kb in
# size, so if we have a billion users, we're talking a few terabytes of user
# objects, so we'd need to shard users onto multiple computers. This makes our
# shortest path problem more challenging, since we'll have to handle querying
# multiple computers.

# We'd like to make it more likely that we don't have to leave a computer to
# get the best answer, so I would shard users in a way that keeps cliques of
# users on the same computer. Without knowing about the data, geographical
# sharding seems likely (since most people's friends will live close to them?)
# I imagine that finding more efficient sharding methods could be the subject
# of a lot of research.
# I'm running short on time, but a few things in mind for the search:
# -- Do bidirectional search to try to minimize the exponential problems in
#    the worst cases
# -- Have a maximum search depth (say 6 links at most?)
# -- Group up requests (i.e. when you search at a given depth, and have to ask
#    neighboring shards for friend information, ask for all the friends on that
#    shard at once to minimize network overhead and such)

# Time: 15 minutes (time limit for design problems)

###
# Mistakes / Bugs / Misses
###
# Did not think about caching
# -- Also, did not think about having/storing a smaller version of the User
#    object just for this problem, which may or may not be worth it.
# Did not think about server failure
# Thought about but did not discuss Users with more friends. It makes sense
#   to try to look at users with more friends first, since it's more likely
#   to find a path through that friend. Additionally, if we were ok with
#   estimations in some cases, we could maintain a structure or cache of paths
#   between certain users with high numbers of friends that are well distributed
#   as a possible shortcut?
