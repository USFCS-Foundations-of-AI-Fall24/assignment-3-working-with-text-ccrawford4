from unittest import TestCase

from sklearn.linear_model._base import make_dataset

from Cluster import *
from Document import *
from make_dataset import create_docs


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
        documents = []
        pos_docs, neg_docs = create_docs(3, 4)
        for tokens in pos_docs:
            doc = Document(true_class='pos')
            doc.add_tokens(tokens)
            documents.append(doc)

        for tokens in neg_docs :
            doc = Document(true_class='neg')
            doc.add_tokens(tokens)
            documents.append(doc)

        result = k_means(2, ['pos', 'neg'], documents)
        self.assertGreaterEqual(compute_homogeneity(result[0]), 0.75)
        self.assertGreaterEqual(compute_homogeneity(result[1]), 0.75)

