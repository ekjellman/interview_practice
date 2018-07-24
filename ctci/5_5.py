###
# Problem
###

# Explain what this code does:
# ((n & (n-1)) == 0)

###
# Work
###
# Questions:
# In a normal language, or in Python? ^_^

"""
The idea is that this checks if a number is a power of two. Say we have a
power of two like this:

100000 (32)

This minus one is 31
011111

Effectively, it takes the least significant 1, replaces it with a 0, and changes
all the lesser 0s to 1s, just like subtracting 1 from 10000 in base 10 is 9999.

Then, when we and them together, the least significant one and all the zeros
before it become zero.

100000
011111
------ &
000000

If there were more than one 1, it would look like this:

100100 n
100011 n-1
------ &
100000
   ^^^

In this case, since there's more than one one in the original number, the result
is not zero.

Any number where there is exactly one 1 is a power of two. Except.

In a two's complement system, if the number is the most negative integer (say
-2**31) this will also work, as it converts the sign bit to 0, leaving all the
other zeros.

This doesn't happen in Python with negative numbers, because the overflow that
happens with the n-1 of the most negative number just causes Python to extend
the original number.
"""

# Time: 6 minutes, mostly typing the explanation

###
# Mistakes / Bugs / Misses
###

