###
# Problem
###

# Design a caching mechanism for a "simple" search engine. You have 100 machines
# to process queries, which can call processSearch(query) to another cluster
# of machines. You can't guarantee the same machine will always respond to the
# same request. processSearch() is very expensive. Make sure you handle data
# changing (and so invalidating the cache)

###
# Work
###

# Questions:
# When it says "you cannot guarantee that the same machine will always respond
#   to the same request", do you mean our 100 machines, or the processSearch()
#   machines, or both?
# What is the distribution of queries? Are some queries far more popular than
#   others?
# What do the results from processSearch look like? Notably, how large are they?
# How often does the underlying data change? Or put another way, how fresh do
#   we need the results to be?

# Without knowing the answer to that question, one thing I'd like to do is
# shard the queries that are coming in so that the caches on each machine are
# more effective. However, it's not strictly necessary.

# Without an interviewer to ask, we'll make a few assumptions:
# -- Some queries (like "weather in san francisco") are more popular than
#    others. Additionally, we'll assume the queries have been canonicalized in
#    some way that's useful (for example, Google does personalization of
#    queries, so if I search for "weather", I get "Weather in <local city>",
#    but caching "weather" would not be useful for someone else. I assume there
#    is some layer that takes care of this for me before it gets to me.
# -- The results are a large serializable results object (like an HTML page,
#    an XML object, or a text file). Let's say they're 100k for now?
# -- We'll assume that we can invalidate results at a certain level of staleness
#    (that we'll make configurable) and not exactly when the data changes. It's
#    interesting to note that this staleness might actually be different based
#    on the query, but for now we'll assume it's constant.

# Unless we can shard based on the query, I don't think having 100 machines
# changes our caching strategy. Either we have a cache on each machine, or
# a larger cache on the machine that's sharding out queries to machines.

# The basic strategy I have in mind is an LRU cache. For efficiency, we have
# a queue with a parallel hashtable. The queue keeps track of which queries have
# been asked most recently, the head of the queue is the query that's closest
# to being evicted. The hashtable makes it easy to find a query in the queue
# in o(1), so if a query is asked for again, we move it to the tail of the
# queue.

# To handle data becoming stale, we keep a timestamp in either the queue or the
# hashtable. When we ask for a query, and we have a cached result, we check if
# the cached version is too old. If so, we evict it and call processSearch()
# again, otherwise we return the cached version.

# Time: 15 minutes

###
# Mistakes / Bugs / Misses
###
# Didn't discuss how many queries we're processing or caching. I assumed "large"
#   and hinted at it with size of the result object, but didn't discuss further.
# Didn't discuss the alternative where we actually want to invalidate when the
#   underlying data changes, not basing off freshness.

