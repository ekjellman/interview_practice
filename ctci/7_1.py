###
# Problem
###

# Design the data structures for a generic deck of cards. Explain how you would
# subclass the data structures to implement blackjack

###
# Work
###

# Questions:
# When you say "generic deck of cards", do you mean trump cards? There are a
# variety of types of cards for various games. Tarot cards, Magic the Gathering,
# Ticket to Ride card, etc etc. (Assume yes)
# What are the use cases for the generic deck? Are we trying to make a deck
# class that can be subclassed for many games, or for a particular class of
# games? This determines where I might put some functionality (for example
# shuffle(), draw(), etc)
# Where are we going to be using this? A PC game? An online casino? We might
# have different bounds for speed, code complexity, etc.

# You could imagine a generic class that looks something like this.

class Card(object):
  def __init__(self, value, suit):
    self.value = value
    self.suit = suit

class Deck(object):
  def __init__(self):
    self.cards = []
    # create cards, add them to the deck

  def shuffle(self):
    pass  # TODO

  def draw_card(self):
    pass  # TODO

# Then, for Blackjack, we would want some game-specific knowledge. We could
# either put that in a Blackjack game class, or put it in the deck itself.
# Here we're talking about things like hand values, whether one hand beats
# another hand (particularly if a hand has an ace, say A5, we'd need logic to
# say "this can be valued 6 or 16, which of these are valid, and which should
# we use". It gets trickier when there are multiple aces.

# In a casino, you might also have logic for which cards are face up or
# face down, for example.

# You could imagine having a hand object like this:

class BlackjackHand(object):
  def __init__(self, deck):
    # We'd have to be careful here about security considerations in a casino
    # scenario. We don't want the player to know what cards are next, for
    # example. Python is not super well suited to this, but we would almost
    # certainly have deck access methods access something on a server, not
    # something that's stored remotely.
    self.deck = deck
    self.hand = []  # We would not draw right away.
    self.complete = False  # Whether there are more actions for this hand

  def deal_card(self):  # Have a card dealt to this hand
    pass  # TODO

  def hand_value(self):
    pass  # TODO

  def busted(self):  # Is this hand's value over 21, and so invalid?
    pass  # TODO

  def hit(self):
    pass  # TODO

  def stand(self):
    pass  # TODO

  # You could imagine having "double" here, but that is probably better handled
  # by the Blackjack game class, giving a player multiple hands. You could have
  # the function here anyway, if we think of these as player actions, but I
  # think that goes better in a game class or in a player class

# Time: 15 minutes (time limit for these problems)

###
# Mistakes / Bugs / Misses
###
# Study enumeration in Python.
# Did not have getters and setters, that's an interesting conversation to have.
# Interesting methods from book for Deck: remaining_cards(), deal_hand()
# Interesting idea for card: Mark as "available" or not. I would have delegated
# this to the Deck.
# She puts score() in the generic deck, which is interesting.
# BlackjackHand methods: is21, isBlackJack (I don't know about is21)

