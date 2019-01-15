###
# Problem
###

# Detect duplicates in 10 billion URLs. "Duplicate" means the URLs are
# identical

###
# Work
###

# Questions:
# How big are the URLs, on average? Max? (Isn't it like 2kb max?)
# By "detect", what do you mean?
# -- For example, do you want to check a new url against the corpus?
# -- Or do you want to remove all duplicates?
# -- Or do you want to output all duplicates?
# Input/output?

# ----

# Depending on what we want to do, and how quickly we need to do it, there are
# a few different ideas that come to mind.

# First, let's assume the average URL is about 100 bytes, so we have 1 TB of
# text data.

# One way would be to take the URLs and do an external sort, then read through
# looking for duplicates. However, we don't need to perfectly sort them, so
# another similar idea is to shard the URLs using a hash function into smaller
# files that can read entirely into memory, and use a hashtable/set to find
# the duplicates in those shards. 1000 shards should be easily sufficient.

# Depending on how often we need to do this, we might even just do this in
# memory on one very beefy server. We could also consider compression of the
# URLs, since URLs should compress very easily.

# If we're ok with false positives we might consider using a bloom filter.

# I'm probably missing things, but I don't see much else to think about here.

# Time: 9 minutes

###
# Mistakes / Bugs / Misses
###
# The maximum URL length is theoretically unbounded. However, the RFCs recommend
# less than 8000 octets, and some modern browsers (say IE) won't handle more
# than about 2k. Also, search engines don't like more than 2k. Let's call it 2k.

# Didn't really think about multiple machines, or the speed of doing an
# external sort on one computer.
