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

    def calculate_centroid(self):
        centroid_tokens = defaultdict(lambda : 0.0)
        for member in self.members :
            for key in member.tokens.keys() :
                if key not in centroid_tokens :
                    centroid_tokens[key] = member.tokens[key]
                else :
                    centroid_tokens[key] = (centroid_tokens[key] + member.tokens[key]) / 2
        centroid_doc = Document()
        centroid_doc.tokens = centroid_tokens
        self.centroid = centroid_doc

# Call like so: k_means(2, ['pos','neg'], positive_docs + negative_docs)
def k_means(n_clusters, true_classes, data) :
    cluster_list = [Cluster(centroid=Document(true_class=item)) for item in true_classes]

    ## initially assign data randomly.
    for doc in data :
        rand_idx = random.randint(0, len(cluster_list) - 1)
        cluster_list[rand_idx].members.append(doc)

    for cluster in cluster_list:
        cluster.calculate_centroid()

    # while not done and i < limit
    #   i++

    #   reassign each Document to the closest matching cluster using
    #   cosine similarity
    #   compute the centroids of each cluster

    i = 0
    while i < n_clusters :
        ## compute initial cluster centroids
        og_cluster_list = cluster_list
        for cluster in cluster_list :
            for doc in cluster.members :
                similarities = [cosine_similarity(doc, cluster.centroid) for cluster in cluster_list]
                closest_cluster_idx = similarities.index(max(similarities))

                # If the document is closer to a different cluster then move it to said cluster
                if doc not in cluster_list[closest_cluster_idx].members :
                    # Remove the doc from the cluster its in currently
                    cluster.members.remove(cluster.members.index(doc))

                    # move it to the new cluster
                    cluster_list[closest_cluster_idx].members.append(doc)
        # If no docs were moved then we finished
        if og_cluster_list == cluster_list :
            print("Finished K-Means")
            break
        i += 1

        for cluster in cluster_list:
            cluster.calculate_centroid()
    return cluster_list