###
# Problem
###

# Design a system that will be called by up to 1,000 client applications to get
# end-of-day stock price information (open, close, high, low). Assume you have
# the data, can store it any way you wish, and can distribute it however you
# want.

###
# Work
###

# Questions:
# What does "1,000 client applications" mean? That we're going to get 1,000
#   requests per day? That we have 1,000 users? (Regardless, that's not many)
# So speaking of which, how many requests per day might we receive? Is there
#   a particular distribution to when we receive requests?
# Who are these endusers? What are their usecases generally?
# What does a request look like? For example, will they ask for only one
#   specific stock? Or will it be a variety of stocks? What about historical
#   data? Will they ask for a date? If they only ask for the most recent day,
#   when does it change over, and should we signal that it does?
# How do we get the data ourselves? Do we get it at a predictable time?
#   What should we do if we don't get the data during a particular day?

# ---

# Ultimately, this is a fairly simple application, with not very much data.
# Any kind of solution we have could be fairly high throughput, even on a
# single machine.

# I feel uncomfortable designing a solution without knowing more about the
# users and how they might want to use the data. But from the problem
# description, it looks like we have a simple set of data, that doesn't change
# much or often.

# Internally, you could imagine storing the data as a hashtable from, say,
# (stock, date) -> (open, close, high, low)
# We could also use a database of some kind (does not need to be relational,
# a key/value store would work) for this, but the data is simple enough that
# this probably isn't necessary. However, it might be better in terms of having
# some off the shelf software that's already tested.
# We can probably store the whole thing in RAM. If you imagine 100 years of
# historical data on 5000 stocks, that 500,000 entries, and each one would be
# far less than 1kb, which would be 500MB, which is fine. If we expect many
# many calls per day, we could easily store the whole dataset on each computer
# we run this on, so we could split requests to multiple computers easily.

# In terms of input/output, an HTML request would be fine (we could return the
# data in XML). This could be overkill; if most of the users of this app are
# using older tech, or want something simple, a really simple telnet kind of
# interface would be fine, where they connect, send a request for a stock and
# date, and get an answer (think SMTP, but modified for this use case). There
# would be less overhead here as well.

# Any of these would be fairly simple to write and scale. It all depends on
# use cases and volume, which I'd have to ask the interviewer about.

# There is a lot more to talk about but I'm out of time.

# Time: 15 minutes (time limit for design questions)

###
# Mistakes / Bugs / Misses
###
# Didn't really think about having users download flat text files. It's possible
#   as a very simple answer.
# Thought about but didn't discuss security. Telnet, for example, would be
#   insecure, and it might be that the queries a person is making are sensitive.


