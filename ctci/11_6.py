###
# Problem
###

# How would you test an ATM in a distributed banking system?

###
# Work
###

# Questions:
# What are the use cases? What functions does the ATM have?
# What kind of ATM?
# Where will this ATM be located?
# Who owns the ATM? i.e. is it at a bank, or in a store, or what?

# First and most basically, we'd want to make tests for each of the individual
# functions of the ATM. These would be similar to normal unit tests. Can we
# withdraw money? Is there a maximum amount? What if we try to withdraw more
# than that? What if we try to withdraw more than we have in our account?
# All the kinds of standard cases and edge cases for each function.

# Then I would want to start thinkinga about the things that are more unique to
# ATMs. When I think about ATMs one of the first things that comes to mind is
# security. So we could talk about testing the physical ATM. How susceptible is
# it to theft? To losing money due to damage? Is it easy to break into the
# machine to get money? Do we have a camera in the machine? How easy is it to
# disable? Are there alarms? Do they work? What if the machine is unplugged or
# there is power failure? Is it easy or difficult to install a skimmer?

# We might also think about how network failure affects the device. Does it
# stop dispensing money, or give a normal sort of error message? Maybe it
# fails to authenticate users and eats their cards, which would be a problem.
# What happens if we lose network at critical parts of the transaction?
# After authentication, but before dispensing money? (Maybe it checks balance
# and dispenses money, but then can't update the balance and we lose money).
# etc. etc.

# Similarly with threading issues. We don't want two people to access the same
# account at the same time and both get money when they couldn't due to a race
# condition.

# This question basically comes down to nailing down the use cases, and what
# kinds of decisions and tradeoffs we want to make for security vs ease of use
# and testing whether the machine's implementation matches that design.

# Time: 13 minutes

###
# Mistakes / Bugs / Misses
###
# I did not think about what tools we have to test. I did not think about white
# vs black box testing.
# 
