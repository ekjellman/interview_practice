###
# Problem
###

# Explain how you would sort a 20GB file with one string per line.

###
# Work
###

# Questions:
# How do we want it sorted? (Assume lexicographic order)
# How large are the lines? (Assume "normal" length... i.e. no 19GB lines,
#   probably most lines are 1kb or less)
# What kinds of strings? Unicode issues? (Assume don't worry about it)

# Well, if we have enough RAM, sort them in memory. Let's assume we don't.
# I can think of two main approaches:
# 1) Split the file into small enough chunks
#    that we can sort each chunk individually, then merge all the files together
#    using either a two-file-at-a-time merge sort approach, or with an approach
#    where we open all the files at once, read a line from each, and output
#    the lexicographically first line to the file, reading another line from
#    the file we just output the line from. Like an n-way merge sort. Since
#    most of the time is spent reading and writing, the n-way comparison will
#    probably not be a bottleneck (and this requires only writing the file
#    twice, once for the original split, and once for the merge, as opposed to
#    log(n) times).
# 2) Shard the file into smaller files based on prefixes of the lines, then
#    sort those smaller files. For a bad example, all the lines starting with
#    a go into one file, then b, then c, etc. The advantage is merging these
#    files should be easier, since we basically just have to cat them all
#    together. The disadvantage is if we don't know the distribution of the
#    prefixes, some shards could be much larger than others (for example, if
#    these are lines from books, maybe t or s are much larger than z). We would
#    either have to do a scan to figure out the distribution first, or we would
#    have to be ready to reshard larger files.

# Time: 9 minutes

###
# Mistakes / Bugs / Misses
###
# None
