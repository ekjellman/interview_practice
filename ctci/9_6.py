###
# Problem
###

# Describe a system to list the best-selling products, overall and by category.
# For example, a product could be xth best-selling overall, or yth best selling
# under safety, or zth best selling under sports.

###
# Work
###

# Questions:
# number of items/products?
# number of categories?
# Are the categories hierarchical?
# How many categories can a product be in?
# How real-time do we want this? For example, we might be content with it
#   updating once an hour or once a day. Maybe it would be more realtime for
#   higher ranked items
# How accurate do we want it to be? For example, we might be content with a
#   precise ranking for the top n in a category, but beyond that we might be
#   ok with an estimate

# We can imagine a few overarching ideas on how to handle this. We can update
# a products ranking every time the items sells, but this is likely to generate
# too much work (especially on a large site, think Amazon)

# Probably better would be to have some background process updating the ranking
# occasionally, say once an hour or once a day.

# We almost certainly have sales in a database already. We would want to add
# a table where each item is linked to the category ids it's in. It would
# probably also be a good idea for each item to have a counter of how many
# sales there have been on that item.

# We might be able to estimate a item's position formulaicly. I don't know if
# sales in a category tends to follow a distribution or not. If so, we could,
# instead of getting a full sorting of each particular category (and overall
# ranking, ew) we could find the top 100 or 1000 or so, and go based on
# distribution after that. Depending on the number of sales after the top n,
# if we want an exact ranking we could do a bucket sort on sales instead of
# a full n log n sort (especially if there are more than, say, millions of
# items.

# We also should define what "best-selling" means. Is this over all time? In
# the past week? Etc? If so, instead of storing the numbers of sales an item has
# on it, we could, for example, store a rolling week by keeping 7 days worth of
# sales, and dropping the 7th day when we do daily ranking.

# Time: 15 minutes (time limit for design problems)

###
# Mistakes / Bugs / Misses
###
# Didn't really consider the frontend.
# Didn't think about having a sales rank data cache for the frontend to hit
# Thought about but did not write that this particular table could be kept in
#   memory. I did write to consider how many items there would be.
# Did not consider using a log file / mapreduce, which is actually really nice.

