from unittest import TestCase
from matplotlib import pyplot as plt

from Cluster import *
from Document import *
from make_dataset import create_docs

def populate_documents(tokens, true_class, documents) :
    for token in tokens :
        new_doc = Document(true_class=true_class)
        new_doc.add_tokens(token)
        documents.append(new_doc)

class TestCluster(TestCase):
    def test_calculate_centroid(self):
        doc1 = Document()
        doc2 = Document()
        doc1.tokens = {'cat': 2, 'dog': 1, 'lizard': 32}
        doc2.tokens = {'cat': 6, 'dog': 5, 'lizard': 2}
        cluster = Cluster(members=[doc1, doc2])
        cluster.calculate_centroid()
        self.assertEquals(cluster.centroid.tokens, {'cat': 4, 'dog': 3, 'lizard': 17})

    def test_kmeans(self):
        d = Document(true_class='pos')
        d.add_tokens(['cat', 'dog', 'fish'])
        d2 = Document(true_class='pos')
        d2.add_tokens(['cat', 'dog', 'fish'])
        d3 = Document(true_class='neg')
        d3.add_tokens(['bunny', 'lizard', 'octopus'])
        d4 = Document(true_class='neg')
        d4.add_tokens(['bunny', 'lizard', 'turtle'])
        cluster_list = k_means(2, ['pos', 'neg'], [d, d2, d3, d4])

        for cluster in cluster_list :
            if d in cluster.members :
                self.assertTrue(d2 in cluster.members)
            if d3 in cluster.members :
                self.assertTrue(d4 in cluster.members)

    def test_compute_homogeneity(self) :
        # Take the most common thing / total
        documents = []
        pos_docs, neg_docs = create_docs(3, 4)
        populate_documents(pos_docs, 'pos', documents)
        populate_documents(neg_docs, 'neg', documents)
        result = k_means(2, ['pos', 'neg'], documents)
        for cluster in result :
            self.assertGreaterEqual(compute_homogeneity(cluster), 0.75)

    def test_compute_completeness(self) :
        # most common element * how many of the total # of positives
        # the # pos / total # of positives

        # the # of pos in this cluster / the total # of positives
        documents = []
        pos_docs, neg_docs = create_docs(3, 1)
        populate_documents(pos_docs, 'pos', documents)
        populate_documents(neg_docs, 'neg', documents)
        result = k_means(2, ['pos', 'neg'], documents)
        for cluster in result:
            self.assertGreaterEqual(compute_homogeneity(cluster), 0.66666)
