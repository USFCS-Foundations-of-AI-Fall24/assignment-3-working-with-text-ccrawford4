## generate a simple dataset for clustering.
import random
import string

from model import get_random_words

def modify_words(words) :
    for word in words:
        rand = random.random()
        if rand <= 0.3:
            new_word = word + random.choice(string.punctuation)
            words.remove(word)
            words.append(new_word)
        if rand <= 0.2:
            new_word = word.capitalize()
            if word in words :
                words.remove(word)
            words.append(new_word)
        if rand >= 0.8 :
            new_word = random.choice(['a', 'an', 'the'])
            if word in words :
                words.remove(word)
            words.append(new_word)

def create_docs(npos, nneg, use_random=False) :
    pos_lexicon = ['cat', 'dog', 'fish', 'monkey', 'goat', 'hippo', 'orangutan', 'whale', 'lobster', 'horse']
    neg_lexicon = ['cat', 'fish', 'joke', 'map', 'right', 'fly', 'sled', 'tiger', 'hide', 'float']

    pos_docs = []
    neg_docs = []

    if use_random :
        pos_lexicon = get_random_words(npos)
        neg_lexicon = get_random_words(nneg)
        modify_words(pos_lexicon)
        modify_words(neg_lexicon)

    for i in range(npos) :
        d = [random.choice(pos_lexicon) for j in range(npos)]
        pos_docs.append(d)
    for j in range(nneg) :
        d = [random.choice(neg_lexicon) for j in range(nneg)]
        neg_docs.append(d)

    return (pos_docs, neg_docs)