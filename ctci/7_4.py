###
# Problem
###

# Design a parking lot using OOP

###
# Work
###
# Questions:
# Commercial or "personal use". i.e.: size of parking lot, what kinds of cars,
# are we charging fees / do we need to track entry and exit, do we have monthly
# users? Or is this four spots in the back of a small apartment?

# I'm going to move away from writing the Python classes

# Let's assume a commercial parking lot.

# First, we'll consider the Garage. We might have a fixed number of slots that
# we keep track of. If we fill up, we'll stop allowing entry. When a car enters,
# we'll give a ticket that notes the time of entry so that we can get payment
# later. We'll also need a separate method for monthly users (they won't get a
# ticket)

# Garage class:
#   -- Number of empty slots
#   -- List of outstanding tickets
#   -- List of monthly users / link to another system that handles users
#   -- enter_garage_ticketed()
#     Gives a ticket, reduces number of empty slots, stores ticket. Rejects if
#     full.
#   -- enter_garage_access_card()
#     Checks if card is valid, rejects if invalid, reduces empty slots if valid
#   -- leave_garage_ticketed()
#     Gets payment, increases number of empty slots, removes/logs ticket.
#     How to handle rejected payment / unable to pay / error cases?
#   -- leave_garage_access_card()
#     How to handle case where card becomes invalid during stay?
#   -- payment()
#     Handling various forms of payment, called by leave_garage_ticketed()?

# User class
#   -- Any history information we want (car coming/going, etc)
#   -- Dates of validity
#   -- Any user ID information we want (name / registered cars / etc)

# Display class
#   -- At most basic, is the garage full or not. Could show open slots, or
#      as noted below, more detailed information on floors / open areas / etc

# Advanced ideas:
#   -- Have a system that knows which spaces are taken, using weight sensors or
#      simple cameras. Use this to populate the display, or to get info about
#      where people tend to park / where individual users tend to park.
#   -- Could even assign cars to a space as they arrive, and light a path to
#      show users where to park

# Time: 15 minutes (time limit for OO problems)

###
# Mistakes / Bugs / Misses
###
# She talks more about types of vehicles and then vehicle objects. Also parking
# lot levels, for example. 
