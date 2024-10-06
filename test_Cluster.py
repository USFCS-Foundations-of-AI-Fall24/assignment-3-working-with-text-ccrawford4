from unittest import TestCase
from Cluster import *
from Document import *

class TestCluster(TestCase):
    def test_calculate_centroid(self):
        doc1 = Document()
        doc1.tokens = {'a': 2, 'b': 23, 'c': 13, 'f': -1, 'h': 3, 'i': 3, 'j': 1}
        doc2 = Document()
        doc2.tokens = {'c': 2, 'e': 2, 'f': 3, 'g': 78, 'z': 2}
        expected_result = defaultdict(lambda: 0.0)
        expected_result['f'] = 1.0
        expected_result['c'] = 7.5
        self.assertEqual(calculate_centroid(doc1, doc2).tokens, expected_result)



    def test_kmeans(self):
        d = Document(true_class='pos')
        d.add_tokens(['cat', 'dog', 'fish'])
        d2 = Document(true_class='pos')
        d2.add_tokens(['cat', 'dog', 'fish'])
        d3 = Document(true_class='neg')
        d3.add_tokens(['bunny', 'lizard', 'octopus'])
        print(k_means(2, ['pos', 'neg'], [d,d2,d3]))


