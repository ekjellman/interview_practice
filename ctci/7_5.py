###
# Problem
###

# Design the data structures for an online book reader system

###
# Work
###
# Questions:
# Are we talking about an reader for an individual book (like say a PDF), or are
# we talking about a larger infrastructure (like say Amazon Kindle, etc)
# Use cases we care about?
# Integration with other systems? (Like payment, etc)
# Assuming we're making a Kindle clone

# Assuming we're talking about a larger system, we need a bunch of structures

# User object
#   -- Ways to buy / gain access to books
#   -- Information about the user's interactions with a book (bookmarks, notes,
#      highlights, etc). These may or may not be stored on the server as well
#      If so, send these to the Library/Server when made
#   -- open_book(book)
#      When a book is opened, check for a last read marker and open there
#   -- make_note(location object)
#   -- make_highlight(location object)
#   -- set_bookmark(location object)
#   -- set_last_read(location object)
#      Set this when a reader flips a page, etc

# Location object
#   -- book
#   -- start
#   -- optional end

# Library / Server object:
#   -- Data about what books the user has access to
#   -- data structure containing all books
#   -- can_access(book, user)
#   -- search(criteria, optional user): Look for books with criteria
#                                       Optionally only within user's books
#   -- functions to accept highlights/bookmarks/etc from users.

# Book object
#   -- Stores book data (book text, title, author, ISBN, Dewey, reviews,
#      other catalog information)
#   -- Stores (anonymized?) aggregate data about reads, purchases, highlights,
#      bookmarks, etc
#   -- Returns data about book (i.e. text / graphics / etc) between 
#      locations (for aid in display)

# Display object
#   -- Shows book data (text / graphics / etc) given a location object,
#      dependent on the device. (Different implementations for different
#      devices, etc)

# Time: 15 minutes (limit for OOP problems)

###
# Mistakes / Bugs / Misses
###
# I am probably being a bit too hand-wavy on these problems now, not specifying
# details of the system. It's hard to keep the balance on that right without an
# interviewer.
