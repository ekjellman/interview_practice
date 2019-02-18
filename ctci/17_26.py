###
# Problem
###

# The similarity of two documents (each with distinct words) is the size of the
# intersection divided by the size of the union. For example, if the documents
# consist of integers, the similarity of {1, 5, 3} and {1, 7, 2, 3} is 0.4,
# because the intersection is 2 (1, 3) and the union is 5 (1, 2, 3, 5, 7)

# We have a long list of documents where the similarity is believed to be
# sparse. Meaning, any two arbitrarily selected documents are likely to have
# similarity 0. Design an algorithm that returns a list of pairs of IDs and
# similarity.

# Print only the pairs with similarity greater than 0. Empty documents should
# not be printed. For simplicity, assume each document is an array of
# distinct integers

###
# Work
###
# Number of documents?
# Number of "words"?
# Number of document pairs we expect to be non-sparse?
# Print each pair once?
# Input? Can we assume a set of words instead? (sure)
# Output? (just the printing)

# Approaches:
# Brute force: compare each pair of documents
# -- Instead, make a dictionary from word to documents that have that word.
#    Then, for each document, we can find all the documents that have any
#    similarity by unioning the document lists for each word in the document.
import collections

def print_similarities(documents):
  word_index = collections.defaultdict(set)
  for document in documents:
    for word in documents[document]:
      word_index[word].add(document)
  for document in documents:
    similar_docs = set()
    for word in documents[document]:
      similar_docs |= word_index[word]
    for similar_doc in similar_docs:
      if document < similar_doc:
        s = similarity(documents[document], documents[similar_doc])
        print "%d, %d\t: %f" % (document, similar_doc, s)

def similarity(a, b):
  # Div 0 seems possible, but we can't call this unless a or b has a common word
  return float(len(a & b)) / len(a | b)

documents = {13: set((14, 15, 100, 9, 3)),
             16: set((32, 1, 9, 3, 5)),
             19: set((15, 29, 2, 6, 8, 7)),
             24: set((7, 10))}
print_similarities(documents)

# Time: 21 minutes

###
# Mistakes / Bugs / Misses
###
# Wasn't sure about set.extend(). TODO: Make card
# Line 40 was for word in document:
# Line 40 had append not add
# Line 44 had extend instead of &=
# Line 44 had &= instead of |=  TODO: Make card
# Line 52 had print instead of return
# Line 52 had no float. TODO: make card
# Did not think of approach of making an intersection count for (doca, docb) by
#   iterating through pairs of words in the word_index

