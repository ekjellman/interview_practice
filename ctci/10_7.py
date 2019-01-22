###
# Problem
###

# Given an input file with four billion non-negative integers, what is an
# algorithm to find an integer not in the file? Assume you have 1 GB RAM

# Part 2: What if you have 10MB memory for a billion distinct non-negative
#         integers?

###
# Work
###

# Questions:
# (Python) Is there a range you want us to generate from within?
#          (Assume we want an integer less than 2**31)

# Part 1: Read the file in number by number and use a bitset. When we read a
#         number n, set the nth bit in the bitset to 1. At the end, scan the
#         bitset for a 0, and return that position as an integer not contained
#         in the file.

# Part 2: 10MB is not enough for the bitset. So instead, we'll do it in a couple
#         passes. In pass one, we'll make 2**31 / 1,000,000 buckets. Each bucket
#         will represent how many numbers we found in a certain range. For
#         example:
#         Bucket 0: Numbers from 0 - 999,999
#         Bucket 1: Numbers from 1,000,000 - 1,999,999
#         etc. There will be ~2 million of these buckets which should fit in
#         RAM. (At least in Java, which this book assumes. If there isn't
#         enough RAM we can do it in three passes instead)
#         We will take any bucket with less than a million numbers in it (and
#         there must be at least one) and make a bitset for those numbers, and
#         read the file in again, ignoring numbers not in the range of that
#         bucket. At the end, find a 0 in the bitset, and return the number
#         that bit represents.

# Time: 8 minutes
# No code, since it just asked for the algorithm.

###
# Mistakes / Bugs / Misses
###
# For some reason, I thought a million * a million = a billion, so I said there
# would be too many buckets.

