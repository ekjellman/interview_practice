###
# Problem
###

# Design a chat server. In particular, talk about the backend components,
# classes, and methods. What are the hardest problems to solve?

###
# Work
###
# Questions:
# Use cases?
# How many users are we expecting simultaneously?
# Do we have any particular kind of chat server in mind? For example, we might
# think about IRC, or AIM, or Discord, or Slack. These all handle things
# differently. Do we need to think about chat rooms? images? Or just one-on-one
# conversations?
# Do we need to provide history or logging?
# Do we need to provide authentication, or will people be psuedo-anonymous?

# Let's talk about something like IRC with authentication, to start with.

# We'll have a single chat server that we'll connect with (as opposed to a
# farm of servers that have to communicate with each other)

# The server will be responsible for receiving incoming messages and sending
# received messages to clients, in a kind of pubsub sort of way. We can have
# rooms that we will join.

# A little more concretely:

# The server object stores:
# -- A set of chat rooms (identified by a string)
#   -- We should think about whether rooms can be private / require auth
# -- A set of users
# -- A set of logged in users
# -- A set of connections we listen to for incoming messages, and send outgoing
#    messages to
# -- connection and disconnection methods

# A user object has:
# -- A string identifier (unique?)
# -- A numeric ID (unique.)
# -- Authentication information (hashed/salted password, for example)
# -- Other information we care about (account details like account creation time
#    or credit/karma information, etc)
# -- login methods?
# -- message sending methods

# A room object has:
# -- A string identifier (unique)
# -- Possibly a log of messages for that room
# -- Room-specific auth information
# -- Joining and parting methods
# -- utility methods
# -- Think about room bots

# Sending a message would involve sending a request from the client to the
# server indicating the user, any auth information we need to send / session
# cookie, the message, and the room or user we want to send it to.

# The hardest problems to solve, for me, would be handling incoming connections
# and all the edge cases that can happen there. What if a user disconnects
# without notification? What if they try to reconnect and we think they're
# logged on? What if they connect from two places at once? What if they're
# connected, and then they connect their VPN and now they have a different IP
# address? Do we make them reconnect or handle it seamlessly? 

# Time: 15 minutes (time limit for OOP questions)

###
# Mistakes / Bugs / Misses
###
# Did not drill down into any specific area, tried to stay at the top level.
# I should have recognized the problem was too large.
# It's difficult to compare because we both focused on different areas, with
# different requirements. She went in for a multi-server chat server system,
# and went to talk about user management and conversation stuff, where I was
# thinking more about server connection issues.
# She talked more about specific technologies than I did (XML, SQL, etc)
# The ideas about scalability and handling DDoS attacks being difficult are
# interesting
