###
# Problem
###

# Design Pastebin, where a user enters a piece of text and gets a randomly
# generated URL for public access

###
# Work
###

# Questions:
# How many users / documents a day do we expect?
# How "secure" do we want the docs to be? Notably, if people start trying
#   random URLs to find texts, how likely do we want them to be successful?
#   Also, do we want to try to detect people doing this?
# Do we want the text to be valid forever, or to go away after a period of time?
# Do we want to allow for assignable URLs?
# Do we want analytics? Should those analytics be at a different URL?

# Let's make some assumptions based on the questions above. Let's say we expect
# a million documents a day. We want the odds of hitting a document at random
# to be about one in a million. We do want to detect people scanning for docs.
# We want the docs to be available for a month. We don't want to allow picking
# URLs, and we can talk about analytics if there is time at the end.

# We could have some front end where people put in a piece of text, and it
# gets saved to a randomly assigned URL. On our backend, we'd have a database
# or cluster of databases (1 million docs a day is about 12 docs a second on
# average, although we wouldn't expect this to be uniform. This would be a
# simple app, so I imagine the load would not require more than one server).
# When a piece of text is submitted, our backend assigns a randomized URL and
# reports it to the frontend. It also stores the text in the database.

# For our URL, we can create a string of random letters and numbers. For example
# we could use A-Z a-z 0-9 for our character set, giving us 62 characters for
# each letter of the URL. For usability, let's get rid of some commonly
# confused letters (iIl oO0, a couple others?) and say we have 50.
# Since we expect a million documents a day, and we are storing documents for
# a month, and we want a one in a million chance of "hitting", we could use
# URLs that are nine or ten characters long. We can of course adjust this
# length as our constraints change in the future.

# We could also just store the text as flat files, and use the URL as a file
# name.

# We would want to consider having a limit on file size. If we're storing
# 30 million documents, and they're each 100kb in size, that would be 3 GB of
# text, which is completely managable. But it might be easy to try to DDoS us
# with large files.

# We also should consider how much network bandwidth we would need to serve the
# files, and guess how many times we think each file will be accessed. If we
# imagine, on average, each file is accessed 10 times per day that's 30GB of
# bandwidth a day. Access would likely not be that flat.

# There might also be legal considerations storing random text from random
# people, which we should look into.

# I'm out of time for looking at the rest of it.

# Time: 15 minutes (time limit for design problems)

###
# Mistakes / Bugs / Misses
###
# Didn't consider user accounts
# I talked about storing documents for a given period of time, but removing them
#   after not being accessed for a while is a better model
# I thought about but didn't talk about how to generate the URLs. My idea wass
#   generate a random URL of the given length, and regenerate on collision.
# Didn't think about how to shard this to multiple computers, although with
#   random URLs it's fairly straightforward.
# Didn't think about caching files.

# I think a lot of these issues would have come up if I had cranked up the
#   scope of the problem. 30 million documents is not that many. 30 billion
#   would certainly require multiple servers.
