import random

from Document import *

class Cluster :
    ## a cluster is a group of documents
    def __init__(self, centroid=None, members=None):
        if centroid :
            self.centroid = centroid
        else :
            self.centroid = Document(true_class='pos')
        if members :
            self.members = members
        else :
            self.members = []

    def __repr__(self):
        return f"{self.centroid} {len(self.members)}"

def calculate_centroid(d1, d2):
    centroid_tokens = defaultdict(lambda: 0)
    join = d1.tokens.keys() & d2.tokens.keys()
    for k in join :
        centroid_tokens[k] = (d1.tokens[k] + d2.tokens[k]) / 2
    centroid_doc = Document()
    centroid_doc.tokens = centroid_tokens
    return centroid_doc

# Call like so: k_means(2, ['pos','neg'], positive_docs + negative_docs)
def k_means(n_clusters, true_classes, data) :
    cluster_list = [Cluster(centroid=Document(true_class=item)) for item in true_classes]

    ## initially assign data randomly.

    ## compute initial cluster centroids

    # while not done and i < limit
    #   i++

    #   reassign each Document to the closest matching cluster using
    #   cosine similarity
    #   compute the centroids of each cluster
    return cluster_list