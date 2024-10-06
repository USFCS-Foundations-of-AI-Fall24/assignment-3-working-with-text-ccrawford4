## A representation of a document as a set of tokens.

from collections import defaultdict
from math import sqrt
import numpy as np
from numpy.linalg import norm

class Document :
    def __init__(self, true_class=None):
        self.true_class = true_class
        self.tokens = defaultdict(lambda:0)

    def add_tokens(self, token_list) :
        for item in token_list :
            self.tokens[item] = self.tokens[item] + 1

    def __repr__(self):
        return f"{self.true_class} {self.tokens}"

# return the distance between two documents
def euclidean_distance(d1, d2) :
    # take the union of the tokens in each document
    union = d1.tokens.keys() | d2.tokens.keys()
    dist = sum([(d1.tokens[item] - d2.tokens[item])**2 for item in union])
    return dist

def cosine_similarity(d1,d2) :
    numerator = sum(value * d2.tokens[key] for key, value in d1.tokens.items() if key in d2.tokens)
    sqrt1 = sqrt(sum(value**2 for value in d1.tokens.values()))
    sqrt2 = sqrt(sum(value**2 for value in d2.tokens.values()))
    denominator = sqrt1 * sqrt2
    return numerator / max(denominator, 0.0000000000001)
