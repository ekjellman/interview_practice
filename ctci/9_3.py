###
# Problem
###

# If you were designing a web crawler, how would you avoid getting into
# infinite loops?

###
# Work
###

# Use a hashtable. Ok, j/k

# Questions:
# What webpages do we consider equivalent? For example, we might consider
#   query parameters different pages or we might not. Or we might consider
#   the content of the page (i.e. if the content is equivalent, it's the same
#   page)
#   -- Also, if we're considering the full text, should it just be on pages
#      in the same domain?
#   -- Also, if we're considering the full text, we will probably want a way
#      to quickly check if the text could be equivalent, like a hash.
# How many pages are we crawling? Can we store all the URLs or relevant data
#   in memory, or do we need a database?
# Use cases for the web crawler, size of the webcrawler, etc
# Thinking about age / staleness of our crawling data as well.

# ---

# First, what does an infinite loop look like? What are we trying to guard
# against, and why is this a problem?
# I imagine we have a web crawler that is doing the following:
# -- Getting a page
# -- Storing it somewhere
# -- Scanning it for links
# -- Adding those links to a queue
# -- repeating with the next page in the queue

# So if page A has a link to page B, and B gets put in the queue, then later
# B has a link to page A, this forms an infinite loop. Pages can even have links
# to themselves.

# So we need some sort of storage of pages we've already crawled, so that we
# don't crawl it again until the next time we recrawl the data (or until the
# data is stale or what have you)

# A simple way of doing this would be to have a hashtable in memory of URLs
# that we've crawled. This only really works if we have a single crawler, and
# we're not crawling that many pages.

# Another way would be to check whatever database / data structure we're making
# of crawled pages. We could either check when we get the list of links from
# a page, when we're going to crawl the page (i.e. when we pop it from the
# queue) or both. We'd want to make sure then that this data structure can
# easily be queried this way.

# One problem might be that there can be URLs that look slightly different that
# actually point to the same page. I don't know of any way to deal with this
# in the general case, since servers can do whatever they want with the requests
# they're given. If we wanted to try to deal with this, we could assume that
# any web page that is equivalent is the same. We could hash the web page,
# and check if we have that hash in our data store before scraping it for links.
# Even this probably doesn't work, because pages that are basically the same
# might be different in very tiny ways (date/time stamps, or "served in 0.03s"
# kinds of messages). We could try to develop some other kind of fingerprint for
# the text, but that might be a very difficult problem.

# Time: 15 minutes (time limit for design problems)

###
# Mistakes / Bugs / Misses
###
# -- Didn't really consider deprioritizing crawling a child, just not crawling.
# -- Thought about but forgot to discuss bloom filters.
